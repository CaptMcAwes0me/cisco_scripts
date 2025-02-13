# Description: This script contains the BGP menu and its associated functions.

from core.utils import display_formatted_menu
from lina.routing.bgp.bgp_running_config.bgp_running_config import bgp_running_config
from lina.routing.bgp.bgp_summary.bgp_summary import bgp_summary
from lina.routing.bgp.bgp_neighbors.bgp_neighbors import bgp_neighbors
from lina.routing.bgp.bgp_ipv4_unicast.bgp_ipv4_unicast import bgp_ipv4_unicast
from lina.routing.bgp.bgp_cidr_only.bgp_cidr_only import bgp_cidr_only
from lina.routing.bgp.bgp_paths.bgp_paths import bgp_paths
from lina.routing.bgp.bgp_pending_prefixes.bgp_pending_prefixes import bgp_pending_prefixes
from lina.routing.bgp.bgp_rib_failure.bgp_rib_failure import bgp_rib_failure
from lina.routing.bgp.bgp_help.bgp_help import bgp_help
from lina.routing.bgp.bgp_advertised_routes.bgp_advertised_routes import bgp_advertised_routes
from lina.routing.bgp.bgp_update_group.bgp_update_group import bgp_update_group


def bgp_menu():
    menu_options = {
        "1": ("BGP Running Configuration", bgp_running_config),
        "2": ("BGP Summary", bgp_summary),
        "3": ("BGP Neighbors", bgp_neighbors),
        "4": ("BGP IPv4 Unicast", bgp_ipv4_unicast),
        "5": ("BGP CIDR-Only", bgp_cidr_only),
        "6": ("BGP Paths", bgp_paths),
        "7": ("BGP Pending Prefixes", bgp_pending_prefixes),
        "8": ("BGP RIB Failure", bgp_rib_failure),
        "9": ("BGP Get Advertised Routes", bgp_advertised_routes),
        "10": ("BGP Update-group", bgp_update_group),
        "11": ("BGP Help", bgp_help),
        "0": ("Exit", None),
    }

    while True:
        # Prepare the menu options for display (excluding "help" shortcuts)
        options_display = {key: description for key, (description, _) in menu_options.items()}
        display_formatted_menu("BGP Menu", options_display)

        choice = input("Select an option (0-11): ").strip().lower()

        # Check if the user entered a valid option with "i" appended (e.g., "2i")
        if choice.endswith("i"):
            base_choice = choice[:-1]  # Remove "i" from input
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
