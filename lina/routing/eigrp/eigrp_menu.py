# Description: This script contains the EIGRP menu and its associated functions.

from core.utils import display_formatted_menu
from lina.routing.eigrp.eigrp_events.eigrp_events import eigrp_events
from lina.routing.eigrp.eigrp_interfaces.eigrp_interfaces import eigrp_interfaces
from lina.routing.eigrp.eigrp_neighbors.eigrp_neighbors import eigrp_neighbors
from lina.routing.eigrp.eigrp_topology.eigrp_topology import eigrp_topology
from lina.routing.eigrp.eigrp_traffic.eigrp_traffic import eigrp_traffic
from lina.routing.eigrp.eigrp_routing_table.eigrp_routing_table import eigrp_routing_table
from lina.routing.eigrp.dump_all_eigrp_data.dump_all_eigrp_data import dump_all_eigrp_data


def eigrp_menu():
    menu_options = {
        "1": ("EIGRP Events", eigrp_events),
        "2": ("EIGRP Interfaces", eigrp_interfaces),
        "3": ("EIGRP Neighbors", eigrp_neighbors),
        "4": ("EIGRP Topology", eigrp_topology),
        "5": ("EIGRP Traffic", eigrp_traffic),
        "6": ("EIGRP Routing Table", eigrp_routing_table),
        "7": ("Dump All EIGRP Data", dump_all_eigrp_data),
        "0": ("Exit", None),
    }

    while True:
        # Prepare the menu options for display
        options_display = {key: description for key, (description, _) in menu_options.items()}
        display_formatted_menu("EIGRP Menu", options_display)

        choice = input("Select an option (0-6): ").strip()

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
            print("\n[!] Invalid choice. Please enter a number between 0 and 6.")
