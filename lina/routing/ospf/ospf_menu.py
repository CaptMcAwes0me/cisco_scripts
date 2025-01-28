# Description: This script contains the OSPF menu and its associated functions.

from core.utils import display_formatted_menu
from lina.routing.ospf.ospf_running_config.ospf_running_config import ospf_running_config
from lina.routing.ospf.ospf_all.ospf_all import ospf_all
from lina.routing.ospf.ospf_border_routers.ospf_border_routers import ospf_border_routers
from lina.routing.ospf.ospf_database.ospf_database import ospf_database
from lina.routing.ospf.ospf_events.ospf_events import ospf_events
from lina.routing.ospf.ospf_interface.ospf_interface import ospf_interface
from lina.routing.ospf.ospf_neighbor.ospf_neighbor import ospf_neighbor
from lina.routing.ospf.ospf_nsf.ospf_nsf import ospf_nsf
from lina.routing.ospf.ospf_rib.ospf_rib import ospf_rib
from lina.routing.ospf.ospf_statistics.ospf_statistics import ospf_statistics
from lina.routing.ospf.ospf_traffic.ospf_traffic import ospf_traffic
from lina.routing.ospf.dump_all_ospf_data.dump_all_ospf_data import dump_all_ospf_data


def ospf_menu():
    menu_options = {
        "1": ("OSPF Running Configuration", ospf_running_config),
        "2": ("OSPF All", ospf_all),
        "3": ("OSPF Border Routers", ospf_border_routers),
        "4": ("OSPF Database", ospf_database),
        "5": ("OSPF Events", ospf_events),
        "6": ("OSPF Interface", ospf_interface),
        "7": ("OSPF Neighbor", ospf_neighbor),
        "8": ("OSPF NSF", ospf_nsf),
        "9": ("OSPF RIB", ospf_rib),
        "10": ("OSPF Statistics", ospf_statistics),
        "11": ("OSPF Traffic", ospf_traffic),
        "12": ("Dump All OSPF Data", dump_all_ospf_data),
        "0": ("Exit", None),
    }

    while True:
        # Prepare the menu options for display
        options_display = {key: description for key, (description, _) in menu_options.items()}
        display_formatted_menu("OSPF Menu", options_display)

        choice = input("Select an option (0-12): ").strip()

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
            print("\n[!] Invalid choice. Please enter a number between 0 and 12.")
