import os
from datetime import datetime
from lina.vpn.s2s.s2s_config.s2s_config import s2s_config
from lina.vpn.s2s.crypto_isakmp_sa_detail.crypto_isakmp_sa_detail import crypto_isakmp_sa_detail
from lina.vpn.s2s.crypto_ipsec_sa_detail_dump.crypto_ipsec_sa_detail_dump import crypto_ipsec_sa_detail_dump


def dump_all_s2s_data():
    """Gathers output from all Site-to-Site VPN-related commands and writes them to a log file under
    /var/log/fp_troubleshooting_data."""

    # Define the directory path
    troubleshooting_dir = "/var/log/fp_troubleshooting_data"

    # Check if the directory exists, if not, create it
    if not os.path.exists(troubleshooting_dir):
        try:
            os.makedirs(troubleshooting_dir)
            print(f"[+] Created directory: {troubleshooting_dir}")
        except Exception as e:
            print(f"[!] Error creating directory: {e}")
            return

    # Generate timestamp for the log file
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = os.path.join(troubleshooting_dir, f"{timestamp}_s2s_dump.log")

    try:
        # Gather outputs
        data_to_dump = [
            ("S2S Configuration", s2s_config(suppress_output=True)),
            ("Crypto ISAKMP SA Detail", crypto_isakmp_sa_detail(suppress_output=True)),
            ("Crypto IPSec SA Detail", crypto_ipsec_sa_detail_dump(suppress_output=True))
        ]

        # Write all outputs to the log file
        with open(log_file, "w") as f:
            for title, output in data_to_dump:
                f.write(f"{'=' * 80}\n")
                f.write(f"{title}\n")
                f.write(f"{'-' * 80}\n")
                f.write(f"{output}\n")
                f.write(f"{'=' * 80}\n\n")

        print(f"\n[+] All Site-to-Site VPN data written to: {log_file}")

    except Exception as e:
        print(f"[!] Error writing Site-to-Site VPN data to file: {e}")
