# Description: This script is a simple menu-driven program that allows the user to dump various data for Cisco Firepower
# devices.

from lina.nat.dump_all_nat_data.dump_all_nat_data import dump_all_nat_data
from firepower.device_information.device_information import device_information
from menus.routing_dump_menu import routing_dump_menu
from menus.inspection_menu import inspection_menu
from menus.vpn_menu import vpn_menu
from menus.high_availability_failover_menu import high_availability_failover_menu
from menus.traffic_analysis_and_logging_menu import traffic_analysis_and_logging_menu
from menus.clustering_menu import clustering_menu
from menus.user_authentication_and_aaa_menu import user_authentication_and_aaa_menu
from menus.access_control_menu import access_control_menu
from core.utils import display_formatted_menu


def data_dump_menu():
    menu_options = {
        "1": ("Device Information", device_information),
        "2": ("NAT (Network Address Translation) Dump", dump_all_nat_data),
        "3": ("Access Control (ACLs)", access_control_menu),  # still working on this
        "4": ("Routing", routing_dump_menu),
        "5": ("Inspection Features", inspection_menu),  # still working on this
        "6": ("VPN", vpn_menu),  # still working on this
        "7": ("High Availability (HA) / Failover", high_availability_failover_menu),  # still working on this
        "8": ("Traffic Analysis and Logging", traffic_analysis_and_logging_menu),  # still working on this
        "9": ("Clustering", clustering_menu),  # still working on this
        "10": ("User Authentication and AAA", user_authentication_and_aaa_menu),  # still working on this
        "0": ("Exit", None),
    }

    while True:
        # Prepare the menu options for display
        options_display = {key: description for key, (description, _) in menu_options.items()}
        display_formatted_menu("Data Dump Menu", options_display)

        choice = input("Select an option (0-3): ").strip()

        if choice in menu_options:
            description, function = menu_options[choice]
            if function:  # If a function is assigned
                print("\n" + "-" * 80)
                print(f"Accessing {description}...".center(80))
                print("-" * 80)
                function()
            else:  # Exit condition
                print("\nExiting back to the Main Menu...")
                break
        else:
            print("\n[!] Invalid choice. Please enter a number between 0 and 3.")
