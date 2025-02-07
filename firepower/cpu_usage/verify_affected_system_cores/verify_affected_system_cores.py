# Description: This script is used to verify the affected system cores using 'pmtool show affinity' and runs 'mpstat' for those cores.

import re
import subprocess
from firepower.cpu_usage.run_mpstat.run_mpstat import run_mpstat


def verify_affected_system_cores():
    """
    Gathers and verifies the affected system cores using 'pmtool show affinity' and runs 'mpstat' for those cores.
    """
    try:
        # Execute the command to gather system core information
        result = subprocess.run(["pmtool", "show", "affinity"],
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                text=True)

        # Check if the command executed successfully
        if result.returncode == 0:
            output = result.stdout

            # Extract the line with "System CPU Affinity"
            system_affinity_match = re.search(r"System CPU Affinity:\s([\d,-]+)", output)
            if system_affinity_match:
                system_cores = system_affinity_match.group(1)
                print("\n" + "-" * 80)
                print("System CPU Cores Used:".center(80))
                print("-" * 80)
                print(f"Cores: {system_cores}")

                # Call the mpstat function with the system cores
                run_mpstat(system_cores)
            else:
                print("\n[!] Unable to parse 'System CPU Affinity' from the output.")
        else:
            print("\n[!] Error gathering CPU affinity information:")
            print(result.stderr)
    except FileNotFoundError:
        print("\n[!] 'pmtool' command not found. Please ensure it is installed and accessible.")
    except Exception as e:
        print(f"\n[!] An unexpected error occurred: {e}")
