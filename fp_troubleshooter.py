# Description: This script is a simple menu-driven program that allows the user to access various troubleshooting tools for Cisco Firepower devices.

from firepower.device_information.device_information import device_information
from firepower.firepower_menu import firepower_menu
from lina.lina_menu import lina_menu


def main_menu():
    while True:
        print("\n" + "=" * 80)
        print(" Main Menu ".center(80, "="))
        print("=" * 80)
        print("1) Device Information")
        print("2) Firepower Troubleshooting")
        print("3) Lina Troubleshooting")
        print("0) Exit")
        print("=" * 80)

        # Prompt the user for their choice
        choice = input("Select an option (0-3): ").strip()

        # Process the user's choice
        if choice == "1":
            print("\n" + "-" * 80)
            print("Accessing Device Information...".center(80))
            print("-" * 80)
            device_information()
        elif choice == "2":
            print("\n" + "-" * 80)
            print("Accessing Firepower Menu...".center(80))
            print("-" * 80)
            firepower_menu()
        elif choice == "3":
            print("\n" + "-" * 80)
            print("Accessing Lina Menu...".center(80))
            print("-" * 80)
            lina_menu()
        elif choice == "0":
            print("\nExiting the script. Goodbye!")
            break
        else:
            print("\n[!] Invalid choice. Please enter a number between 0 and 3.")


if __name__ == "__main__":
    main_menu()
