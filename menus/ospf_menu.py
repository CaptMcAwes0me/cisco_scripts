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
from lina.routing.ospf.ospf_help.ospf_help import ospf_help


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
        "12": ("OSPF Help", ospf_help),
        "0": ("Exit", None),
    }

    while True:
        # Prepare the menu options for display (excluding hidden help shortcuts)
        options_display = {key: description for key, (description, _) in menu_options.items()}
        display_formatted_menu("OSPF Menu", options_display)

        choice = input("Select an option (0-12): ").strip().lower()

        # Check if the user entered a valid option with "?" appended (e.g., "5?")
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
