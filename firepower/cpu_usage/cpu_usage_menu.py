# Description: CPU usage troubleshooting menu.

from firepower.cpu_usage.show_cpu_affinity.show_cpu_affinity import show_cpu_affinity
from firepower.cpu_usage.verify_affected_system_cores.verify_affected_system_cores import verify_affected_system_cores
from firepower.cpu_usage.gather_processes_on_cores.gather_processes_on_cores import gather_processes_on_cores
from firepower.cpu_usage.check_process_threads.check_process_threads import check_process_threads
from core.utils import display_formatted_menu
from firepower.cpu_usage.extract_sys_cores import extract_sys_cores


def cpu_usage_troubleshooting():
    # Extract the system cores before proceeding with the menu
    system_cores = extract_sys_cores()
    if system_cores is None:
        print(system_cores)
        print("\n[!] Cannot proceed without extracting system core information. Exiting.")
        return  # Exit the function if the cores couldn't be gathered

    # Map menu options to descriptions and their respective functions
    menu_options = {
        "1": ("Show CPU affinity", show_cpu_affinity),
        "2": ("Verify Affected System Cores", verify_affected_system_cores),
        "3": ("Gather processes on specific cores with high CPU usage", gather_processes_on_cores),
        "4": ("Check if a process is multi-threaded or single-threaded", check_process_threads),
        "0": ("Return to Main Menu", None),
    }

    while True:
        # Create a dictionary for menu display
        options_display = {key: description for key, (description, _) in menu_options.items()}
        display_formatted_menu("System CPU Usage Troubleshooting Menu", options_display)

        choice = input("Select an option (0-4): ").strip()

        if choice in menu_options:
            description, function = menu_options[choice]
            if function:  # If a function is assigned
                print("\n" + "-" * 80)
                print(f"Accessing {description}...".center(80))
                print("-" * 80)

                # If the function requires system cores (e.g., gather_processes_on_cores)
                if function == gather_processes_on_cores:
                    function(system_cores)  # Pass the system cores to the function
                else:
                    function()  # Call the function normally
            else:  # Return to the main menu
                print("\nReturning to Main Menu...")
                break
        else:
            print("\n[!] Invalid choice. Please enter a valid option (0-4).")
