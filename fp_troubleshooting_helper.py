# Description: This script is a simple menu-driven program that allows the user to access data dumps.

from core.utils import display_formatted_menu
from menus.troubleshoot_menu import troubleshoot_menu
from menus.data_dump_menu import data_dump_menu
from menus.help_about_menu import help_about_menu


def main_menu():
    menu_options = {
        "1": ("Troubleshooting Menu", troubleshoot_menu),
        "2": ("Data Dump Menu", data_dump_menu),
        "3": ("Help and About", help_about_menu),
        "0": ("Exit123", None),
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


if __name__ == "__main__":
    main_menu()
