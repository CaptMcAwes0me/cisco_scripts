# Description: This script contains the VRF menu and its associated functions.

from core.utils import display_formatted_menu
from lina.routing.vrf.vrf_running_config.vrf_running_config import vrf_running_config
from lina.routing.vrf.vrf.vrf import vrf
from lina.routing.vrf.vrf_counters.vrf_counters import vrf_counters
from lina.routing.vrf.vrf_detail.vrf_detail import vrf_detail
from lina.routing.vrf.vrf_lock.vrf_lock import vrf_lock
from lina.routing.vrf.vrf_tableid.vrf_tableid import vrf_tableid
from lina.routing.vrf.vrf_help.vrf_help import vrf_help


def vrf_menu():
    menu_options = {
        "1": ("VRF Running Configuration", vrf_running_config),
        "2": ("VRF", vrf),
        "3": ("VRF Counters", vrf_counters),
        "4": ("VRF Detail", vrf_detail),
        "5": ("VRF Lock", vrf_lock),
        "6": ("VRF Table ID", vrf_tableid),
        "7": ("VRF Help", vrf_help),
        "0": ("Exit", None),
    }

    while True:
        # Prepare the menu options for display (excluding hidden help shortcuts)
        options_display = {key: description for key, (description, _) in menu_options.items()}
        display_formatted_menu("VRF Menu", options_display)

        choice = input("Select an option (0-7): ").strip().lower()

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
