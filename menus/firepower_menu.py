# Description: This script is the main menu for the Firepower troubleshooting section.
# It allows the user to access various troubleshooting tools for Cisco Firepower devices.

from firepower.registration.registration_menu import registration_menu
from firepower.device_information.device_information import device_information
from firepower.database.database_menu import database_menu
from firepower.disk_usage.disk_usage_menu import disk_usage_menu
from firepower.cpu_usage.cpu_usage_menu import cpu_usage_menu
from firepower.firepower_menu_help.firepower_menu_help import firepower_menu_help
from core.utils import display_formatted_menu


def firepower_menu():
    # Map menu options to descriptions and their respective functions
    menu_options = {
        "1": ("Device Information", device_information),
        "2": ("Registration Troubleshooting", registration_menu),
        "3": ("Database Troubleshooting", database_menu),
        "4": ("Disk Usage Troubleshooting", disk_usage_menu),
        "5": ("System CPU Troubleshooting", cpu_usage_menu),
        "6": ("Firepower Menu Help", firepower_menu_help),
        "0": ("Exit", None),
    }

    while True:
        # Create a dictionary for menu display
        options_display = {key: description for key, (description, _) in menu_options.items()}
        display_formatted_menu("Firepower Menu", options_display)

        choice = input("Select an option (0-6): ").strip()

        if choice in menu_options:
            description, function = menu_options[choice]
            if function:  # If a function is assigned
                print("\n" + "-" * 80)
                print(f"Accessing {description}...".center(80))
                print("-" * 80)
                function()
            else:  # Exit condition
                print("\nExiting to previous menu...")
                break
        else:
            print("\n[!] Invalid choice. Please enter a number between 0 and 6.")
