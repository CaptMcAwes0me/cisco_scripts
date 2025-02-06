# Description: This script provides a menu for accessing Help and About information.

from core.utils import display_formatted_menu


def help_menu():
    print("\nHelp:")
    print("-" * 80)
    print("This script offers a set of troubleshooting and diagnostic tools designed for Cisco Firepower devices.")
    print("Each troubleshooting section includes a 'Help' option, where you can access the relevant commands used to")
    print("gather data for that section. You will also find a brief explanation of each command's purpose and usage.")
    print("Navigate through the available menus to select specific diagnostic options and view detailed information.")
    print("-" * 80)


def about_menu():
    print("\nAbout:")
    print("-" * 80)
    print("This script is developed by Garrett McCollum and Shane Bebber to streamline troubleshooting")
    print("tasks for Cisco Firepower devices.")
    print("-" * 80)
    print("Version: Still building")
    print("-" * 80)
    print("For more information or support, contact gmccollu@cisco.com or shbebber@cisco.com.")
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
