# Description: This script collects all EIGRP-related outputs and writes them to a log file.

import os
from datetime import datetime
from lina.routing.eigrp.eigrp_events.eigrp_events import eigrp_events
from lina.routing.eigrp.eigrp_interfaces.eigrp_interfaces import eigrp_interfaces
from lina.routing.eigrp.eigrp_neighbors.eigrp_neighbors import eigrp_neighbors
from lina.routing.eigrp.eigrp_topology.eigrp_topology import eigrp_topology
from lina.routing.eigrp.eigrp_traffic.eigrp_traffic import eigrp_traffic
from lina.routing.eigrp.eigrp_routing_table.eigrp_routing_table import eigrp_routing_table


def dump_all_eigrp_data():
    """Gathers output from all EIGRP commands and writes them to a log file under /var/log/fp_troubleshooting_data."""

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
    log_file = os.path.join(troubleshooting_dir, f"{timestamp}_eigrp_dump.log")

    try:
        # Gather outputs
        data_to_dump = [
            ("EIGRP Events", eigrp_events(suppress_output=True)),
            ("EIGRP Interfaces", eigrp_interfaces(suppress_output=True)),
            ("EIGRP Neighbors", eigrp_neighbors(suppress_output=True)),
            ("EIGRP Topology", eigrp_topology(suppress_output=True)),
            ("EIGRP Traffic", eigrp_traffic(suppress_output=True)),
            ("EIGRP Routing Table", eigrp_routing_table(suppress_output=True)),
        ]

        # Write all outputs to the log file
        with open(log_file, "w") as f:
            for title, output in data_to_dump:
                f.write(f"{'=' * 80}\n")
                f.write(f"{title}\n")
                f.write(f"{'-' * 80}\n")
                f.write(f"{output}\n")
                f.write(f"{'=' * 80}\n\n")

        print(f"\n[+] All EIGRP data written to: {log_file}")

    except Exception as e:
        print(f"[!] Error writing EIGRP data to file: {e}")

