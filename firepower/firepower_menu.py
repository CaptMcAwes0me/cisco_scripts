# Description: This script is the main menu for the Firepower troubleshooting section. It allows the user to access various troubleshooting tools for Cisco Firepower devices.

from firepower.registration.registration_menu import registration_troubleshooting
from firepower.device_information.device_information import device_information
from firepower.database.database_menu import database_troubleshooting
from firepower.disk_usage.disk_usage_menu import disk_usage_troubleshooting
from firepower.cpu_usage.cpu_usage_menu import cpu_usage_troubleshooting


def firepower_menu():
    while True:
        print("\n" + "=" * 80)
        print(" Firepower Menu ".center(80, "="))
        print("=" * 80)
        print("1) Device Information")
        print("2) Registration Troubleshooting")
        print("3) Database Troubleshooting")
        print("4) Disk Usage Troubleshooting")
        print("5) System CPU Troubleshooting (FTD Only)")
        print("0) Exit")
        print("=" * 80)

        # Prompt the user for their choice
        choice = input("Select an option (0-5): ").strip()

        # Process the user's choice
        if choice == "1":
            print("\n" + "-" * 80)
            print("Accessing Device Information...".center(80))
            print("-" * 80)
            device_information()
        elif choice == "2":
            print("\n" + "-" * 80)
            print("Accessing Registration Troubleshooting...".center(80))
            print("-" * 80)
            registration_troubleshooting()
        elif choice == "3":
            print("\n" + "-" * 80)
            print("Accessing Database Troubleshooting...".center(80))
            print("-" * 80)
            database_troubleshooting()
        elif choice == "4":
            print("\n" + "-" * 80)
            print("Accessing Disk Usage Troubleshooting...".center(80))
            print("-" * 80)
            disk_usage_troubleshooting()
        elif choice == "5":
            print("\n" + "-" * 80)
            print("Accessing System CPU Usage Troubleshooting...".center(80))
            print("-" * 80)
            cpu_usage_troubleshooting()
        elif choice == "0":
            print("\nExiting the script. Goodbye!")
            break
        else:
            print("\n[!] Invalid choice. Please enter a number between 0 and 5.")
