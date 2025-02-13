# Description: This script contains the ISIS menu options and functions to access the ISIS data.

from core.utils import display_formatted_menu
from lina.routing.isis.isis_database.isis_database import isis_database
from lina.routing.isis.isis_hostname.isis_hostname import isis_hostname
from lina.routing.isis.isis_lsp_log.isis_lsp_log import isis_lsp_log
from lina.routing.isis.isis_neighbors.isis_neighbors import isis_neighbors
from lina.routing.isis.isis_rib.isis_rib import isis_rib
from lina.routing.isis.isis_spf_log.isis_spf_log import isis_spf_log
from lina.routing.isis.isis_topology.isis_topology import isis_topology
from lina.routing.isis.isis_help.isis_help import isis_help
from lina.routing.isis.isis_running_config.isis_running_config import isis_running_config


def isis_menu():
    menu_options = {
        "1": ("ISIS Running Configuration", isis_running_config),
        "2": ("ISIS Database", isis_database),
        "3": ("ISIS Hostname", isis_hostname),
        "4": ("ISIS LSP Log", isis_lsp_log),
        "5": ("ISIS Neighbors", isis_neighbors),
        "6": ("ISIS RIB", isis_rib),
        "7": ("ISIS SPF Log", isis_spf_log),
        "8": ("ISIS Topology", isis_topology),
        "9": ("ISIS Help", isis_help),
        "0": ("Exit", None),
    }

    while True:
        # Prepare the menu options for display (excluding hidden help shortcuts)
        options_display = {key: description for key, (description, _) in menu_options.items()}
        display_formatted_menu("ISIS Menu", options_display)

        choice = input("Select an option (0-9): ").strip().lower()

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
