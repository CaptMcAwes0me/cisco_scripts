import os
from datetime import datetime
from lina.nat.nat_running_config.nat_running_config import nat_running_config
from lina.nat.nat_detail.nat_detail import nat_detail
from lina.nat.xlate_count.xlate_count import xlate_count
from lina.nat.xlate_detail.xlate_detail import xlate_detail


def dump_all_nat_data():
    """Gathers output from all NAT commands and writes them to a log file under /var/log/fp_troubleshooting_data."""

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
    log_file = os.path.join(troubleshooting_dir, f"{timestamp}_nat_dump.log")

    try:
        # Gather outputs
        data_to_dump = [
            ("NAT Running Config", nat_running_config(suppress_output=True)),
            ("NAT Detail Table", nat_detail(suppress_output=True)),
            ("Xlate Count", xlate_count(suppress_output=True)),
            ("Xlate Detail Table", xlate_detail(suppress_output=True))
        ]

        # Write all outputs to the log file
        with open(log_file, "w") as f:
            for title, output in data_to_dump:
                f.write(f"{'=' * 80}\n")
                f.write(f"{title}\n")
                f.write(f"{'-' * 80}\n")
                f.write(f"{output}\n")
                f.write(f"{'=' * 80}\n\n")

        print(f"\n[+] All NAT data written to: {log_file}")

    except Exception as e:
        print(f"[!] Error writing NAT data to file: {e}")
