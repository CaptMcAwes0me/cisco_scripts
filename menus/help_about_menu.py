# Description: This script provides a menu for accessing Help and About information.

from core.utils import display_formatted_menu


def help_menu():
    print("\nHelp:")
    print("-" * 80)
    print("This script provides various troubleshooting and diagnostic tools for Cisco Firepower devices.")
    print("Use the available menus to access specific troubleshooting options and data dumps.")
    print("-" * 80)


def about_menu():
    print("\nAbout:")
    print("-" * 80)
    print("This script is developed by [Your Name] to streamline troubleshooting tasks for Cisco Firepower devices.")
    print("Version: 1.0")
    print("For more information or support, contact [Your Email].")
    print("-" * 80)


def help_about_menu():
    menu_options = {
        "1": ("Help", help_menu),
        "2": ("About", about_menu),
        "0": ("Back to Main Menu", None),
    }

    while True:
        # Prepare the menu options for display
        options_display = {key: description for key, (description, _) in menu_options.items()}
        display_formatted_menu("Help and About Menu", options_display)

        choice = input("Select an option (0-2): ").strip()

        if choice in menu_options:
            description, function = menu_options[choice]
            if function:  # If a function is assigned
                print("\n" + "-" * 80)
                print(f"Accessing {description}...".center(80))
                print("-" * 80)
                function()
            else:  # Back to Main Menu condition
                break
        else:
            print("\n[!] Invalid choice. Please enter a number between 0 and 2.")
