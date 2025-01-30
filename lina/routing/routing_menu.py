# Description: This script contains the routing menu and its corresponding functions.

from lina.routing.global_routing.global_routing_menu import global_routing_menu
from lina.routing.eigrp.eigrp_menu import eigrp_menu
from lina.routing.ospf.ospf_menu import ospf_menu
from lina.routing.bgp.bgp_menu import bgp_menu
from lina.routing.isis.isis_menu import isis_menu
from lina.routing.vrf.vrf_menu import vrf_menu
from core.utils import display_formatted_menu


def routing_menu():
    menu_options = {
        "1": ("Global Routing", global_routing_menu),
        "2": ("EIGRP", eigrp_menu),
        "3": ("OSPF", ospf_menu),
        "4": ("BGP", bgp_menu),
        "5": ("ISIS", isis_menu),
        "6": ("VRF", vrf_menu),
        "0": ("Exit", None),
    }

    while True:
        # Prepare the menu options for display
        options_display = {key: description for key, (description, _) in menu_options.items()}
        display_formatted_menu("Routing Menu", options_display)

        choice = input("Select an option (0-6): ").strip()

        if choice in menu_options:
            description, function = menu_options[choice]
            if function:  # If a function is assigned
                print("\n" + "-" * 80)
                print(f"Accessing {description}...".center(80))
                print("-" * 80)
                function()  # Call the corresponding function
            else:  # Exit condition
                print("\nExiting the script. Goodbye!")
                break
        else:
            print("\n[!] Invalid choice. Please enter a number between 0 and 7.")
