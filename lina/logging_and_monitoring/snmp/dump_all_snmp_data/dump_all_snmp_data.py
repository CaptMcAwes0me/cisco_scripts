import os
from datetime import datetime
from lina.logging_and_monitoring.snmp.snmp_config.snmp_config import snmp_config
from lina.logging_and_monitoring.snmp.snmp_engineid.snmp_engineid import snmp_engineid
from lina.logging_and_monitoring.snmp.snmp_group.snmp_group import snmp_group
from lina.logging_and_monitoring.snmp.snmp_host.snmp_host import snmp_host
from lina.logging_and_monitoring.snmp.snmp_user.snmp_user import snmp_user
from lina.logging_and_monitoring.snmp.snmp_stats.snmp_stats import snmp_stats


def dump_all_snmp_data():
    """Gathers output from all SNMP-related commands and writes them to a log file under
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
    log_file = os.path.join(troubleshooting_dir, f"{timestamp}_snmp_dump.log")

    try:
        # Gather outputs
        data_to_dump = [
            ("SNMP Configuration", snmp_config(suppress_output=True)),
            ("SNMP Engine ID", snmp_engineid(suppress_output=True)),
            ("SNMP Group", snmp_group(suppress_output=True)),
            ("SNMP Host", snmp_host(suppress_output=True)),
            ("SNMP User", snmp_user(suppress_output=True)),
            ("SNMP Statistics", snmp_stats(suppress_output=True)),
        ]

        # Write all outputs to the log file
        with open(log_file, "w") as f:
            for title, output in data_to_dump:
                f.write(f"{'=' * 80}\n")
                f.write(f"{title}\n")
                f.write(f"{'-' * 80}\n")
                f.write(f"{output}\n")
                f.write(f"{'=' * 80}\n\n")

        print(f"\n[+] All SNMP data written to: {log_file}")

    except Exception as e:
        print(f"[!] Error writing SNMP data to file: {e}")
