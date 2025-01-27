# Description: This file contains the disk usage troubleshooting menu.

from firepower.disk_usage.display_disk_usage.display_disk_usage import display_disk_usage
from firepower.disk_usage.find_large_files.find_large_files import find_large_files
from firepower.disk_usage.gather_deleted_files.gather_deleted_files import gather_deleted_files_info
from core.utils import display_formatted_menu


def disk_usage_troubleshooting():
    # Map menu options to descriptions and their respective functions
    menu_options = {
        "1": ("Display disk usage (df -TH)", display_disk_usage),
        "2": ("Find large files", find_large_files),
        "3": ("Gather deleted file information", gather_deleted_files_info),
        "0": ("Return to Main Menu", None),
    }

    while True:
        # Create a dictionary for menu display
        options_display = {key: description for key, (description, _) in menu_options.items()}
        display_formatted_menu("Disk Usage Troubleshooting Menu", options_display)

        choice = input("Select an option: ").strip()

        if choice in menu_options:
            description, function = menu_options[choice]
            if function:  # If a function is assigned
                print("\n" + "-" * 80)
                print(f"{description}...".center(80))
                print("-" * 80)
                function()
            else:  # Return to main menu condition
                print("\nReturning to the firepower menu...")
                break
        else:
            print("\n[!] Invalid choice. Please enter a valid option.")
