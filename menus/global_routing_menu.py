# Description: This script contains the Global menu and its associated functions.

from core.utils import display_formatted_menu
from lina.routing.global_routing.show_route_all.show_route_all import show_route_all
from lina.routing.global_routing.asp_table_routing_all.asp_table_routing_all import asp_table_routing_all
from lina.routing.global_routing.global_routing_help.global_routing_help import global_routing_help
from lina.routing.global_routing.running_config_all.running_config_all import running_config_all


def global_routing_menu():
    menu_options = {
        "1": ("Route Running Configuration", lambda: running_config_all(suppress_output=False, config_type="route")),
        "2": ("Router Running Configuration", lambda: running_config_all(suppress_output=False, config_type="router")),
        "3": ("Show Route All", show_route_all),
        "4": ("ASP Table Routing All", asp_table_routing_all),
        "5": ("Global Routing Help", global_routing_help),
        "0": ("Exit", None),
    }

    while True:
        # Prepare the menu options for display
        options_display = {key: description for key, (description, _) in menu_options.items()}
        display_formatted_menu("Global Routing Menu", options_display)

        choice = input("Select an option (0-5): ").strip()

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
            print("\n[!] Invalid choice. Please enter a number between 0 and 5.")
