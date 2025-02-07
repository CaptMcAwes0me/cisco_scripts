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
from core.utils import display_formatted_menu

def database_menu():
    # Map menu options to descriptions and their respective functions
    menu_options = {
        "1": ("Check EM Peers Table", em_peers),
        "2": ("Check SSL Peer Table", ssl_peers),
        "3": ("Check Notifications Table", notifications_table),
        "4": ("Check VDB Table", vdb_table),
        "5": ("Check GeoDB Table", geodb_table),
        "6": ("Delete Peer from EM Peer Table", remove_peer),
        "7": ("Delete Notification", delete_notification),
        "8": ("Fail Stuck Deployment", fail_deployment),
        "0": ("Return to Main Menu", None),
    }

    while True:
        # Create a dictionary for menu display
        options_display = {key: description for key, (description, _) in menu_options.items()}
        display_formatted_menu("Database Troubleshooting Menu", options_display)

        choice = input("Select an option: ").strip()

        if choice in menu_options:
            description, function = menu_options[choice]
            if function:  # If a function is assigned
                print("\n" + "-" * 80)
                print(f"{description}...".center(80))
                print("-" * 80)
                function()
            else:  # Return to main menu condition
                print("\nReturning to the main menu...")
                break
        else:
            print("\n[!] Invalid choice. Please enter a valid option.")
