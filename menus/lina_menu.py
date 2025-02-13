# Description: This script contains the Lina menu and its options.

from core.utils import display_formatted_menu
from lina.show_version.show_version import show_version
from menus.nat_menu import nat_menu
from menus.connectivity_and_traffic_menu import connectivity_and_traffic_menu
from menus.routing_menu import routing_menu
from menus.vpn_menu import vpn_menu
from menus.failover_menu import failover_menu
from menus.logging_and_monitoring_menu import logging_and_monitoring_menu
from menus.cluster_menu import cluster_menu
from menus.blocks_menu import blocks_menu
from menus.lina_menu_help.lina_menu_help import lina_menu_help


def lina_menu():
    menu_options = {
        "1": ("System Version", show_version),
        "2": ("NAT (Network Address Translation) Menu", nat_menu),
        "3": ("Routing Menu", routing_menu),
        "4": ("VPN Menu", vpn_menu),
        "5": ("Connectivity and Traffic Menu", connectivity_and_traffic_menu),
        "6": ("High Availability (HA) / Failover Menu", failover_menu),
        "7": ("Logging and Monitoring Menu", logging_and_monitoring_menu),
        "8": ("Clustering Menu", cluster_menu),
        "9": ("Block Memory Menu", blocks_menu),
        "10": ("Lina Menu Help", lina_menu_help),
        "0": ("Exit", None),
    }

    while True:
        # Prepare the menu options for display
        options_display = {key: description for key, (description, _) in menu_options.items()}
        display_formatted_menu("Lina Menu", options_display)

        choice = input("Select an option (0-10): ").strip()

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
