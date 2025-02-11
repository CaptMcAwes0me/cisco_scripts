import os
import json
import shutil
import re
from datetime import datetime
from core.utils import get_and_parse_cli_output, ip_sort_key
from lina.vpn.s2s.s2s_config.s2s_config import (
    s2s_ikev1_vti_config,
    s2s_ikev1_policy_based_config,
    s2s_ikev2_vti_config,
    s2s_ikev2_policy_based_config
)
from lina.vpn.s2s.s2s_crypto_accelerator_data.s2s_crypto_accelerator_data import s2s_crypto_accelerator_data
from lina.vpn.s2s.crypto_isakmp_sa_detail.crypto_isakmp_sa_detail import crypto_isakmp_sa_detail
from lina.vpn.s2s.crypto_ipsec_sa_detail.crypto_ipsec_sa_detail import crypto_ipsec_sa_detail


def dump_s2s_tunnel_groups():
    """
    Gathers all IPSec S2S tunnels, identifies IKE version, and categorizes as Policy-Based or VTI.
    Stores all tunnel groups in memory without user interaction.
    """
    command = "show running-config tunnel-group | include type ipsec-l2l"
    cli_output = get_and_parse_cli_output(command)

    # Store categories
    ikev1_policy_based = []
    ikev1_vti = []
    ikev2_policy_based = []
    ikev2_vti = []

    # Gather unique IPs
    tunnel_groups = sorted(set([line.split()[1] for line in cli_output.splitlines() if line.startswith("tunnel-group")]), key=ip_sort_key)

    # Process each IP
    for ip in tunnel_groups:
        tunnel_output = get_and_parse_cli_output(f"show running-config tunnel-group {ip}")

        # Determine IKE version
        ikev1 = bool(re.search(r"ikev1 pre-shared-key", tunnel_output))
        ikev2 = bool(re.search(r"ikev2 (remote|local)-authentication pre-shared-key", tunnel_output))

        # Check for Virtual Tunnel Interface
        vti_output = get_and_parse_cli_output("show running-config interface | begin Tunnel")
        vti_match = re.search(rf"tunnel destination {re.escape(ip)}", vti_output)

        # Check for Policy-Based VPN
        policy_output = get_and_parse_cli_output("show running-config crypto map")
        policy_match = re.search(rf"set peer {re.escape(ip)}", policy_output)

        # Categorize and append tuples with (IP, IKE version, VPN type)
        if ikev1:
            if vti_match:
                ikev1_vti.append((ip, 'ikev1', 'vti'))
            if policy_match:
                ikev1_policy_based.append((ip, 'ikev1', 'policy'))

        if ikev2:
            if vti_match:
                ikev2_vti.append((ip, 'ikev2', 'vti'))
            if policy_match:
                ikev2_policy_based.append((ip, 'ikev2', 'policy'))

    # Store all tunnel groups in memory
    selected_peers = ikev1_policy_based + ikev1_vti + ikev2_policy_based + ikev2_vti

    # Proceed with data dump for all selected peers
    collected_data = dump_s2s_menu(selected_peers)

    # Save collected data to files
    save_collected_data(collected_data)


def dump_s2s_menu(selected_peers):
    """
    Processes Site-to-Site VPN-related tasks for all selected peers without user interaction.
    Gathers and stores the data in memory.
    """
    collected_data = {}

    for peer in selected_peers:
        ip_address, ike_version, vpn_type = peer
        peer_data = {}

        # Gather Site-to-Site Configuration
        if ike_version == 'ikev1' and vpn_type == 'vti':
            peer_data['configuration'] = s2s_ikev1_vti_config(ip_address)
        elif ike_version == 'ikev1' and vpn_type == 'policy':
            peer_data['configuration'] = s2s_ikev1_policy_based_config(ip_address)
        elif ike_version == 'ikev2' and vpn_type == 'vti':
            peer_data['configuration'] = s2s_ikev2_vti_config(ip_address)
        elif ike_version == 'ikev2' and vpn_type == 'policy':
            peer_data['configuration'] = s2s_ikev2_policy_based_config(ip_address)

        # Gather Crypto IPSec SA Detail
        peer_data['ipsec_sa_detail'] = crypto_ipsec_sa_detail(peer_data)

        # Store data in the dictionary with IP as the key
        collected_data[ip_address] = peer_data

        # Save Crypto ISAKMP SA Detail directly to file
        save_output_to_file(ip_address, 'isakmp_sa_detail', crypto_isakmp_sa_detail())

        # Save Crypto Accelerator Data directly to file
        save_output_to_file(ip_address, 'crypto_accelerator_data', s2s_crypto_accelerator_data())

    return collected_data


def save_output_to_file(ip_address, data_type, data):
    """
    Saves specific data type output directly to a file for a given peer.
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    base_dir = f"/var/log/fp_troubleshooting_data/{timestamp}_s2s_dump/{timestamp}_{ip_address}_s2s_dump"
    os.makedirs(base_dir, exist_ok=True)

    file_path = os.path.join(base_dir, f"{timestamp}_{ip_address}_{data_type}.txt")
    with open(file_path, 'w') as f:
        f.write(data)


def save_collected_data(collected_data):
    """
    Saves the collected data for each peer into individual files and compresses them.
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    base_dir = f"/var/log/fp_troubleshooting_data/{timestamp}_s2s_dump"
    os.makedirs(base_dir, exist_ok=True)

    # Save data for each peer
    for ip_address, data in collected_data.items():
        peer_dir = os.path.join(base_dir, f"{timestamp}_{ip_address}_s2s_dump")
        os.makedirs(peer_dir, exist_ok=True)

        file_path = os.path.join(peer_dir, f"{timestamp}_{ip_address}_s2s_dump.json")
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=4)

    # Compress all peer directories into a single archive
    compressed_file = f"/var/log/fp_troubleshooting_data/{timestamp}_s2s_dump.tar.gz"
    shutil.make_archive(base_dir, 'gztar', base_dir)

    # Optionally, remove the uncompressed directory after archiving
    shutil.rmtree(base_dir)

    print(f"Data has been collected and saved to {compressed_file}")
