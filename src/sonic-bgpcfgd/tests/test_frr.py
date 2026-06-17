import json
from unittest.mock import patch, MagicMock
import bgpcfgd.frr
import pytest

def test_constructor():
    f = bgpcfgd.frr.FRR(["abc", "cde"])
    assert f.daemons == ["abc", "cde"]

def test_wait_for_daemons():
    bgpcfgd.frr.run_command = lambda cmd, **kwargs: (0, ["abc", "cde"], "")
    f = bgpcfgd.frr.FRR(["abc", "cde"])
    f.wait_for_daemons(5)

def test_wait_for_daemons_fail():
    bgpcfgd.frr.run_command = lambda cmd, **kwargs: (0, ["abc", "non_expected"], "")
    f = bgpcfgd.frr.FRR(["abc", "cde"])
    with pytest.raises(Exception):
        assert f.wait_for_daemons(5)

def test_wait_for_daemons_error():
    bgpcfgd.frr.run_command = lambda cmd, **kwargs: (1, ["abc", "cde"], "some error")
    f = bgpcfgd.frr.FRR(["abc", "cde"])
    with pytest.raises(Exception):
        assert f.wait_for_daemons(5)

def test_get_config():
    bgpcfgd.frr.run_command = lambda cmd: (0, "expected config", "")
    f = bgpcfgd.frr.FRR(["abc", "cde"])
    out = f.get_config()
    assert out == "expected config"

@patch('bgpcfgd.frr.log_crit')
def test_get_config_fail(mocked_log_crit):
    bgpcfgd.frr.run_command = lambda cmd: (1, "some config", "some error")
    f = bgpcfgd.frr.FRR(["abc", "cde"])
    out = f.get_config()
    assert out == ""
    mocked_log_crit.assert_called_with("can't update running config: rc=1 out='some config' err='some error'")

def test_write():
    bgpcfgd.frr.run_command = lambda cmd: (0, "some output", "")
    f = bgpcfgd.frr.FRR(["abc", "cde"])
    res = f.write("config context")
    assert res, "Expect True return value"

def test_write_fail():
    bgpcfgd.frr.run_command = lambda cmd: (1, "some output", "some error")
    f = bgpcfgd.frr.FRR(["abc", "cde"])
    res = f.write("config context")
    assert not res, "Expect False return value"


def test_get_peer_group_members():
    """Test _get_peer_group_members parses FRR JSON correctly"""
    pg_json = json.dumps({
        "PEER_V6": {
            "members": {
                "fc00::7a": {"state": "Established"},
                "fc00::46": {"state": "Established"},
                "fc00::62": {"state": "Established"}
            }
        }
    })
    bgpcfgd.frr.run_command = lambda cmd: (0, pg_json, "")
    members = bgpcfgd.frr.FRR._get_peer_group_members("PEER_V6")
    assert set(members) == {"fc00::7a", "fc00::46", "fc00::62"}


def test_get_peer_group_members_failure():
    """Test _get_peer_group_members returns empty on failure"""
    bgpcfgd.frr.run_command = lambda cmd: (1, "", "some error")
    members = bgpcfgd.frr.FRR._get_peer_group_members("PEER_V6")
    assert members == []


def test_get_peer_group_members_bad_json():
    """Test _get_peer_group_members returns empty on invalid JSON"""
    bgpcfgd.frr.run_command = lambda cmd: (0, "not json", "")
    members = bgpcfgd.frr.FRR._get_peer_group_members("PEER_V6")
    assert members == []


@patch('bgpcfgd.frr.time.sleep')
def test_restart_peer_groups_staggered(mock_sleep):
    """Test staggered per-peer soft clear when members are enumerable"""
    pg_json = json.dumps({
        "pg_1": {
            "members": {
                "10.0.0.1": {},
                "10.0.0.2": {}
            }
        }
    })
    cleared_peers = []

    def mock_run_command(cmd):
        cmd_str = str(cmd)
        if "show bgp peer-group" in cmd_str:
            return (0, pg_json, "")
        if "clear bgp" in cmd_str:
            cleared_peers.append(cmd)
            return (0, "", "")
        return (0, "", "")

    bgpcfgd.frr.run_command = mock_run_command
    f = bgpcfgd.frr.FRR(["bgpd"])
    res = f.restart_peer_groups(["pg_1"])
    assert res, "Expect True return value"
    # Should clear individual peers, not peer-group
    assert len(cleared_peers) == 2
    assert any("10.0.0.1" in str(c) for c in cleared_peers)
    assert any("10.0.0.2" in str(c) for c in cleared_peers)
    # Sleep should be called between peers (once for 2 peers)
    assert mock_sleep.call_count == 1


@patch('bgpcfgd.frr.time.sleep')
def test_restart_peer_groups_fallback_on_empty_members(mock_sleep):
    """Test fallback to bulk peer-group clear when members can't be enumerated"""
    cleared = []

    def mock_run_command(cmd):
        cmd_str = str(cmd)
        if "show bgp peer-group" in cmd_str:
            return (0, "{}", "")
        if "clear bgp peer-group" in cmd_str:
            cleared.append(cmd)
            return (0, "", "")
        return (0, "", "")

    bgpcfgd.frr.run_command = mock_run_command
    f = bgpcfgd.frr.FRR(["bgpd"])
    res = f.restart_peer_groups(["pg_1"])
    assert res, "Expect True return value"
    # Should fall back to bulk clear
    assert len(cleared) == 1
    assert "peer-group" in str(cleared[0])
    # No stagger delay needed for fallback
    mock_sleep.assert_not_called()


@patch('bgpcfgd.frr.time.sleep')
@patch('bgpcfgd.frr.log_crit')
def test_restart_peer_groups_per_peer_failure(mocked_log_crit, mock_sleep):
    """Test that failure on individual peer clear is reported correctly"""
    pg_json = json.dumps({
        "pg_1": {
            "members": {
                "10.0.0.1": {},
                "10.0.0.2": {}
            }
        }
    })

    def mock_run_command(cmd):
        cmd_str = str(cmd)
        if "show bgp peer-group" in cmd_str:
            return (0, pg_json, "")
        if "10.0.0.2" in cmd_str:
            return (1, "some output", "some error")
        return (0, "", "")

    bgpcfgd.frr.run_command = mock_run_command
    f = bgpcfgd.frr.FRR(["bgpd"])
    res = f.restart_peer_groups(["pg_1"])
    assert not res, "Expect False when a peer clear fails"
    mocked_log_crit.assert_called()


@patch('bgpcfgd.frr.time.sleep')
def test_restart_peer_groups_multiple_groups(mock_sleep):
    """Test staggered clear across multiple peer-groups"""
    def make_pg_json(pg_name, members):
        return json.dumps({pg_name: {"members": {m: {} for m in members}}})

    cleared_peers = []

    def mock_run_command(cmd):
        cmd_str = str(cmd)
        if "show bgp peer-group pg_1" in cmd_str:
            return (0, make_pg_json("pg_1", ["10.0.0.1", "10.0.0.2"]), "")
        if "show bgp peer-group pg_2" in cmd_str:
            return (0, make_pg_json("pg_2", ["fc00::1"]), "")
        if "clear bgp" in cmd_str:
            cleared_peers.append(cmd)
            return (0, "", "")
        return (0, "", "")

    bgpcfgd.frr.run_command = mock_run_command
    f = bgpcfgd.frr.FRR(["bgpd"])
    res = f.restart_peer_groups(["pg_1", "pg_2"])
    assert res, "Expect True return value"
    # 2 peers in pg_1 + 1 peer in pg_2 = 3 clears total
    assert len(cleared_peers) == 3
    # Sleep between peers within a group: 1 for pg_1, 0 for pg_2 (single member)
    assert mock_sleep.call_count == 1


def test_get_peer_group_members_toplevel_members():
    """Test fallback to top-level 'members' key"""
    pg_json = json.dumps({"members": {"10.0.0.1": {}, "10.0.0.2": {}}})
    bgpcfgd.frr.run_command = lambda cmd: (0, pg_json, "")
    members = bgpcfgd.frr.FRR._get_peer_group_members("PEER_V4")
    assert set(members) == {"10.0.0.1", "10.0.0.2"}
