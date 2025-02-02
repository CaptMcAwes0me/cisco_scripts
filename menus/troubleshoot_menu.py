# Description: This script is a simple menu-driven program that allows the user to access various troubleshooting tools
# for Cisco Firepower devices.

from firepower.device_information.device_information import device_information
from firepower.firepower_menu import firepower_menu
from menus.lina_menu import lina_menu
from core.utils import display_formatted_menu


def troubleshoot_menu():
    menu_options = {
        "1": ("Device Information", device_information),
        "2": ("Firepower Troubleshooting", firepower_menu),
        "3": ("Lina Troubleshooting", lina_menu),
        "0": ("Exit", None),
    }

    while True:
        # Prepare the menu options for display
        options_display = {key: description for key, (description, _) in menu_options.items()}
        display_formatted_menu("Main Menu", options_display)

        choice = input("Select an option (0-3): ").strip()

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
            print("\n[!] Invalid choice. Please enter a number between 0 and 3.")
