# Description: This script is a simple menu-driven program that allows the user to dump various data for Cisco Firepower
# devices.

from lina.nat.dump_all_nat_data.dump_all_nat_data import dump_all_nat_data
from firepower.device_information.device_information import device_information
from menus.routing_dump_menu import routing_dump_menu
from menus.vpn_dump_menu import vpn_dump_menu
from lina.failover.dump_all_failover_data.dump_all_failover_data import dump_all_failover_data
from menus.logging_and_monitoring_dump_menu import logging_and_monitoring_dump_menu
from lina.cluster.dump_all_cluster_data.dump_all_cluster_data import dump_all_cluster_data
from lina.blocks.dump_all_blocks_data.dump_all_blocks_data import dump_all_blocks_data
from lina.connectivity_and_traffic.dump_all_conn_and_traffic_data.dump_all_conn_and_traffic_data \
    import dump_all_conn_and_traffic_data
from core.utils import display_formatted_menu


def data_dump_menu():
    menu_options = {
        "1": ("Device Information", device_information),
        "2": ("NAT (Network Address Translation) Dump", dump_all_nat_data),
        "3": ("Connectivity and Traffic", dump_all_conn_and_traffic_data),
        "4": ("Routing", routing_dump_menu),
        "5": ("VPN", vpn_dump_menu),
        "6": ("High Availability (HA) / Failover", dump_all_failover_data),
        "7": ("Logging and Monitoring", logging_and_monitoring_dump_menu),
        "8": ("Clustering", dump_all_cluster_data),
        "9": ("Block Memory", dump_all_blocks_data),
        "0": ("Exit", None),
    }

    while True:
        # Prepare the menu options for display
        options_display = {key: description for key, (description, _) in menu_options.items()}
        display_formatted_menu("Data Dump Menu", options_display)

        choice = input("Select an option (0-9): ").strip()

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
            print("\n[!] Invalid choice. Please enter a number between 0 and 9.")
