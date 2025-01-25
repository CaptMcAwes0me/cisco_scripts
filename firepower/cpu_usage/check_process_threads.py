# Description: This script checks the thread information of a given process.

import subprocess


def check_process_threads():
    """
    Prints the thread information of the given process.
    """
    try:
        process_name = input("\nEnter the process name (case sensitive): ").strip()

        # Use 'pidof' to get the PID of the process
        pid_command = f"pidof {process_name}"
        result = subprocess.run(pid_command,
                                shell=True,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                text=True)

        # Check if the command executed successfully
        if result.returncode == 0:
            pid = result.stdout.strip()
            if pid:
                # Execute the pidstat command to get the thread information
                pidstat_command = f"pidstat -h -t -p {pid} 1 1"
                print(f"\nExecuting: {pidstat_command}")

                pidstat_result = subprocess.run(pidstat_command,
                                                shell=True,
                                                stdout=subprocess.PIPE,
                                                stderr=subprocess.PIPE,
                                                text=True)

                if pidstat_result.returncode == 0:
                    # Print the output of the pidstat command
                    print("\n" + "-" * 80)
                    print("pidstat Output:".center(80))
                    print("-" * 80)
                    print(pidstat_result.stdout)
                else:
                    print("\n[!] Error running pidstat command:")
                    print(pidstat_result.stderr)
            else:
                print(f"\n[!] Process '{process_name}' not found.")
        else:
            print(f"\n[!] Error finding process '{process_name}':")
            print(result.stderr)
    except Exception as e:
        print(f"\n[!] An error occurred while checking process threads: {e}")
