# Description: This script is used to verify the contents of the sftunnel.conf file by printing it.

import subprocess


def sftunnel_conf():
    """
    Verify the contents of the sftunnel.conf file by printing it.
    """
    print("Displaying the contents of /etc/sf/sftunnel.conf...")
    try:
        result = subprocess.run(
            ["cat", "/etc/sf/sftunnel.conf"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        if result.returncode == 0:
            print(result.stdout)  # Print the contents of the sftunnel.conf file
        else:
            print(f"Error reading sftunnel.conf: {result.stderr.strip()}")
    except Exception as e:
        print(f"An error occurred while trying to read sftunnel.conf: {e}")

    # Revert to main menu after checking sftunnel.conf
    input("\nPress Enter to return to the main menu...")
    return
