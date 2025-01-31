# Description: This script contains the nat menu and its corresponding functions.

from lina.nat.nat_running_config import nat_running_config
from lina.nat.nat_detail import nat_detail
from lina.nat.xlate_count import xlate_count
from lina.nat.xlate_detail import xlate_detail
from lina.nat.dump_all_nat_data import dump_all_nat_data
from core.utils import display_formatted_menu


def nat_menu():
    menu_options = {
        "1": ("NAT Running Config", nat_running_config),
        "2": ("NAT Detail Table", nat_detail),
        "3": ("Xlate Count", xlate_count),
        "4": ("Xlate Detail", xlate_detail),
        "5": ("Dump All NAT Data", dump_all_nat_data),
        "0": ("Exit", None),
    }

    while True:
        # Prepare the menu options for display
        options_display = {key: description for key, (description, _) in menu_options.items()}
        display_formatted_menu("NAT Menu", options_display)

        choice = input("Select an option (0-5): ").strip()

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
            print("\n[!] Invalid choice. Please enter a number between 0 and 5.")
