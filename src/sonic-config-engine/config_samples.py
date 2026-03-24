import sys

from collections import defaultdict
from ipaddress import ip_interface
from natsort import natsorted

import smartswitch_config
from sonic_py_common import device_info

#TODO: Remove once Python 2 support is removed
if sys.version_info.major == 3:
    UNICODE_TYPE = str
else:
    UNICODE_TYPE = unicode

def generate_common_config(data):
    data['FLEX_COUNTER_TABLE'] = {
        'ACL': {
            'FLEX_COUNTER_STATUS': 'disable',
            'POLL_INTERVAL': '10000'
        }
    }
    return data

# The following config generation methods exits:
#    't1': generate_t1_sample_config,
#    'l2': generate_l2_config,
#    'empty': generate_empty_config,
#    'l1': generate_l1_config,
#    'l3': generate_l3_config

def generate_l1_config(data):
    for port in natsorted(data['PORT']):
        data['PORT'][port]['admin_status'] = 'up'
        data['PORT'][port]['mtu'] = '9100'
    return data;

def generate_l3_config(data):
    data['LOOPBACK_INTERFACE'] = {"Loopback0": {},
                                  "Loopback0|10.1.0.1/32": {}}
    data['BGP_NEIGHBOR'] = {}
    data['DEVICE_NEIGHBOR'] = {}
    data['INTERFACE'] = {}
    for port in natsorted(data['PORT']):
        data['PORT'][port]['admin_status'] = 'up'
        data['PORT'][port]['mtu'] = '9100'
        data['INTERFACE']['{}'.format(port)] = {}
    return data;

def generate_t1_sample_config(data):
    data['DEVICE_METADATA']['localhost']['hostname'] = 'sonic'
    data['DEVICE_METADATA']['localhost']['type'] = 'LeafRouter'
    data['DEVICE_METADATA']['localhost']['bgp_asn'] = '65100'
    data['LOOPBACK_INTERFACE'] = {"Loopback0": {},
                                  "Loopback0|10.1.0.1/32": {}}
    data['BGP_NEIGHBOR'] = {}
    data['DEVICE_NEIGHBOR'] = {}
    data['INTERFACE'] = {}
    port_count = 0
    total_port_amount = len(data['PORT'])
    for port in natsorted(data['PORT']):
        data['PORT'][port]['admin_status'] = 'up'
        data['PORT'][port]['mtu'] = '9100'
        local_addr = '10.0.{}.{}'.format(2 * port_count // 256, 2 * port_count % 256)
        peer_addr = '10.0.{}.{}'.format(2 * port_count // 256, 2 * port_count % 256 + 1)
        peer_name='ARISTA{0:02d}{1}'.format(1+port_count%(total_port_amount // 2), 'T2' if port_count < (total_port_amount // 2) else 'T0')
        peer_asn = 65200 if port_count < (total_port_amount // 2) else 64001 + port_count - (total_port_amount // 2)
        data['INTERFACE']['{}'.format(port)] = {}
        data['INTERFACE']['{}|{}/31'.format(port, local_addr)] = {}
        data['BGP_NEIGHBOR'][peer_addr] = {
                'rrclient': 0,
                'name': peer_name,
                'local_addr': local_addr,
                'nhopself': 0,
                'holdtime': '180',
                'asn': str(peer_asn),
                'keepalive': '60'
                }
        port_count += 1
    return data

def generate_t1_smartswitch_switch_sample_config(data, ss_config):
    data = generate_t1_sample_config(data)
    data['DEVICE_METADATA']['localhost']['subtype'] = 'SmartSwitch'

    mpbr_prefix = '169.254.200'
    mpbr_address = '{}.254'.format(mpbr_prefix)

    bridge_name = 'bridge-midplane'

    data['MID_PLANE_BRIDGE'] = {
        "GLOBAL": {
            "bridge": bridge_name,
            "ip_prefix": "169.254.200.254/24"
        }
    }
    dhcp_server_ports = {}
    dpu_midplane_dict = {}

    for dpu_name in natsorted(ss_config.get('DPUS', {})):
        midplane_interface = ss_config['DPUS'][dpu_name]['midplane_interface']
        dpu_midplane_dict[dpu_name] = {'midplane_interface': midplane_interface}
        dpu_id = int(midplane_interface.replace('dpu', ''))
        dhcp_server_ports['{}|{}'.format(bridge_name, midplane_interface)] = {'ips': ['{}.{}'.format(mpbr_prefix, dpu_id + 1)]}

    if dhcp_server_ports:
        data['DPUS'] = dpu_midplane_dict

        data['FEATURE'] = {
            "dhcp_relay": {
                "auto_restart": "enabled",
                "check_up_status": "False",
                "delayed": "False",
                "has_global_scope": "True",
                "has_per_asic_scope": "False",
                "high_mem_alert": "disabled",
                "set_owner": "local",
                "state": "enabled",
                "support_syslog_rate_limit": "True"
            },
            "dhcp_server": {
                "auto_restart": "enabled",
                "check_up_status": "False",
                "delayed": "False",
                "has_global_scope": "True",
                "has_per_asic_scope": "False",
                "high_mem_alert": "disabled",
                "set_owner": "local",
                "state": "enabled",
                "support_syslog_rate_limit": "False"
            }
        }

        data['DHCP_SERVER_IPV4'] = {
            bridge_name: {
                'gateway': mpbr_address,
                'lease_time': '3600',
                'mode': 'PORT',
                'netmask': '255.255.255.0',
                "state": "enabled"
            }
        }

        data['DHCP_SERVER_IPV4_PORT'] = dhcp_server_ports

    data['NTP'] = {
        "global": {
            "server_role": "enabled"
        }
    }

    return data

def generate_t1_smartswitch_dpu_sample_config(data, ss_config):
    data['DEVICE_METADATA']['localhost']['hostname'] = 'sonic'
    data['DEVICE_METADATA']['localhost']['switch_type'] = 'dpu'
    data['DEVICE_METADATA']['localhost']['type'] = 'SmartSwitchDPU'
    data['DEVICE_METADATA']['localhost']['subtype'] = 'SmartSwitch'
    data['DEVICE_METADATA']['localhost']['bgp_asn'] = '65100'

    if "SYSTEM_DEFAULTS" not in data:
        data["SYSTEM_DEFAULTS"] = {}

    for port in natsorted(data['PORT']):
        data['PORT'][port]['admin_status'] = 'up'
        data['PORT'][port]['mtu'] = '9100'

    dash_crm_resources = ["vnet", "eni", "eni_ether_address_map", "ipv4_inbound_routing", "ipv6_inbound_routing", "ipv4_outbound_routing",
                          "ipv6_outbound_routing", "ipv4_pa_validation", "ipv6_pa_validation", "ipv4_outbound_ca_to_pa", "ipv6_outbound_ca_to_pa",
                          "ipv4_acl_group", "ipv6_acl_group", "ipv4_acl_rule", "ipv6_acl_rule"]
    dash_crm_thresholds = dict([thresholds for res in dash_crm_resources for thresholds in (
            (f"dash_{res}_threshold_type", "percentage"),
            (f"dash_{res}_low_threshold", "70"),
            (f"dash_{res}_high_threshold", "85")
        )])

    crmconfig = data.setdefault('CRM', {}).setdefault('Config', {})
    crmconfig.update(dash_crm_thresholds)

    if "pensando" in data['DEVICE_METADATA']['localhost']['hwsku'].lower():
        data['SYSTEM_DEFAULTS'] = {
            "polaris": {
                "status": "enabled"
            }
        }

    data["SYSTEM_DEFAULTS"]["software_bfd"] = {
        "status": "enabled"
    }

    data['NTP_SERVER'] = {
        "169.254.200.254": {
            "iburst": "on"
        }
    }

    data['NTP'] = {
        "global": {
            "admin_state": "enabled",
            "authentication": "disabled",
            "dhcp": "enabled",
            "server_role": "disabled",
            "src_intf": "eth0",
            "vrf": "default"
        }
    }

    return data

def generate_t1_smartswitch_sample_config(data):
    ss_config = smartswitch_config.get_smartswitch_config(data['DEVICE_METADATA']['localhost']['hwsku'])

    if smartswitch_config.DPU_TABLE in ss_config:
        return generate_t1_smartswitch_dpu_sample_config(data, ss_config)

    return generate_t1_smartswitch_switch_sample_config(data, ss_config)

def generate_empty_config(data):
    new_data = {'DEVICE_METADATA': data['DEVICE_METADATA']}
    if 'hostname' not in new_data['DEVICE_METADATA']['localhost']:
        new_data['DEVICE_METADATA']['localhost']['hostname'] = 'sonic'
    if 'type' not in new_data['DEVICE_METADATA']['localhost']:
        new_data['DEVICE_METADATA']['localhost']['type'] = 'LeafRouter'
    return new_data

def generate_global_dualtor_tables():
    data = defaultdict(lambda: defaultdict(dict))
    data['LOOPBACK_INTERFACE'] = {
                                    'Loopback2': {},
                                    'Loopback2|3.3.3.3/32': {}
                                    }
    data['MUX_CABLE'] = {}
    data['PEER_SWITCH'] = {
                            "peer_switch_hostname": {
                                "address_ipv4": "1.1.1.1"
                            }
                            }
    data['TUNNEL'] = {
                        "MuxTunnel0": {
                            "dscp_mode": "uniform",
                            "dst_ip": "2.2.2.2",
                            "ecn_mode": "copy_from_outer",
                            "encap_ecn_mode": "standard",
                            "ttl_mode": "pipe",
                            "tunnel_type": "IPINIP"
                        }
                    }
    return data

def generate_l2_config(data):
    # Check if dual ToR configs are needed
    if 'is_dualtor' in data and data['is_dualtor']:
        is_dualtor = True
        data.pop('is_dualtor')
    else:
        is_dualtor = False

    if 'uplinks' in data:
        uplinks = data['uplinks']
        data.pop('uplinks')

    if 'downlinks' in data:
        downlinks = data['downlinks']
        data.pop('downlinks')

    # VLAN initial data
    data['VLAN'] = {'Vlan1000': {'vlanid': '1000'}}
    data['VLAN_MEMBER'] = {}

    if is_dualtor:
        data['DEVICE_METADATA']['localhost']['subtype'] = 'DualToR'
        data['DEVICE_METADATA']['localhost']['peer_switch'] = 'peer_switch_hostname'
        data.update(generate_global_dualtor_tables())

        server_ipv4_base = ip_interface(UNICODE_TYPE('192.168.0.1/32'))
        server_ipv6_base = ip_interface(UNICODE_TYPE('fc02:1000::1/128'))
        server_offset = 1
    for port in natsorted(data['PORT']):
        if is_dualtor:
            # Ports in use should be admin up, unused ports default to admin down
            if port in downlinks or port in uplinks:
                data['PORT'][port].setdefault('admin_status', 'up')
                data['VLAN_MEMBER']['Vlan1000|{}'.format(port)] = {'tagging_mode': 'untagged'}

            # Downlinks (connected to mux cable) need a MUX_CABLE entry
            # as well as the `mux_cable` field in the PORT table
            if port in downlinks:
                mux_cable_entry = {
                    'server_ipv4': str(server_ipv4_base + server_offset),
                    'server_ipv6': str(server_ipv6_base + server_offset),
                    'state': 'auto'
                }
                server_offset += 1
                data['MUX_CABLE'][port] = mux_cable_entry
                data['PORT'][port]['mux_cable'] = 'true'
        else:
            data['PORT'][port].setdefault('admin_status', 'up')
            data['VLAN_MEMBER']['Vlan1000|{}'.format(port)] = {'tagging_mode': 'untagged'}
    return data


def is_voq_platform():
    """Check if the platform is a VoQ platform by reading platform_env.conf."""
    platform_env_conf_file_path = device_info.get_platform_env_conf_file_path()
    if platform_env_conf_file_path is None:
        return False
    try:
        with open(platform_env_conf_file_path) as f:
            for line in f:
                tokens = line.split('=')
                if len(tokens) < 2:
                    continue
                if tokens[0].strip().lower() == 'voq':
                    if tokens[1].strip() == '1':
                        return True
    except Exception:
        pass
    return False

def generate_voq_system_ports(data):
    """Generate VoQ DEVICE_METADATA and SYSTEM_PORT table from PORT data.

    For VoQ platforms, the DEVICE_METADATA needs switch_type, switch_id,
    max_cores, and asic_name. The SYSTEM_PORT table is derived from PORT
    entries that contain core_id, core_port_id, num_voq, and speed fields.

    The system_port_id for each port is calculated as:
        port_index (0-based, in PORT iteration order) * num_voq + 1
    This reserves num_voq queue IDs per system port in the hardware.

    This targets standalone single-ASIC VoQ switches (switch_id=0, asic_name=asic0).
    Multi-linecard or multi-ASIC chassis deployments use minigraph-based config.
    """
    hostname = data.get('DEVICE_METADATA', {}).get('localhost', {}).get('hostname', 'sonic')

    # Generate SYSTEM_PORT table from PORT data
    system_ports = {}
    max_core_id = 0
    port_index = 0
    for port_name in natsorted(data.get('PORT', {})):
        port_data = data['PORT'][port_name]
        core_id = port_data.get('core_id')
        core_port_id = port_data.get('core_port_id')
        num_voq = int(port_data.get('num_voq', 8))
        speed = port_data.get('speed')

        # Skip ports without VoQ-related fields
        if core_id is None or core_port_id is None:
            continue

        try:
            max_core_id = max(max_core_id, int(core_id))
        except (ValueError, TypeError):
            pass

        system_port_id = port_index * num_voq + 1
        key = '{}|asic0|{}'.format(hostname, port_name)
        system_ports[key] = {
            'system_port_id': str(system_port_id),
            'switch_id': '0',
            'core_index': str(core_id),
            'core_port_index': str(core_port_id),
            'speed': str(speed) if speed else '400000',
            'num_voq': str(num_voq)
        }
        port_index += 1

    # Only add VoQ metadata and SYSTEM_PORT if valid ports were found
    if system_ports:
        max_cores = max_core_id + 1
        data.setdefault('DEVICE_METADATA', {}).setdefault('localhost', {})
        data['DEVICE_METADATA']['localhost']['switch_type'] = 'voq'
        data['DEVICE_METADATA']['localhost']['switch_id'] = 0
        data['DEVICE_METADATA']['localhost']['max_cores'] = max_cores
        data['DEVICE_METADATA']['localhost']['asic_name'] = 'asic0'
        data['SYSTEM_PORT'] = system_ports

    return data

_sample_generators = {
        't1': generate_t1_sample_config,
        'l2': generate_l2_config,
        't1-smartswitch': generate_t1_smartswitch_sample_config,
        'empty': generate_empty_config,
        'l1': generate_l1_config,
        'l3': generate_l3_config
        }

def get_available_config():
    return list(_sample_generators.keys())

def generate_sample_config(data, setting_name):
    data = generate_common_config(data)
    data = _sample_generators[setting_name.lower()](data)
    if is_voq_platform():
        data = generate_voq_system_ports(data)
    return data
