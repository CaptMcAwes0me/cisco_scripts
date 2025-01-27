# Description: Functions to delete a notification from the database.

from core.utils import print_warning_box, validate_hex_uuid
import subprocess

def delete_notification():
    """
    Prompt the user for a UUID and delete the notification with the corresponding UUID from the database.
    """
    warning_message = (
        "WARNING: Deleting a notification will permanently remove it from the system.\n"
        "WARNING: DO NOT delete deployment notifications. If you need to fail a stuck deployment, please select option 7 from the previous menu."
    )
    print_warning_box(warning_message)

    # Option to return to the previous menu
    while True:
        uuid = input("\nEnter the UUID of the notification to delete (32-character hex value) or enter '0' to return to the previous menu: ").strip()

        if uuid == '0':
            print("Returning to the previous menu...")
            return  # Exit and return to the previous menu

        # Validate the UUID format
        if not uuid:
            print("UUID cannot be empty.")
            continue  # Prompt again if UUID is empty
        elif not validate_hex_uuid(uuid):
            print("Invalid UUID format. Please enter a valid 32-character hex UUID (uppercase).")
            continue  # Prompt again if UUID is invalid

        break  # Exit the loop once a valid UUID is provided

    # Construct the OmniQuery command to delete the notification
    query_command = f"OmniQuery.pl -db mdb -e \"DELETE FROM notification WHERE uuid=unhex('{uuid}');\""

    print(f"Running query to delete notification with UUID {uuid}...")

    try:
        # Execute the OmniQuery command and capture the output
        result = subprocess.run(
            query_command,
            shell=True,  # Using shell=True to allow multi-part commands
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,  # Text mode to automatically decode
            encoding='utf-8',  # UTF-8 encoding
            errors='ignore'  # Ignore characters that can't be decoded
        )

        if result.returncode == 0:
            print(f"Notification with UUID {uuid} successfully deleted.")
        else:
            print(f"Error executing query: {result.stderr.strip()}")
    except Exception as e:
        print(f"An error occurred while deleting the notification: {e}")

    # Return to the previous menu after deleting the notification
    input("\nPress Enter to return to the previous menu...")
    return