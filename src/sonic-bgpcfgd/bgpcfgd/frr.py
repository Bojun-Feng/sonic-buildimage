import json
import os
import datetime
import time
import tempfile

from bgpcfgd.log import log_err, log_info, log_warn, log_crit
from .vars import g_debug
from .utils import run_command


class FRR(object):
    """Proxy object with FRR"""

    # Delay between per-peer soft clears (seconds). Allows bgpd's event loop
    # to process keepalives/hold-timers between clears, preventing session flaps
    # on large peer-groups. See sonic-net/sonic-buildimage#27787.
    STAGGER_DELAY = 0.1

    def __init__(self, daemons):
        self.daemons = daemons

    def wait_for_daemons(self, seconds):
        """
        Wait until FRR daemons are ready for requests
        :param seconds: number of seconds to wait, until raise an error
        """
        stop_time = datetime.datetime.now() + datetime.timedelta(seconds=seconds)
        log_info("Start waiting for FRR daemons: %s" % str(datetime.datetime.now()))
        while datetime.datetime.now() < stop_time:
            ret_code, out, err = run_command(["vtysh", "-c", "show daemons"], hide_errors=True)
            if ret_code == 0 and all(daemon in out for daemon in self.daemons):
                log_info("All required daemons have connected to vtysh: %s" % str(datetime.datetime.now()))
                return
            else:
                log_warn("Can't read daemon status from FRR: %s" % str(err))
            time.sleep(0.1)  # sleep 100 ms
        raise RuntimeError("FRR daemons hasn't been started in %d seconds" % seconds)

    @staticmethod
    def get_config():
        ret_code, out, err = run_command(["vtysh", "-c", "show running-config"])
        if ret_code != 0:
            log_crit("can't update running config: rc=%d out='%s' err='%s'" % (ret_code, out, err))
            return ""
        return out

    @staticmethod
    def write(config_text):
        fd, tmp_filename = tempfile.mkstemp(dir='/tmp')
        os.close(fd)
        with open(tmp_filename, 'w') as fp:
            fp.write("%s\n" % config_text)
        command = ["vtysh", "-f", tmp_filename]
        ret_code, out, err = run_command(command)
        if ret_code != 0:
            err_tuple = tmp_filename, ret_code, out, err
            log_err("ConfigMgr::commit(): can't push configuration from file='%s', rc='%d', stdout='%s', stderr='%s'" % err_tuple)
        else:
            if not g_debug:
                os.remove(tmp_filename)
        return ret_code == 0

    @staticmethod
    def _get_peer_group_members(peer_group):
        """
        Get the list of neighbor addresses belonging to a peer-group.
        :param peer_group: name of the peer-group
        :return: list of neighbor IP address strings, or empty list on failure
        """
        rc, out, err = run_command(["vtysh", "-c", "show bgp peer-group %s json" % peer_group])
        if rc != 0:
            log_warn("Can't get peer-group members for '%s'. rc='%d', err='%s'" % (peer_group, rc, err))
            return []
        try:
            data = json.loads(out)
        except (json.JSONDecodeError, ValueError) as e:
            log_warn("Can't parse peer-group JSON for '%s': %s" % (peer_group, str(e)))
            return []
        # FRR JSON format: {<peer_group>: {"members": {"<ip>": {...}, ...}}}
        if peer_group in data and "members" in data[peer_group]:
            return list(data[peer_group]["members"].keys())
        # Fallback: top-level "members" key
        if "members" in data:
            return list(data["members"].keys())
        return []

    @staticmethod
    def restart_peer_groups(peer_groups):
        """
        Perform soft-inbound clear on peer-groups by clearing each member
        individually with a small stagger delay. This prevents bgpd's
        single-threaded event loop from being monopolized by a bulk
        peer-group clear, which would starve keepalive/hold-timer
        processing and cause session flaps at scale.
        :param peer_groups: List of peer_groups to restart
        :return: True if restart of all peer-groups was successful, False otherwise
        """
        res = True
        for peer_group in sorted(peer_groups):
            members = FRR._get_peer_group_members(peer_group)
            if not members:
                # Fallback: if we can't enumerate members, use the original
                # bulk peer-group clear to maintain correctness
                log_info("restart_peer_groups: falling back to bulk clear for '%s'" % peer_group)
                rc, out, err = run_command(["vtysh", "-c", "clear bgp peer-group %s soft in" % peer_group])
                if rc != 0:
                    log_value = peer_group, rc, out, err
                    log_crit("Can't restart bgp peer-group '%s'. rc='%d', out='%s', err='%s'" % log_value)
                res = res and (rc == 0)
                continue
            log_info("restart_peer_groups: staggering soft clear for '%s' (%d members)" % (peer_group, len(members)))
            for i, neighbor in enumerate(members):
                rc, out, err = run_command(["vtysh", "-c", "clear bgp %s soft in" % neighbor])
                if rc != 0:
                    log_value = neighbor, peer_group, rc, out, err
                    log_crit("Can't soft-clear neighbor '%s' (peer-group '%s'). rc='%d', out='%s', err='%s'" % log_value)
                    res = False
                if i < len(members) - 1:
                    time.sleep(FRR.STAGGER_DELAY)
        return res
