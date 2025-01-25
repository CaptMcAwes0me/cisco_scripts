# Description: This script allows the user to fail a deployment notification by setting the status to 'failed' (status=13).

from core.utils import print_warning_box, validate_hex_uuid
import subprocess

def fail_deployment():
    """
    Prompt the user for a UUID and set the status of the notification to 'failed' (status=13).
    """
    warning_message = (
        "WARNING: You are about to fail a deployment notification. Make sure you have the correct UUID.\n"
        "If you're unsure, do not proceed with the action."
    )
    print_warning_box(warning_message)

    # Option to return to the previous menu or fail a deployment
    while True:
        uuid = input("\nEnter the UUID of the notification to fail (32-character hex value) or enter '0' to exit: ").strip()

        if uuid == '0':
            print("Exiting without making changes...")
            return  # Exit without making changes

        # Validate the UUID format
        if not uuid:
            print("UUID cannot be empty.")
            continue  # Prompt again if UUID is empty
        elif not validate_hex_uuid(uuid):
            print("Invalid UUID format. Please enter a valid 32-character hex UUID (uppercase).")
            continue  # Prompt again if UUID is invalid

        break  # Exit the loop once a valid UUID is provided

    # Construct the OmniQuery command to fail the deployment
    query_command = f"OmniQuery.pl -db mdb -e \"update notification set status=13 where uuid=unhex('{uuid}');\""

    print(f"Running query to fail deployment for notification with UUID {uuid}...")

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
            print(f"Deployment with UUID {uuid} successfully marked as failed.")
        else:
            print(f"Error executing query: {result.stderr.strip()}")
    except Exception as e:
        print(f"An error occurred while failing the deployment: {e}")

    # Return to the previous menu after failing the deployment
    input("\nPress Enter to return to the previous menu...")
    return