# Description: This script is used to remove a peer from the Firepower Management Center database using the remove_peer.pl script.

from core.utils import print_warning_box, validate_hex_uuid
import subprocess

def remove_peer():
    """
    Prompt the user for a UUID and execute the remove_peer.pl command.
    """
    warning_message = (
        "WARNING: You are about to remove a peer using the remove_peer.pl script. "
        "This action is irreversible. Ensure you have the correct UUID.\n"
        "If you're unsure, do not proceed with the action."
    )
    print_warning_box(warning_message)

    # Option to return to the previous menu or remove a peer
    while True:
        uuid = input("\nEnter the UUID of the peer to remove (32-character hex value) or enter '0' to exit: ").strip()

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

    # Construct the remove_peer.pl command
    command = f"remove_peer.pl {uuid}"

    print(f"Running command to remove peer with UUID {uuid}...")

    try:
        # Execute the command and capture the output
        result = subprocess.run(
            command,
            shell=True,  # Using shell=True to allow the command to run
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,  # Text mode to automatically decode
            encoding='utf-8',  # UTF-8 encoding
            errors='ignore'  # Ignore characters that can't be decoded
        )

        if result.returncode == 0:
            print(f"Peer with UUID {uuid} successfully removed.")
        else:
            print(f"Error executing command: {result.stderr.strip()}")
    except Exception as e:
        print(f"An error occurred while removing the peer: {e}")

    # Return to the previous menu after removing the peer
    input("\nPress Enter to return to the previous menu...")
    return
