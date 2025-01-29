import os
from datetime import datetime
from lina.routing.vrf.vrf_running_config.vrf_running_config import vrf_running_config
from lina.routing.vrf.vrf.vrf import vrf
from lina.routing.vrf.vrf_counters.vrf_counters import vrf_counters
from lina.routing.vrf.vrf_detail.vrf_detail import vrf_detail
from lina.routing.vrf.vrf_lock.vrf_lock import vrf_lock
from lina.routing.vrf.vrf_tableid.vrf_tableid import vrf_tableid


def dump_all_vrf_data():
    """Gathers output from all VRF commands and writes them to a log file under /var/log/fp_troubleshooting_data."""

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
    log_file = os.path.join(troubleshooting_dir, f"{timestamp}_vrf_dump.log")

    try:
        # Gather outputs
        data_to_dump = [
            ("VRF Running Configuration", vrf_running_config(suppress_output=True)),
            ("VRF Information", vrf(suppress_output=True)),
            ("VRF Counters", vrf_counters(suppress_output=True)),
            ("VRF Detail", vrf_detail(suppress_output=True)),
            ("VRF Lock", vrf_lock(suppress_output=True)),
            ("VRF Table ID", vrf_tableid(suppress_output=True)),
        ]

        # Write all outputs to the log file
        with open(log_file, "w") as f:
            for title, output in data_to_dump:
                f.write(f"{'=' * 80}\n")
                f.write(f"{title}\n")
                f.write(f"{'-' * 80}\n")
                f.write(f"{output}\n")
                f.write(f"{'=' * 80}\n\n")

        print(f"\n[+] All VRF data written to: {log_file}")

    except Exception as e:
        print(f"[!] Error writing VRF data to file: {e}")
