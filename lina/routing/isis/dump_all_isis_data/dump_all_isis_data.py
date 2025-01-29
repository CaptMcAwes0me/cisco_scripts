import os
from datetime import datetime
from core.utils import isis_running_config, isis_database, isis_hostname, isis_lsp_log, isis_neighbors, isis_rib, isis_spf_log, isis_topology

def dump_all_isis_data():
    """Gathers output from all ISIS commands and writes them to a log file under /var/log/fp_troubleshooting_data."""

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
    log_file = os.path.join(troubleshooting_dir, f"{timestamp}_isis_dump.log")

    try:
        # Gather outputs
        data_to_dump = [
            ("ISIS Running Config", isis_running_config(suppress_output=True)),
            ("ISIS Database", isis_database(suppress_output=True)),
            ("ISIS Hostname", isis_hostname(suppress_output=True)),
            ("ISIS LSP Log", isis_lsp_log(suppress_output=True)),
            ("ISIS Neighbors", isis_neighbors(suppress_output=True)),
            ("ISIS RIB", isis_rib(suppress_output=True)),
            ("ISIS SPF Log", isis_spf_log(suppress_output=True)),
            ("ISIS Topology", isis_topology(suppress_output=True)),
        ]

        # Write all outputs to the log file
        with open(log_file, "w") as f:
            for title, output in data_to_dump:
                f.write(f"{'=' * 80}\n")
                f.write(f"{title}\n")
                f.write(f"{'-' * 80}\n")
                f.write(f"{output}\n")
                f.write(f"{'=' * 80}\n\n")

        print(f"\n[+] All ISIS data written to: {log_file}")

    except Exception as e:
        print(f"[!] Error writing ISIS data to file: {e}")

