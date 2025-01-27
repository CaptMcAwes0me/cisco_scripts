# Description: This script contains the Lina menu and its options.

from core.utils import display_formatted_menu
from firepower.device_information.device_information import device_information


def lina_menu():
    menu_options = {
        "1": ("Device Information", device_information),
        "2": ("NAT (Network Address Translation)", registration_troubleshooting),
        "3": ("Access Control (ACLs)", database_troubleshooting),
        "4": ("Inspection Features", disk_usage_troubleshooting),
        "5": ("VPN", cpu_usage_troubleshooting),
        "6": ("High Availability (HA) / Failover", database_troubleshooting),
        "7": ("Traffic Analysis and Logging", disk_usage_troubleshooting),
        "8": ("Clustering", cpu_usage_troubleshooting),
        "9": ("User Authentication and AAA", cpu_usage_troubleshooting),
        "0": ("Exit", None),
    }

    while True:
        # Prepare the menu options for display
        options_display = {key: description for key, (description, _) in menu_options.items()}
        display_formatted_menu("Lina Menu", options_display)

        choice = input("Select an option (0-9): ").strip()

        if choice in menu_options:
            description, function = menu_options[choice]
            if function:  # If a function is assigned
                print("\n" + "-" * 80)
                print(f"Accessing {description}...".center(80))
                print("-" * 80)
                function()
            else:  # Exit condition
                print("\nExiting the script. Goodbye!")
                break
        else:
            print("\n[!] Invalid choice. Please enter a number between 0 and 9.")
