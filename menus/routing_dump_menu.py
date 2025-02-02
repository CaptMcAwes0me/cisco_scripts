# Description: This script contains the routing menu and its corresponding functions.

from lina.routing.global_routing.dump_all_route_data import dump_all_route_data
from lina.routing.eigrp.dump_all_eigrp_data import dump_all_eigrp_data
from lina.routing.ospf.dump_all_ospf_data import dump_all_ospf_data
from lina.routing.bgp.dump_all_bgp_data import dump_all_bgp_data
from lina.routing.isis.dump_all_isis_data import dump_all_isis_data
from lina.routing.vrf.dump_all_vrf_data import dump_all_vrf_data
from core.utils import display_formatted_menu


def routing_dump_menu():
    menu_options = {
        "1": ("Dump Global Routing Data", dump_all_route_data),
        "2": ("Dump EIGRP Data", dump_all_eigrp_data),
        "3": ("Dump OSPF Data", dump_all_ospf_data),
        "4": ("Dump BGP Data", dump_all_bgp_data),
        "5": ("Dump ISIS Data", dump_all_isis_data),
        "6": ("Dump VRF Data", dump_all_vrf_data),
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
