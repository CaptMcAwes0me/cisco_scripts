# Description: This script is used to validate the EM_peers database table by querying the database for peer information.

import subprocess
from core.utils import validate_uuid

def em_peers():
    """
    Validate a database table by querying the database for peer information.
    """
    print("\n" + "=" * 80)
    print(" Peer Database Validation ".center(80, "="))
    print("=" * 80)
    print("You can either:")
    print("  1. Enter a peer's UUID to query specific peer information.")
    print("  2. Leave the input blank to query all peer data.")
    print("  3. Enter '0' to return to the previous menu.")
    print("\nNote: The peer's UUID can be found by running the 'show version' command on the peer device.")
    print("=" * 80)

    # Prompt the user to enter the UUID of the peer
    while True:
        uuid = input("\nEnter the peer's UUID (or leave blank to query all peers, or enter '0' to exit): ").strip()

        # Exit back to the menu if the user enters '0'
        if uuid == '0':
            print("\nReturning to the previous menu...")
            return

        # If UUID is not empty, validate its format
        if uuid and not validate_uuid(uuid):
            print("\n[!] Invalid UUID format. Please enter a valid UUID (32 characters, uppercase hex).")
            continue  # Prompt again if UUID is invalid

        break  # Exit the loop once a valid UUID, blank entry, or '0' is provided

    # Construct the OmniQuery command based on whether the UUID is provided
    if uuid:
        query_command = f"OmniQuery.pl -db mdb -e \"select name, ip, uuid, sw_version, role, reg_state from EM_peers where uuid = '{uuid}';\""
        query_desc = f"Querying data for UUID: {uuid}"
    else:
        query_command = "OmniQuery.pl -db mdb -e \"select name, ip, uuid, sw_version, role, reg_state from EM_peers;\""
        query_desc = "Querying data for all peers"

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
            text=True
        )

        if result.returncode == 0:
            output = result.stdout.strip()
            if output:
                print("\nQuery result:")
                print(output)
            else:
                print("\n[!] No results found for the specified UUID or for all peers.")
        else:
            print(f"\n[!] Error executing query: {result.stderr.strip()}")
    except Exception as e:
        print(f"\n[!] An error occurred while querying the database: {e}")

    # Revert to main menu after validating the database table
    print("\n" + "=" * 80)
    input("Press Enter to return to the main menu...")
    return