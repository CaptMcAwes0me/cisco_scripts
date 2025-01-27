# Description: This file contains the database troubleshooting menu.

from core.utils import flush_stdin
from firepower.database.em_peers.em_peers import em_peers
from firepower.database.ssl_peers.ssl_peers import ssl_peers
from firepower.database.fail_deployment.fail_deployment import fail_deployment
from firepower.database.delete_notification.delete_notification import delete_notification
from firepower.database.vdb_table.vdb_table import vdb_table
from firepower.database.geodb_table.geodb_table import geodb_table
from firepower.database.notifications_table.notifications_table import notifications_table
from firepower.database.remove_peer.remove_peer import remove_peer


def database_troubleshooting():
    """
    Main menu for database troubleshooting.
    """
    while True:
        flush_stdin()  # Ensure the input buffer is clean

        print("\n" + "=" * 80)
        print(" Database Troubleshooting Menu ".center(80, "="))
        print("=" * 80)
        print("1) Check EM Peers Table")
        print("2) Check SSL Peer Table")
        print("3) Check Notifications Table")
        print("4) Check VDB Table")
        print("5) Check GeoDB Table")
        print("6) Delete Peer from EM Peer Table")
        print("7) Delete Notification")
        print("8) Fail Stuck Deployment")
        print("0) Return to Main Menu")
        print("=" * 80)

        # Prompt the user for their choice
        choice = input("Enter your choice (0-7): ").strip()

        # Process the user's choice
        if choice == '1':
            print("\n" + "-" * 80)
            print("Checking EM Peers Table...".center(80))
            print("-" * 80)
            em_peers()
        elif choice == '2':
            print("\n" + "-" * 80)
            print("Checking SSL Peer Table...".center(80))
            print("-" * 80)
            ssl_peers()
        elif choice == '3':
            print("\n" + "-" * 80)
            print("Checking Notifications Table...".center(80))
            print("-" * 80)
            notifications_table()
        elif choice == '4':
            print("\n" + "-" * 80)
            print("Checking VDB Table...".center(80))
            print("-" * 80)
            vdb_table()
        elif choice == '5':
            print("\n" + "-" * 80)
            print("Checking GeoDB Table...".center(80))
            print("-" * 80)
            geodb_table()
        elif choice == '6':
            print("\n" + "-" * 80)
            print("Delete Peer...".center(80))
            print("-" * 80)
            remove_peer()
        elif choice == '7':
            print("\n" + "-" * 80)
            print("Delete Notification...".center(80))
            print("-" * 80)
            delete_notification()
        elif choice == '8':
            print("\n" + "-" * 80)
            print("Fail Stuck Deployment...".center(80))
            print("-" * 80)
            fail_deployment()
        elif choice == '0':
            print("\nReturning to the main menu...")
            break
        else:
            print("\n[!] Invalid choice. Please enter a number between 0 and 8.")

        flush_stdin()  # Flush input before returning to the menu
