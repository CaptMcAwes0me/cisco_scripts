# Description: This script gathers and displays the output of 'pmtool show affinity'.

import subprocess


def show_cpu_affinity():
    """
    Gathers and displays the output of 'pmtool show affinity'.
    """
    try:
        print("\nGathering CPU affinity information...")
        # Execute the command and capture its output
        result = subprocess.run(["pmtool", "show", "affinity"],
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                text=True)

        # Check if the command executed successfully
        if result.returncode == 0:
            print("\n" + "-" * 80)
            print("CPU Affinity Information:".center(80))
            print("-" * 80)
            print(result.stdout)
        else:
            print("\n[!] Error gathering CPU affinity information:")
            print(result.stderr)
    except FileNotFoundError:
        print("\n[!] 'pmtool' command not found. Please ensure it is installed and accessible.")
    except Exception as e:
        print(f"\n[!] An unexpected error occurred: {e}")
