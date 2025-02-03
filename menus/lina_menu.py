# Description: This script contains the Lina menu and its options.

from core.utils import display_formatted_menu
from firepower.device_information.device_information import device_information
from menus.nat_menu import nat_menu
from menus.connectivity_and_traffic_menu import connectivity_and_traffic_menu
from menus.routing_menu import routing_menu
from menus.inspection_menu import inspection_menu
from menus.vpn_menu import vpn_menu
from menus.high_availability_failover_menu import high_availability_failover_menu
from menus.logging_menu import logging_menu
from menus.cluster_menu import cluster_menu
from menus.block_memory_menu import block_memory_menu


def lina_menu():
    menu_options = {
        "1": ("Device Information", device_information),
        "2": ("NAT (Network Address Translation)", nat_menu),
        "3": ("Connectivity and Traffic", connectivity_and_traffic_menu),
        "4": ("Routing", routing_menu),
        "5": ("Inspection Features", inspection_menu),
        "6": ("VPN", vpn_menu),
        "7": ("High Availability (HA) / Failover", high_availability_failover_menu),
        "8": ("Logging", logging_menu),
        "9": ("Clustering", cluster_menu),
        "10": ("Block Memory", block_memory_menu),
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
                print("\nExiting to previous menu...")
                break
        else:
            print("\n[!] Invalid choice. Please enter a number between 0 and 10.")
