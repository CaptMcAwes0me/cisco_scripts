# Description: This file contains the disk usage troubleshooting menu.

from firepower.disk_usage.display_disk_usage.display_disk_usage import display_disk_usage
from firepower.disk_usage.find_large_files.find_large_files import find_large_files
from firepower.disk_usage.gather_deleted_files.gather_deleted_files import gather_deleted_files_info


def disk_usage_troubleshooting():
    """
    Disk usage troubleshooting menu.
    """
    while True:
        print("\n" + "=" * 80)
        print(" Disk Usage Troubleshooting Menu ".center(80, "="))
        print("=" * 80)
        print("1) Display disk usage (df -TH)")
        print("2) Find large files")
        print("3) Gather deleted file information")
        print("0) Return to Main Menu")
        print("=" * 80)

        choice = input("Select an option (0-3): ").strip()

        if choice == "1":
            print("\n" + "-" * 80)
            print("Displaying disk usage...".center(80))
            print("-" * 80)
            display_disk_usage()
        elif choice == "2":
            print("\n" + "-" * 80)
            print("Finding large files...".center(80))
            print("-" * 80)
            find_large_files()
        elif choice == "3":
            print("\n" + "-" * 80)
            print("Gathering deleted file information...".center(80))
            print("-" * 80)
            gather_deleted_files_info()
        elif choice == "0":
            print("\nReturning to the main menu...")
            break
        else:
            print("\n[!] Invalid choice. Please enter a number between 0 and 3.")
