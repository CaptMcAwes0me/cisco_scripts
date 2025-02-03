# Description: This script contains the nat menu and its corresponding functions.

from lina.nat.nat_running_config.nat_running_config import nat_running_config
from lina.nat.nat_detail.nat_detail import nat_detail
from lina.nat.xlate_count.xlate_count import xlate_count
from lina.nat.xlate_detail.xlate_detail import xlate_detail_interactive
from lina.nat.nat_proxy_arp.nat_proxy_arp import nat_proxy_arp
from lina.nat.nat_pool.nat_pool import nat_pool
from core.utils import display_formatted_menu


def nat_menu():
    menu_options = {
        "1": ("NAT Running Config", nat_running_config),
        "2": ("NAT Detail Table", nat_detail),
        "3": ("NAT Proxy-ARP Table", nat_proxy_arp),
        "4": ("NAT Pool", nat_pool),
        "5": ("Xlate Count", xlate_count),
        "6": ("Xlate Detail", xlate_detail_interactive),
        "0": ("Exit", None),
    }

    while True:
        # Prepare the menu options for display
        options_display = {key: description for key, (description, _) in menu_options.items()}
        display_formatted_menu("NAT Menu", options_display)

        choice = input("Select an option (0-6): ").strip()

        if choice in menu_options:
            description, function = menu_options[choice]
            if function:  # If a function is assigned
                print("\n" + "-" * 80)
                print(f"Accessing {description}...".center(80))
                print("-" * 80)
                function()  # Call the corresponding function
            else:  # Exit condition
                print("\nExiting the script. Goodbye!")
                break
        else:
            print("\n[!] Invalid choice. Please enter a number between 0 and 6.")
