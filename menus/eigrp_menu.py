# Description: This script contains the EIGRP menu and its associated functions.

from core.utils import display_formatted_menu
from lina.routing.eigrp.eigrp_events.eigrp_events import eigrp_events
from lina.routing.eigrp.eigrp_interfaces.eigrp_interfaces import eigrp_interfaces
from lina.routing.eigrp.eigrp_neighbors.eigrp_neighbors import eigrp_neighbors
from lina.routing.eigrp.eigrp_topology.eigrp_topology import eigrp_topology
from lina.routing.eigrp.eigrp_traffic.eigrp_traffic import eigrp_traffic
from lina.routing.eigrp.eigrp_routing_table.eigrp_routing_table import eigrp_routing_table
from lina.routing.eigrp.eigrp_help.eigrp_help import eigrp_help
from lina.routing.eigrp.eigrp_running_config.eigrp_running_config import eigrp_running_config


def eigrp_menu():
    menu_options = {
        "1": ("EIGRP Running Configuration", eigrp_running_config),
        "2": ("EIGRP Events", eigrp_events),
        "3": ("EIGRP Interfaces", eigrp_interfaces),
        "4": ("EIGRP Neighbors", eigrp_neighbors),
        "5": ("EIGRP Topology", eigrp_topology),
        "6": ("EIGRP Traffic", eigrp_traffic),
        "7": ("EIGRP Routing Table", eigrp_routing_table),
        "8": ("EIGRP Help", eigrp_help),
        "0": ("Exit", None),
    }

    while True:
        # Prepare the menu options for display (excluding hidden help shortcuts)
        options_display = {key: description for key, (description, _) in menu_options.items()}
        display_formatted_menu("EIGRP Menu", options_display)

        choice = input("Select an option (0-8): ").strip().lower()

        # Check if the user entered a valid option with "?" appended (e.g., "2?")
        if choice.endswith("?"):
            base_choice = choice[:-1]  # Remove "?" from input
            if base_choice in menu_options:
                description, function = menu_options[base_choice]
                if function:
                    print("\n" + "-" * 80)
                    print(f"Help for: {description}".center(80))
                    print("-" * 80)
                    function(help_requested=True)  # Call function in help mode
                else:
                    print("\n[!] Help not available for this option.")
            else:
                print("\n[!] Invalid choice. Please enter a valid number from the menu.")

        elif choice in menu_options:
            description, function = menu_options[choice]
            if function:
                print("\n" + "-" * 80)
                print(f"Accessing {description}...".center(80))
                print("-" * 80)
                function()  # Normal function execution
            else:  # Exit condition
                print("\nExiting to previous menu...")
                break
        else:
            print("\n[!] Invalid choice. Please enter a valid number from the menu.")
