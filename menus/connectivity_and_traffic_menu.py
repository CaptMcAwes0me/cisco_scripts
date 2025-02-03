# Description: This script contains the Cluster menu and its associated functions.

from core.utils import display_formatted_menu
from lina.connectivity_and_traffic.arp.arp import arp
from lina.connectivity_and_traffic.conn_detail.conn_detail import conn_detail
from lina.connectivity_and_traffic.sla_config.sla_config import sla_config
from lina.connectivity_and_traffic.sla_operational_state.sla_operational_state import sla_operational_state
from lina.connectivity_and_traffic.traffic.traffic import traffic


def connectivity_and_traffic_menu():
    menu_options = {
        "1": ("ARP Table", arp),
        "2": ("Conn Detail Table", conn_detail),
        "3": ("SLA Configuration", sla_config),
        "4": ("SLA Operational-State", sla_operational_state),
        "5": ("Traffic", traffic),
        "0": ("Exit", None),
    }

    while True:
        # Prepare the menu options for display
        options_display = {key: description for key, (description, _) in menu_options.items()}
        display_formatted_menu("Cluster Menu", options_display)

        choice = input("Select an option (0-5): ").strip()

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
            print("\n[!] Invalid choice. Please enter a number between 0 and 5.")
