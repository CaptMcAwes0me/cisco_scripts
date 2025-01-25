# Description: This script provides a function to query the notifications table in the Firepower database.

import subprocess

def notifications_table():
    """
    Prompt the user for notification status options and query the database accordingly.
    """
    while True:
        print("\n" + "=" * 80)
        print(" Notification Status Menu ".center(80, "="))
        print("=" * 80)
        print("1) View all notifications")
        print("2) View failed notifications")
        print("3) View running notifications")
        print("0) Return to the previous menu")
        print("=" * 80)

        # Prompt for the user's choice
        choice = input("Enter your choice (1, 2, 3, or 0 to return): ").strip()

        # Handle the user's choice
        if choice == '1':
            query_command = (
                "OmniQuery.pl -db mdb -e "
                "\"SELECT seq, hex(uuid), notification_status.label, notification_status.status, body "
                "FROM notification JOIN notification_status ON notification.status = notification_status.status;\""
            )
            query_desc = "Querying all notifications..."
            break
        elif choice == '2':
            query_command = (
                "OmniQuery.pl -db mdb -e "
                "\"SELECT seq, HEX(uuid), notification_status.label, notification_status.status, body "
                "FROM notification JOIN notification_status ON notification.status = notification_status.status "
                "WHERE notification.status = 13;\""
            )
            query_desc = "Querying failed notifications..."
            break
        elif choice == '3':
            query_command = (
                "OmniQuery.pl -db mdb -e "
                "\"SELECT seq, HEX(uuid), notification_status.label, notification_status.status, body "
                "FROM notification JOIN notification_status ON notification.status = notification_status.status "
                "WHERE notification.status = 7;\""
            )
            query_desc = "Querying running notifications..."
            break
        elif choice == '0':
            print("\nReturning to the previous menu...")
            return  # Exit the function to return to the previous menu
        else:
            print("\n[!] Invalid choice. Please enter 1, 2, 3, or 0.")
            continue

    # Display the query being run
    print("\n" + "-" * 80)
    print(query_desc.center(80))
    print("-" * 80)

    try:
        # Execute the OmniQuery command and capture the output
        result = subprocess.run(
            query_command,
            shell=True,  # Using shell=True to allow multi-part commands
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,  # Text mode to automatically decode
            encoding='utf-8',  # Try UTF-8 encoding
            errors='ignore'  # Ignore characters that can't be decoded
        )

        if result.returncode == 0:
            output = result.stdout.strip()
            if output:
                print("\nQuery result:")
                print(output)
            else:
                print("\n[!] No results found.")
        else:
            print(f"\n[!] Error executing query: {result.stderr.strip()}")
    except Exception as e:
        print(f"\n[!] An error occurred while querying the notifications table: {e}")

    # Revert to main menu after querying the notifications table
    print("\n" + "=" * 80)
    input("Press Enter to return to the main menu...")
    return
