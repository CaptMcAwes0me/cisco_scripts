# Description: This script is used to validate the sftunnel certificate by displaying its details.

import subprocess


def sftunnel_certificate():
    """
    Validate the sftunnel certificate by displaying its details.
    """
    print("Displaying the sftunnel certificate details...")

    try:
        result = subprocess.run(
            ["openssl", "x509", "-text", "-in", "/etc/sf/ca_root/cacert.pem"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        if result.returncode == 0:
            print(result.stdout)  # Print the certificate details
        else:
            print(f"Error reading certificate: {result.stderr.strip()}")
    except Exception as e:
        print(f"An error occurred while trying to read the certificate: {e}")

    # Revert to main menu after checking the certificate
    input("\nPress Enter to return to the main menu...")
    return
