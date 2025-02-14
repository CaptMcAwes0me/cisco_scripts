# Description: This script contains the routing menu and its corresponding functions.

from menus.global_routing_menu import global_routing_menu
from menus.eigrp_menu import eigrp_menu
from menus.ospf_menu import ospf_menu
from menus.bgp_menu import bgp_menu
from menus.isis_menu import isis_menu
from menus.vrf_menu import vrf_menu
from lina.routing.routing_help.routing_help import routing_help
from core.utils import display_formatted_menu


def routing_menu():
    menu_options = {
        "1": ("Global Routing - Menu", global_routing_menu),
        "2": ("EIGRP - Menu", eigrp_menu),
        "3": ("OSPF - Menu", ospf_menu),
        "4": ("BGP - Menu", bgp_menu),
        "5": ("ISIS - Menu", isis_menu),
        "6": ("VRF - Menu", vrf_menu),
        "7": ("Routing Menu Help", routing_help),
        "0": ("Exit", None),
    }

    while True:
        # Prepare the menu options for display
        options_display = {key: description for key, (description, _) in menu_options.items()}
        display_formatted_menu("Routing Menu", options_display)

        choice = input("Select an option (0-7): ").strip()

        if choice in menu_options:
            description, function = menu_options[choice]

            # Special case: `routing_help` runs directly
            if function == routing_help:
                function()
            if function:  # If a function is assigned
                print("\n" + "-" * 80)
                print(f"Accessing {description}...".center(80))
                print("-" * 80)

                if function == routing_help():
                    function()
                function()  # Call the corresponding function
            else:  # Exit condition
                print("\nExiting to previous menu...")
                break
        else:
            print("\n[!] Invalid choice. Please enter a number between 0 and 7.")
