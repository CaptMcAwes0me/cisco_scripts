# Description: This script contains the Lina menu and its options.

from core.utils import display_formatted_menu
from firepower.device_information.device_information import device_information


def lina_menu():
    menu_options = {
        "1": ("Device Information", device_information),
        "2": ("NAT (Network Address Translation)", nat_menu),
        "3": ("Access Control (ACLs)", access_control_menu),
        "4": ("Routing", routing_menu),
        "5": ("Inspection Features", inspection_features_menu),
        "6": ("VPN", vpn_menu),
        "7": ("High Availability (HA) / Failover", high_availability_failover_menu),
        "8": ("Traffic Analysis and Logging", traffic_analysis_and_logging_menu),
        "9": ("Clustering", clustering_menu),
        "10": ("User Authentication and AAA", user_authentication_and_aaa_menu),
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
            print("\n[!] Invalid choice. Please enter a number between 0 and 10.")
