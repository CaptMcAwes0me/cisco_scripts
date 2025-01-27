# Description: This script is used to search logs based on the UUID and IP address and output to a file.

from core.utils import validate_uuid, validate_ip
import time
import subprocess


def grep_logs():
    """
    Search logs based on the UUID and IP address and output to a file.
    """
    print("\n" + "=" * 80)
    print(" Search Logs Based on UUID and IP Address ".center(80, "="))
    print("=" * 80)
    print("\nYou will need to provide the UUID and IP address of the peer to search the logs.")
    print("Enter 0 at any prompt to return to the previous menu.")

    # Prompt for the UUID of the peer
    while True:
        uuid = input("Enter the UUID of the peer (or 0 to return to the previous menu): ").strip()
        if uuid == '0':
            return  # Escape to the previous menu
        if not uuid:
            print("\n[!] UUID cannot be empty. Please enter a valid UUID.")
            continue
        elif not validate_uuid(uuid):
            print("\n[!] Invalid UUID format. Please enter a valid UUID.")
            continue
        break  # Exit the loop once a valid UUID is provided

    # Prompt for the IP address of the peer
    while True:
        ip_address = input("Enter the IP address of the peer (or 0 to return to the previous menu): ").strip()
        if ip_address == '0':
            return  # Escape to the previous menu
        if not ip_address:
            print("\n[!] IP address cannot be empty. Please enter a valid IP address.")
            continue
        elif not validate_ip(ip_address):
            print("\n[!] Invalid IP address format. Please enter a valid IP address.")
            continue
        break  # Exit the loop once a valid IP address is provided

    print(f"\nGathering logs for UUID: {uuid}, IP Address: {ip_address}...")

    # Define output file name with timestamp
    output_file = f'{time.strftime("%Y%m%d_%H%M%S")}_filtered_logs.txt'

    try:
        # Construct the grep command to search for the UUID and IP address in the logs
        grep_command = f'grep -E "{uuid}|{ip_address}|sftunneld" /var/log/messages > {output_file}'

        # Run the grep command to search logs and write to the output file
        subprocess.run(grep_command, shell=True, check=True)

        print(f"\n[+] Logs have been successfully saved to {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"\n[!] Error occurred while gathering logs: {e}")
    except Exception as e:
        print(f"\n[!] An unexpected error occurred: {e}")

    # Return to main menu after completing log gathering
    input("\nPress Enter to return to the main menu...")
    return
