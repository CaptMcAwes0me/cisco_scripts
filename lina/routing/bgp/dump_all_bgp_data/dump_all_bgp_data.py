import os
from datetime import datetime
from lina.routing.bgp.bgp_running_config.bgp_running_config import bgp_running_config
from lina.routing.bgp.bgp_summary.bgp_summary import bgp_summary
from lina.routing.bgp.bgp_neighbors.bgp_neighbors import bgp_neighbors
from lina.routing.bgp.bgp_ipv4_unicast.bgp_ipv4_unicast import bgp_ipv4_unicast
from lina.routing.bgp.bgp_cidr_only.bgp_cidr_only import bgp_cidr_only
from lina.routing.bgp.bgp_paths.bgp_paths import bgp_paths
from lina.routing.bgp.bgp_pending_prefixes.bgp_pending_prefixes import bgp_pending_prefixes
from lina.routing.bgp.bgp_rib_failure.bgp_rib_failure import bgp_rib_failure


def dump_all_bgp_data():
    """Gathers output from all BGP commands and writes them to a log file under /var/log/fp_troubleshooting_data."""

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
    log_file = os.path.join(troubleshooting_dir, f"{timestamp}_bgp_dump.log")

    try:
        # Gather outputs
        data_to_dump = [
            ("BGP Running Configuration", bgp_running_config(suppress_output=True)),
            ("BGP Summary", bgp_summary(suppress_output=True)),
            ("BGP Neighbors", bgp_neighbors(suppress_output=True)),
            ("BGP IPv4 Unicast", bgp_ipv4_unicast(suppress_output=True)),
            ("BGP CIDR-Only", bgp_cidr_only(suppress_output=True)),
            ("BGP Paths", bgp_paths(suppress_output=True)),
            ("BGP Pending Prefixes", bgp_pending_prefixes(suppress_output=True)),
            ("BGP RIB Failure", bgp_rib_failure(suppress_output=True)),
        ]

        # Write all outputs to the log file
        with open(log_file, "w") as f:
            for title, output in data_to_dump:
                f.write(f"{'=' * 80}\n")
                f.write(f"{title}\n")
                f.write(f"{'-' * 80}\n")
                f.write(f"{output}\n")
                f.write(f"{'=' * 80}\n\n")

        print(f"\n[+] All BGP data written to: {log_file}")

    except Exception as e:
        print(f"[!] Error writing BGP data to file: {e}")
