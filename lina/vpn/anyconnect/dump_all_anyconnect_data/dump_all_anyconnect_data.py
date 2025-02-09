import os
from datetime import datetime
from lina.vpn.anyconnect.anyconnect_config.anyconnect_config import anyconnect_config_dump
from lina.vpn.anyconnect.vpn_sessiondb_anyconnect_dump.vpn_sessiondb_anyconnect_dump import vpn_sessiondb_anyconnect_dump
from lina.vpn.anyconnect.crypto_ca_data.crypto_ca_data import crypto_ca_data
from lina.vpn.anyconnect.ssl_data.ssl_data import ssl_data


def dump_all_anyconnect_data():
    """Gathers output from all AnyConnect-related commands and writes them to a log file under
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
    log_file = os.path.join(troubleshooting_dir, f"{timestamp}_anyconnect_dump.log")

    try:
        # Gather outputs
        data_to_dump = [
            ("AnyConnect Configuration", anyconnect_config_dump(suppress_output=True)),
            ("VPN Session Database", vpn_sessiondb_anyconnect_dump(suppress_output=True)),
            ("Crypto CA Data", crypto_ca_data(suppress_output=True)),
            ("SSL Data", ssl_data(suppress_output=True)),
        ]

        # Write all outputs to the log file
        with open(log_file, "w") as f:
            for title, output in data_to_dump:
                f.write(f"{'=' * 80}\n")
                f.write(f"{title}\n")
                f.write(f"{'-' * 80}\n")

                # Check if the output is a tuple (multiple outputs)
                if isinstance(output, tuple):
                    for section in output:
                        f.write(f"{section}\n")  # Write each output separately
                        f.write(f"{'-' * 80}\n")  # Optional: separator between outputs
                else:
                    f.write(f"{output}\n")  # Single output

                f.write(f"{'=' * 80}\n\n")

        print(f"\n[+] All AnyConnect data written to: {log_file}")

    except Exception as e:
        print(f"[!] Error writing AnyConnect data to file: {e}")
