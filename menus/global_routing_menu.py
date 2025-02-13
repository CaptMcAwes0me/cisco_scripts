# Description: This script contains the Global Routing menu and its associated functions.

from core.utils import display_formatted_menu
from lina.routing.global_routing.show_route_all.show_route_all import show_route_all
from lina.routing.global_routing.asp_table_routing_all.asp_table_routing_all import asp_table_routing_all
from lina.routing.global_routing.global_routing_help.global_routing_help import global_routing_help
from lina.routing.global_routing.running_config_all.running_config_all import running_config_all


def global_routing_menu():
    menu_options = {
        "1": ("Route Running Configuration",
              lambda help_requested=False: running_config_all(suppress_output=False, config_type="route",
                                                              help_requested=help_requested)),
        "2": ("Router Running Configuration",
              lambda help_requested=False: running_config_all(suppress_output=False, config_type="router",
                                                              help_requested=help_requested)),
        "3": ("Show Route All", show_route_all),
        "4": ("ASP Table Routing All", asp_table_routing_all),
        "5": ("Global Routing Help", global_routing_help),
        "0": ("Exit", None),
    }

    while True:
        # Prepare the menu options for display (excluding hidden help shortcuts)
        options_display = {key: description for key, (description, _) in menu_options.items()}
        display_formatted_menu("Global Routing Menu", options_display)

        choice = input("Select an option (0-5): ").strip().lower()

        # Check if the user entered a valid option with "?" appended (e.g., "3?")
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
