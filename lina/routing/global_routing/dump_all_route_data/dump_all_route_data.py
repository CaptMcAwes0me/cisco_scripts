import os
from datetime import datetime
from lina.routing.global_routing.running_config_all.running_config_all import running_config_all
from lina.routing.global_routing.show_route_all.show_route_all import show_route_all
from lina.routing.global_routing.asp_table_routing_all.asp_table_routing_all import asp_table_routing_all


def dump_all_route_data():
    """Gathers output from all Route-related commands and writes them to a log file under
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
    log_file = os.path.join(troubleshooting_dir, f"{timestamp}_route_dump.log")

    try:
        # Gather outputs
        data_to_dump = [
            ("Route Running Configuration", running_config_all(suppress_output=True, config_type="route")),
            ("Router Running Configuration", running_config_all(suppress_output=True, config_type="router")),
            ("Show Route All", show_route_all(suppress_output=True)),
            ("ASP Table Routing All", asp_table_routing_all(suppress_output=True)),
        ]

        # Write all outputs to the log file
        with open(log_file, "w") as f:
            for title, output in data_to_dump:
                f.write(f"{'=' * 80}\n")
                f.write(f"{title}\n")
                f.write(f"{'-' * 80}\n")
                f.write(f"{output}\n")
                f.write(f"{'=' * 80}\n\n")

        print(f"\n[+] All Route data written to: {log_file}")

    except Exception as e:
        print(f"[!] Error writing Route data to file: {e}")
