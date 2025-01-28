# Description: This script contains the Lina menu and its options.

from core.utils import display_formatted_menu
from firepower.device_information.device_information import device_information
from lina.nat.nat_menu import nat_menu
from lina.access_control.access_control_menu import access_control_menu
from lina.routing.routing_menu import routing_menu
from lina.inspection.inspection_menu import inspection_menu
from lina.vpn.vpn_menu import vpn_menu
from lina.high_availability_failover.high_availability_failover_menu import high_availability_failover_menu
from lina.traffic_analysis_and_logging.traffic_analysis_and_logging_menu import traffic_analysis_and_logging_menu
from lina.clustering.clustering_menu import clustering_menu
from lina.user_authentication_and_aaa.user_authentication_and_aaa_menu import user_authentication_and_aaa_menu


def lina_menu():
    menu_options = {
        "1": ("Device Information", device_information),
        "2": ("NAT (Network Address Translation)", nat_menu),
        "3": ("Access Control (ACLs)", access_control_menu),
        "4": ("Routing", routing_menu),
        "5": ("Inspection Features", inspection_menu),
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
