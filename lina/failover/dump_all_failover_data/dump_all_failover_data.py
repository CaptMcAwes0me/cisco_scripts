import os
from datetime import datetime
from lina.failover.failover_running_config.failover_running_config import failover_running_config
from lina.failover.failover_state.failover_state import failover_state
from lina.failover.failover.failover import failover
from lina.failover.failover_details.failover_details import failover_details
from lina.failover.failover_interface.failover_interface import failover_interface
from lina.failover.failover_descriptor.failover_descriptor import failover_descriptor
from lina.failover.failover_config_sync_status.failover_config_sync_status import failover_config_sync_status
from lina.failover.failover_app_sync_stats.failover_app_sync_stats import failover_app_sync_stats


def dump_all_failover_data():
    """Gathers output from all failover-related commands and writes them to a log file under
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
    log_file = os.path.join(troubleshooting_dir, f"{timestamp}_failover_dump.log")

    try:
        # Gather outputs in the requested order
        data_to_dump = [
            ("Failover Running Config", failover_running_config(suppress_output=True)),
            ("Failover State", failover_state(suppress_output=True)),
            ("Failover", failover(suppress_output=True)),
            ("Failover Details", failover_details(suppress_output=True)),
            ("Failover Interface", failover_interface(suppress_output=True)),
            ("Failover Descriptor", failover_descriptor(suppress_output=True)),
            ("Failover Config Sync Status", failover_config_sync_status(suppress_output=True)),
            ("Failover Application Sync Stats", failover_app_sync_stats(suppress_output=True)),
        ]

        # Write all outputs to the log file
        with open(log_file, "w") as f:
            for title, output in data_to_dump:
                f.write(f"{'=' * 80}\n")
                f.write(f"{title}\n")
                f.write(f"{'-' * 80}\n")
                f.write(f"{output}\n")
                f.write(f"{'=' * 80}\n\n")

        print(f"\n[+] All failover data written to: {log_file}")

    except Exception as e:
        print(f"[!] Error writing failover data to file: {e}")
