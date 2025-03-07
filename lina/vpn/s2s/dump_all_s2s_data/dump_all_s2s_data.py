import os
import re
import io
import tarfile
from contextlib import redirect_stdout
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
    dump_s2s_menu(selected_peers)

    # Compress and clean up files
    compress_and_cleanup()


def dump_s2s_menu(selected_peers):
    """
    Processes Site-to-Site VPN-related tasks for all selected peers without user interaction.
    Gathers and stores the data in memory.
    """
    for peer in selected_peers:
        ip_address, ike_version, vpn_type = peer
        peer_data = {}

        # Capture output for configuration (suppressing console output)
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            if ike_version == 'ikev1' and vpn_type == 'vti':
                s2s_ikev1_vti_config(ip_address)
            elif ike_version == 'ikev1' and vpn_type == 'policy':
                s2s_ikev1_policy_based_config(ip_address)
            elif ike_version == 'ikev2' and vpn_type == 'vti':
                s2s_ikev2_vti_config(ip_address)
            elif ike_version == 'ikev2' and vpn_type == 'policy':
                s2s_ikev2_policy_based_config(ip_address)

        peer_data['configuration'] = buffer.getvalue()

        # Suppress output for IPSec SA Detail
        buffer_ipsec = io.StringIO()
        with redirect_stdout(buffer_ipsec):
            crypto_ipsec_sa_detail([peer])
        peer_data['ipsec_sa_detail'] = buffer_ipsec.getvalue()

        # Suppress output for ISAKMP SA Detail
        buffer_isakmp = io.StringIO()
        with redirect_stdout(buffer_isakmp):
            crypto_isakmp_sa_detail()
        peer_data['isakmp_sa_detail'] = buffer_isakmp.getvalue()

        # Suppress output for Crypto Accelerator Data
        buffer_crypto = io.StringIO()
        with redirect_stdout(buffer_crypto):
            s2s_crypto_accelerator_data()
        peer_data['crypto_accelerator_data'] = buffer_crypto.getvalue()

        # Save data for the peer
        save_peer_data(ip_address, peer_data)


def save_output_to_file(ip_address, data):
    """
    Saves specific data type output directly to a file for a given peer.
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = f"/var/log/fp_troubleshooting_data/{ip_address}_{timestamp}_s2s_dump.txt"
    with open(file_path, 'a') as f:
        if isinstance(data, dict):
            for key, value in data.items():
                f.write(f"{key}: {value}\n")
        else:
            f.write(data if isinstance(data, str) else str(data))
        f.write("\n\n")


def save_peer_data(ip_address, data):
    """
    Saves collected peer data into a single file.
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = f"/var/log/fp_troubleshooting_data/{ip_address}_{timestamp}_s2s_dump.txt"
    with open(file_path, 'w') as f:
        for key, value in data.items():
            if isinstance(value, dict):
                for sub_key, sub_value in value.items():
                    f.write(f"{sub_key}: {sub_value}\n")
            else:
                f.write(value if isinstance(value, str) else str(value))
            f.write("\n\n")


def compress_and_cleanup():
    """
    Compresses all S2S dump files into a single archive and removes the original files.
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    base_dir = "/var/log/fp_troubleshooting_data/"
    archive_name = f"{base_dir}{timestamp}_s2s_data.tar.gz"

    with tarfile.open(archive_name, "w:gz") as tar:
        for file in os.listdir(base_dir):
            if file.endswith("_s2s_dump.txt"):
                tar.add(os.path.join(base_dir, file), arcname=file)
                os.remove(os.path.join(base_dir, file))

    print(f"Data has been successfully compressed and saved to {archive_name}")
