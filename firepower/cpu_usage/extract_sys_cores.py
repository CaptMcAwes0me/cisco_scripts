# Description: This script is used to extract the system cores from the 'show_cpu_affinity' command output.

import subprocess
from expand_cores import expand_cores


def extract_sys_cores():
    """
    Extract system cores from 'show_cpu_affinity' and return them as a list.
    """
    try:
        # Execute 'show_cpu_affinity' to gather the system cores
        result = subprocess.run(["pmtool", "show", "affinity"],
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                text=True)

        # Check if the command executed successfully
        if result.returncode == 0:
            # Look for the "System CPU Affinity" line and extract the core range
            sys_cores_line = next((line for line in result.stdout.splitlines() if "System CPU Affinity" in line), None)
            if sys_cores_line:
                # Extract the core range from the line
                core_range = sys_cores_line.split(":")[1].strip().split(" ")[0]
                return expand_cores(core_range)  # Use the existing expand_cores to handle ranges
            else:
                print("\n[!] Could not find system core information in the output.")
                return None
        else:
            print("\n[!] Error gathering CPU affinity information:")
            print(result.stderr)
            return None
    except Exception as e:
        print(f"\n[!] An error occurred while extracting system cores: {e}")
        return None
