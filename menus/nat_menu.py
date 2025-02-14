# Description: This script contains the NAT menu and its corresponding functions.

from lina.nat.nat_running_config.nat_running_config import nat_running_config
from lina.nat.nat_detail.nat_detail import nat_detail
from lina.nat.xlate_count.xlate_count import xlate_count
from lina.nat.xlate_detail.xlate_detail import xlate_detail_interactive
from lina.nat.nat_proxy_arp.nat_proxy_arp import nat_proxy_arp
from lina.nat.nat_pool.nat_pool import nat_pool
from lina.nat.nat_help.nat_help import nat_help
from core.utils import display_formatted_menu


def nat_menu():
    menu_options = {
        "1": ("NAT Running Config", nat_running_config),
        "2": ("NAT Detail Table", nat_detail),
        "3": ("NAT Proxy-ARP Table", nat_proxy_arp),
        "4": ("NAT Pool", nat_pool),
        "5": ("Xlate Count", xlate_count),
        "6": ("Xlate Detail", xlate_detail_interactive),
        "7": ("NAT Help", nat_help),
        "0": ("Exit", None),
    }

    while True:
        # Prepare the menu options for display (excluding hidden help shortcuts)
        options_display = {key: description for key, (description, _) in menu_options.items()}
        display_formatted_menu("NAT Menu", options_display)

        choice = input("Select an option (0-7): ").strip().lower()

        # Check if the user entered a valid option with "?" appended (e.g., "2?")
        if choice.endswith("?"):
            base_choice = choice[:-1]  # Remove "?" from input
            if base_choice in menu_options:
                description, function = menu_options[base_choice]

                # Special case: `nat_help` runs directly
                if function == nat_help:
                    function()
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
