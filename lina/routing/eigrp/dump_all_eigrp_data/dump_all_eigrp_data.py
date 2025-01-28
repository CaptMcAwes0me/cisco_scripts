# Description: This script collects all EIGRP-related outputs and writes them to a log file.

from datetime import datetime
from lina.routing.eigrp.eigrp_events.eigrp_events import eigrp_events
from lina.routing.eigrp.eigrp_interfaces.eigrp_interfaces import eigrp_interfaces
from lina.routing.eigrp.eigrp_neighbors.eigrp_neighbors import eigrp_neighbors
from lina.routing.eigrp.eigrp_topology.eigrp_topology import eigrp_topology
from lina.routing.eigrp.eigrp_traffic.eigrp_traffic import eigrp_traffic
from lina.routing.eigrp.eigrp_routing_table.eigrp_routing_table import eigrp_routing_table


def dump_all_eigrp_data():
    """Collects all EIGRP-related outputs and writes them to a log file."""
    try:
        # Gather outputs from each function
        events_output = eigrp_events()
        interfaces_output = eigrp_interfaces()
        neighbors_output = eigrp_neighbors()
        topology_output = eigrp_topology()
        traffic_output = eigrp_traffic()
        routing_table_output = eigrp_routing_table()

        # Prepare log file name with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        log_file_path = f"/var/log/{timestamp}_eigrp_dump.log"

        # Write all outputs to the log file
        with open(log_file_path, "w") as log_file:
            log_file.write("EIGRP Events:\n")
            log_file.write(events_output + "\n\n")

            log_file.write("EIGRP Interfaces:\n")
            log_file.write(interfaces_output + "\n\n")

            log_file.write("EIGRP Neighbors:\n")
            log_file.write(neighbors_output + "\n\n")

            log_file.write("EIGRP Topology:\n")
            log_file.write(topology_output + "\n\n")

            log_file.write("EIGRP Traffic:\n")
            log_file.write(traffic_output + "\n\n")

            log_file.write("EIGRP Routing Table:\n")
            log_file.write(routing_table_output + "\n\n")

        print(f"[+] All EIGRP data has been written to {log_file_path}")

    except Exception as e:
        print(f"[!] Error while dumping EIGRP data: {e}")
