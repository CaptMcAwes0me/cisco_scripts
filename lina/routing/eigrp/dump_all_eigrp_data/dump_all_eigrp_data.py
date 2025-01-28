# Description: This script collects all EIGRP-related outputs and writes them to a log file.

from datetime import datetime
from lina.routing.eigrp.eigrp_events.eigrp_events import eigrp_events
from lina.routing.eigrp.eigrp_interfaces.eigrp_interfaces import eigrp_interfaces
from lina.routing.eigrp.eigrp_neighbors.eigrp_neighbors import eigrp_neighbors
from lina.routing.eigrp.eigrp_topology.eigrp_topology import eigrp_topology
from lina.routing.eigrp.eigrp_traffic.eigrp_traffic import eigrp_traffic
from lina.routing.eigrp.eigrp_routing_table.eigrp_routing_table import eigrp_routing_table


def dump_all_eigrp_data():
    """Gathers output from all EIGRP commands and writes them to a log file."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = f"/var/log/{timestamp}_eigrp_dump.log"

    try:
        # Gather outputs
        data_to_dump = []
        data_to_dump.append(("EIGRP Events", eigrp_events()))
        data_to_dump.append(("EIGRP Interfaces", eigrp_interfaces()))
        data_to_dump.append(("EIGRP Neighbors", eigrp_neighbors()))
        data_to_dump.append(("EIGRP Topology", eigrp_topology()))
        data_to_dump.append(("EIGRP Traffic", eigrp_traffic()))
        data_to_dump.append(("EIGRP Routing Table", eigrp_routing_table()))

        # Write all outputs to the file
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
