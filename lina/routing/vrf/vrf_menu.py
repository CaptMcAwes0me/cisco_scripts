from core.utils import display_formatted_menu
from lina.routing.vrf.vrf_running_config.vrf_running_config import vrf_running_config
from lina.routing.vrf.vrf.vrf import vrf
from lina.routing.vrf.vrf_counters.vrf_counters import vrf_counters
from lina.routing.vrf.vrf_detail.vrf_detail import vrf_detail
from lina.routing.vrf.vrf_lock.vrf_lock import vrf_lock
from lina.routing.vrf.vrf_tableid.vrf_tableid import vrf_tableid


def vrf_menu():
    menu_options = {
        "1": ("VRF Running Configuration", vrf_running_config),
        "2": ("VRF", vrf),
        "3": ("VRF Counters", vrf_counters),
        "4": ("VRF Detail", vrf_detail),
        "5": ("VRF Lock", vrf_lock),
        "6": ("VRF Table ID", vrf_tableid),
        "0": ("Exit", None),
    }

    while True:
        # Prepare the menu options for display
        options_display = {key: description for key, (description, _) in menu_options.items()}
        display_formatted_menu("VRF Menu", options_display)

        choice = input("Select an option (0-6): ").strip()

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
            print("\n[!] Invalid choice. Please enter a number between 0 and 6.")
