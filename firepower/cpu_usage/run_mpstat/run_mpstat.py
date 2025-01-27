# Description: This script runs the 'mpstat' command with the given core list.

import subprocess
from firepower.cpu_usage.expand_cores.expand_cores import expand_cores


def run_mpstat(cores):
    """
    Runs the 'mpstat' command with the given core list.
    """
    try:
        # Expand the core list if necessary
        expanded_cores = expand_cores(cores)

        # Format the cores into a comma-separated list for mpstat
        core_list = ','.join(map(str, expanded_cores))

        # Create the mpstat command
        mpstat_command = f"mpstat -P {core_list} 1 1"

        # Execute the mpstat command and capture its output
        print(f"\nExecuting: {mpstat_command}")
        result = subprocess.run(mpstat_command,
                                shell=True,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                text=True)

        # Check if the mpstat command executed successfully
        if result.returncode == 0:
            print("\n" + "-" * 80)
            print("mpstat Output:".center(80))
            print("-" * 80)
            print(result.stdout)
        else:
            print("\n[!] Error running mpstat command:")
            print(result.stderr)
    except Exception as e:
        print(f"\n[!] An error occurred while executing mpstat: {e}")
