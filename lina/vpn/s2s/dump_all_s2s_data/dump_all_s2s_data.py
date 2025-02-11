import io
from contextlib import redirect_stdout
from datetime import datetime
import os
import shutil
from lina.vpn.s2s.s2s_config.s2s_config import (
    s2s_ikev1_vti_config,
    s2s_ikev1_policy_based_config,
    s2s_ikev2_vti_config,
    s2s_ikev2_policy_based_config
)
from lina.vpn.s2s.s2s_crypto_accelerator_data.s2s_crypto_accelerator_data import s2s_crypto_accelerator_data
from lina.vpn.s2s.crypto_isakmp_sa_detail.crypto_isakmp_sa_detail import crypto_isakmp_sa_detail
from lina.vpn.s2s.crypto_ipsec_sa_detail.crypto_ipsec_sa_detail import crypto_ipsec_sa_detail


def capture_function_output(func, *args, **kwargs):
    """Captures printed output from functions that do not return data."""
    buffer = io.StringIO()
    with redirect_stdout(buffer):
        func(*args, **kwargs)
    return buffer.getvalue().strip()  # Return captured output


def dump_all_s2s_data(selected_peers):
    troubleshooting_dir = "/var/log/fp_troubleshooting_data"
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    archive_name = f"{timestamp}_s2s_dump"
    archive_path = os.path.join(troubleshooting_dir, archive_name)

    if not os.path.exists(troubleshooting_dir):
        try:
            os.makedirs(troubleshooting_dir)
            print(f"[+] Created directory: {troubleshooting_dir}")
        except Exception as e:
            print(f"[!] Error creating directory: {e}")
            return

    try:
        for peer in selected_peers:
            ip_address, ike_version, vpn_type = peer
            peer_dir = os.path.join(troubleshooting_dir, f"{ip_address}_{ike_version}_{vpn_type}")

            if not os.path.exists(peer_dir):
                os.makedirs(peer_dir)

            log_file = os.path.join(peer_dir, f"{ip_address}_s2s_data.log")
            data_to_dump = []

            # ✅ Capture printed output from the s2s_ike* functions
            if ike_version == 'ikev1' and vpn_type == 'vti':
                output = capture_function_output(s2s_ikev1_vti_config, ip_address)
                data_to_dump.append(("IKEv1 VTI Config", output or "No data available"))

            elif ike_version == 'ikev1' and vpn_type == 'policy':
                output = capture_function_output(s2s_ikev1_policy_based_config, ip_address)
                data_to_dump.append(("IKEv1 Policy-Based Config", output or "No data available"))

            elif ike_version == 'ikev2' and vpn_type == 'vti':
                output = capture_function_output(s2s_ikev2_vti_config, ip_address)
                data_to_dump.append(("IKEv2 VTI Config", output or "No data available"))

            elif ike_version == 'ikev2' and vpn_type == 'policy':
                output = capture_function_output(s2s_ikev2_policy_based_config, ip_address)
                data_to_dump.append(("IKEv2 Policy-Based Config", output or "No data available"))

            # ✅ Gather Additional VPN-Related Data
            data_to_dump.append(("Crypto ISAKMP SA Detail", capture_function_output(crypto_isakmp_sa_detail, suppress_output=True)))
            data_to_dump.append(("Crypto IPSec SA Detail", capture_function_output(crypto_ipsec_sa_detail, selected_peers=[peer])))
            data_to_dump.append(("Crypto Accelerator Data", capture_function_output(s2s_crypto_accelerator_data, suppress_output=True)))

            # ✅ Write gathered data to log file
            with open(log_file, "w") as f:
                for title, output in data_to_dump:
                    f.write(f"{'=' * 80}\n")
                    f.write(f"{title}\n")
                    f.write(f"{'-' * 80}\n")
                    f.write(f"{output}\n" if output else "No data available\n")
                    f.write(f"{'=' * 80}\n\n")

        # ✅ Compress all peer directories into a single archive
        shutil.make_archive(archive_path, 'zip', troubleshooting_dir)
        print(f"\n[+] All Site-to-Site VPN data archived to: {archive_path}.zip")

    except Exception as e:
        print(f"[!] Error writing Site-to-Site VPN data to file: {e}")
