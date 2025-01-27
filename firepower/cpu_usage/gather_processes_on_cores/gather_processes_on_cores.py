# Description: Gather a snapshot of processes and threads running on specific cores with highest CPU usage.

from firepower.cpu_usage.expand_cores.expand_cores import expand_cores
import subprocess


def gather_processes_on_cores(cores):
    """
    Gather a snapshot of processes and threads running on specific cores with highest CPU usage.
    """
    try:
        # Expand the core list if necessary
        expanded_cores = expand_cores(cores)

        # Format the cores into a logical OR list for awk
        core_conditions = " || ".join([f"($10=={core})" for core in expanded_cores])

        # Run the pidstat command to capture CPU usage information for processes and threads
        pidstat_command = f"pidstat -h -t -p ALL 1 1 | awk '($10==\"%CPU\") || ({core_conditions} && $9+0 > 10.00)'"

        # Execute the pidstat command and capture its output
        print(f"\nExecuting: {pidstat_command}")
        result = subprocess.run(pidstat_command,
                                shell=True,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                text=True)

        # Check if the pidstat command executed successfully
        if result.returncode == 0:
            print("\n" + "-" * 80)
            print("Processes and Threads with High CPU Usage on Specific Cores:".center(80))
            print("-" * 80)
            print(result.stdout)
        else:
            print("\n[!] Error gathering process information:")
            print(result.stderr)
    except Exception as e:
        print(f"\n[!] An error occurred while gathering process information: {e}")
