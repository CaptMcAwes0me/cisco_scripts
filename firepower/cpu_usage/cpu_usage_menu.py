# Description: CPU usage troubleshooting menu.

from firepower.cpu_usage.show_cpu_affinity import show_cpu_affinity
from firepower.cpu_usage.verify_affected_system_cores import verify_affected_system_cores
from firepower.cpu_usage.gather_processes_on_cores import gather_processes_on_cores
from firepower.cpu_usage.check_process_threads import check_process_threads


def cpu_usage_troubleshooting():
    """
    CPU usage troubleshooting menu.
    """
    while True:
        print("\n" + "=" * 80)
        print(" System CPU Usage Troubleshooting Menu ".center(80, "="))
        print("=" * 80)
        print("1) Show CPU affinity")
        print("2) Verify Affected System Cores")
        print("3) Gather processes on specific cores with high CPU usage")
        print("4) Check if a process is multi-threaded or single-threaded")
        print("0) Return to Main Menu")
        print("=" * 80)

        choice = input("Select an option (0-4): ").strip()

        if choice == "1":
            print("\n" + "-" * 80)
            print("Gathering CPU affinity...".center(80))
            print("-" * 80)
            show_cpu_affinity()
        elif choice == "2":
            print("\n" + "-" * 80)
            print("Gathering Affected CPU Cores...".center(80))
            print("-" * 80)
            verify_affected_system_cores()
        elif choice == "3":
            print("\n" + "-" * 80)
            print("Gathering processes on specific cores with high CPU usage...".center(80))
            print("-" * 80)
            gather_processes_on_cores("10-11")  # Here you can specify the core range or prompt for user input
        elif choice == "4":
            print("\n" + "-" * 80)
            print("Checking process threading...".center(80))
            print("-" * 80)
            check_process_threads()
        elif choice == "0":
            print("\nReturning to Main Menu...")
            break
        else:
            print("\n[!] Invalid option. Please choose a valid option (0-4).")
