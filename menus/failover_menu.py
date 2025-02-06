from lina.failover.failover_app_sync_stats import failover_app_sync_stats
from lina.failover.failover_details import failover_details
from lina.failover.failover_state import failover_state
from lina.failover.failover_config_sync_status import failover_config_sync_status
from lina.failover.failover_interface import failover_interface
from lina.failover.failover import failover
from lina.failover.failover_descriptor import failover_descriptor
from lina.failover.failover_running_config import failover_running_config
from core.utils import display_formatted_menu


def failover_menu():
    """Displays a menu for selecting failover-related commands and executes the corresponding function."""

    menu_options = {
        "1": ("Failover Application Sync Stats", failover_app_sync_stats),
        "2": ("Failover Details", failover_details),
        "3": ("Failover State", failover_state),
        "4": ("Failover Config Sync Status", failover_config_sync_status),
        "5": ("Failover Interface", failover_interface),
        "6": ("Failover", failover),
        "7": ("Failover Descriptor", failover_descriptor),
        "8": ("Failover Running Config", failover_running_config),
        "0": ("Exit", None),
    }

    while True:
        # Prepare the menu options for display
        options_display = {key: description for key, (description, _) in menu_options.items()}
        display_formatted_menu("Failover Menu", options_display)

        choice = input("Select an option (0-8): ").strip()

        if choice in menu_options:
            description, function = menu_options[choice]
            if function:  # If a function is assigned
                print("\n" + "-" * 80)
                print(f"Accessing {description}...".center(80))
                print("-" * 80)
                function()
            else:  # Exit condition
                print("\nReturning to the previous menu...")
                break
        else:
            print("\n[!] Invalid choice. Please enter a number between 0 and 8.")
