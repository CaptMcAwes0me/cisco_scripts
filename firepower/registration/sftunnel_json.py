# Description: Contains utility functions used by the other modules.

import subprocess


def sftunnel_json():
    """
    Verify the contents of the sftunnel.json file by prompting for the peer's UUID.
    """
    print("\n" + "=" * 80)
    print(" Verify sftunnel.json File ".center(80, "="))
    print("=" * 80)
    print("\nTo verify the sftunnel.json file, you need to provide the peer's UUID.")
    print("The peer's UUID can be found by running the 'show version' command on the peer device.")
    print("=" * 80)

    # Prompt the user to enter the UUID of the peer
    uuid = input("Enter the peer's UUID (or press 0 to return): ").strip()

    if uuid == '0':
        print("\nReturning to the previous menu...")
        return  # Return to the previous menu if UUID is '0'

    if not uuid:
        print("\n[!] UUID cannot be empty. Please enter a valid UUID.")
        input("\nPress Enter to return to the main menu...")
        return  # Return to the main menu if UUID is not provided

    # Construct the path to the sftunnel.json file
    json_path = f"/var/sf/peers/{uuid}/sftunnel.json"

    print(f"\nDisplaying the contents of {json_path}...\n")

    try:
        # Run the cat command to read the sftunnel.json file
        result = subprocess.run(
            ["cat", json_path],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        if result.returncode == 0:
            print(result.stdout)  # Print the contents of the sftunnel.json file
        else:
            print(f"\n[!] Error reading {json_path}: {result.stderr.strip()}")
    except Exception as e:
        print(f"\n[!] An error occurred while trying to read {json_path}: {e}")

    # Revert to main menu after checking sftunnel.json
    input("\nPress Enter to return to the main menu...")
    return
