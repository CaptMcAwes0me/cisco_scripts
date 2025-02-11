import os
from datetime import datetime
from contextlib import redirect_stdout
from lina.vpn.s2s.s2s_config.s2s_config import (
    s2s_ikev1_vti_config,
    s2s_ikev1_policy_based_config,
    s2s_ikev2_vti_config,
    s2s_ikev2_policy_based_config
)
from lina.vpn.s2s.s2s_crypto_accelerator_data.s2s_crypto_accelerator_data import s2s_crypto_accelerator_data
from lina.vpn.s2s.crypto_isakmp_sa_detail.crypto_isakmp_sa_detail import crypto_isakmp_sa_detail
from lina.vpn.s2s.crypto_ipsec_sa_detail.crypto_ipsec_sa_detail import crypto_ipsec_sa_detail


def suppress_function_output(func, *args, **kwargs):
    """Suppresses output of the given function."""
    with open(os.devnull, 'w') as fnull:
        with redirect_stdout(fnull):
            return func(*args, **kwargs)

def dump_all_s2s_data(selected_peers):
    """Gathers output from all Site-to-Site VPN-related commands and writes them to a log file under
    /var/log/fp_troubleshooting_data."""

    troubleshooting_dir = "/var/log/fp_troubleshooting_data"

    if not os.path.exists(troubleshooting_dir):
        try:
            os.makedirs(troubleshooting_dir)
            print(f"[+] Created directory: {troubleshooting_dir}")
        except Exception as e:
            print(f"[!] Error creating directory: {e}")
            return

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = os.path.join(troubleshooting_dir, f"{timestamp}_s2s_dump.log")

    try:
        data_to_dump = []

        # Gather Site-to-Site Configuration Data
        for peer in selected_peers:
            ip_address, ike_version, vpn_type = peer

            if ike_version == 'ikev1' and vpn_type == 'vti':
                data_to_dump.append((f"IKEv1 VTI Config for {ip_address}", suppress_function_output(s2s_ikev1_vti_config, ip_address) or "No data available"))
            elif ike_version == 'ikev1' and vpn_type == 'policy':
                data_to_dump.append((f"IKEv1 Policy-Based Config for {ip_address}", suppress_function_output(s2s_ikev1_policy_based_config, ip_address) or "No data available"))
            elif ike_version == 'ikev2' and vpn_type == 'vti':
                data_to_dump.append((f"IKEv2 VTI Config for {ip_address}", suppress_function_output(s2s_ikev2_vti_config, ip_address) or "No data available"))
            elif ike_version == 'ikev2' and vpn_type == 'policy':
                data_to_dump.append((f"IKEv2 Policy-Based Config for {ip_address}", suppress_function_output(s2s_ikev2_policy_based_config, ip_address) or "No data available"))

        # Gather Additional VPN-Related Data
        data_to_dump.append(("Crypto ISAKMP SA Detail", crypto_isakmp_sa_detail(suppress_output=True)))
        data_to_dump.append(("Crypto IPSec SA Detail", crypto_ipsec_sa_detail(selected_peers=selected_peers)))
        data_to_dump.append(("Crypto Accelerator Data", s2s_crypto_accelerator_data(suppress_output=True)))

        with open(log_file, "w") as f:
            for title, output in data_to_dump:
                f.write(f"{'=' * 80}\n")
                f.write(f"{title}\n")
                f.write(f"{'-' * 80}\n")

                # Handle dictionary outputs
                if isinstance(output, dict):
                    for key, value in output.items():
                        f.write(f"{key}:\n")
                        f.write(f"{'-' * 40}\n")
                        f.write(f"{value}\n")
                        f.write(f"{'-' * 80}\n")

                # Handle single string output
                else:
                    f.write(f"{output}\n")

                f.write(f"{'=' * 80}\n\n")

        print(f"\n[+] All Site-to-Site VPN data written to: {log_file}")

    except Exception as e:
        print(f"[!] Error writing Site-to-Site VPN data to file: {e}")
