import os
from datetime import datetime
from lina.connectivity_and_traffic.arp.arp import arp_dump
from lina.connectivity_and_traffic.conn.conn import conn_detail_dump
from lina.connectivity_and_traffic.sla_config.sla_config import sla_config
from lina.connectivity_and_traffic.sla_operational_state.sla_operational_state import sla_operational_state
from lina.connectivity_and_traffic.traffic.traffic import traffic_dump
from lina.connectivity_and_traffic.perfmon.perfmon import perfmon
from lina.connectivity_and_traffic.service_policy.service_policy import service_policy


def dump_all_conn_and_traffic_data():
    """Gathers output from all conn/traffic commands and writes them to a log file under /var/log/fp_troubleshooting_data."""

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
    log_file = os.path.join(troubleshooting_dir, f"{timestamp}_conn_and_traffic_dump.log")

    try:
        # Gather outputs
        data_to_dump = [
            ("ARP", arp_dump(suppress_output=True)),
            ("Conn Detail", conn_detail_dump(suppress_output=True)),
            ("SLA Config", sla_config(suppress_output=True)),
            ("SLA Operational State", sla_operational_state(suppress_output=True)),
            ("Traffic", traffic_dump(suppress_output=True)),
            ("Perfmon", perfmon(suppress_output=True)),
            ("Service Policy", service_policy(suppress_output=True))
        ]

        # Write all outputs to the log file
        with open(log_file, "w") as f:
            for title, output in data_to_dump:
                f.write(f"{'=' * 80}\n")
                f.write(f"{title}\n")
                f.write(f"{'-' * 80}\n")
                f.write(f"{output}\n")
                f.write(f"{'=' * 80}\n\n")

        print(f"\n[+] All Connectivity and Traffic data written to: {log_file}")

    except Exception as e:
        print(f"[!] Error writing Connectivity and Traffic data to file: {e}")
