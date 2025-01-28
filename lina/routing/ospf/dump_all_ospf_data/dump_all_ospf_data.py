import os
from datetime import datetime
from lina.routing.ospf.ospf_running_config import ospf_running_config
from lina.routing.ospf.ospf_all import ospf_all
from lina.routing.ospf.ospf_border_routers import ospf_border_routers
from lina.routing.ospf.ospf_database import ospf_database
from lina.routing.ospf.ospf_events import ospf_events
from lina.routing.ospf.ospf_interface import ospf_interface
from lina.routing.ospf.ospf_neighbor import ospf_neighbor
from lina.routing.ospf.ospf_nsf import ospf_nsf
from lina.routing.ospf.ospf_rib import ospf_rib
from lina.routing.ospf.ospf_statistics import ospf_statistics
from lina.routing.ospf.ospf_traffic import ospf_traffic


def dump_all_ospf_data():
    """Gathers output from all OSPF commands and writes them to a log file under /var/log/fp_troubleshooting_data."""

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
    log_file = os.path.join(troubleshooting_dir, f"{timestamp}_ospf_dump.log")

    try:
        # Gather outputs
        data_to_dump = [
            ("OSPF Running Configuration", ospf_running_config(suppress_output=True)),
            ("OSPF All", ospf_all(suppress_output=True)),
            ("OSPF Border Routers", ospf_border_routers(suppress_output=True)),
            ("OSPF Database", ospf_database(suppress_output=True)),
            ("OSPF Events", ospf_events(suppress_output=True)),
            ("OSPF Interface", ospf_interface(suppress_output=True)),
            ("OSPF Neighbor", ospf_neighbor(suppress_output=True)),
            ("OSPF NSF", ospf_nsf(suppress_output=True)),
            ("OSPF RIB", ospf_rib(suppress_output=True)),
            ("OSPF Statistics", ospf_statistics(suppress_output=True)),
            ("OSPF Traffic", ospf_traffic(suppress_output=True)),
        ]

        # Write all outputs to the log file
        with open(log_file, "w") as f:
            for title, output in data_to_dump:
                f.write(f"{'=' * 80}\n")
                f.write(f"{title}\n")
                f.write(f"{'-' * 80}\n")
                f.write(f"{output}\n")
                f.write(f"{'=' * 80}\n\n")

        print(f"\n[+] All OSPF data written to: {log_file}")

    except Exception as e:
        print(f"[!] Error writing OSPF data to file: {e}")

