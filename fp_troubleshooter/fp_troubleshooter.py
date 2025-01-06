#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: Garrett McCollum
Date: 2025-01-06
Description:

    This script performs various network-related tasks, including verifying connectivity,
    running bandwidth tests, checking configuration files, validating certificates, checking database
    values and gathering logs.

    The script interacts with the user through a simple text-based menu, where the user
    can choose from various options for network testing, configuration verification, and
    log analysis.

    Version: 1.0.0
"""

import socket
import subprocess
import time
import threading
import sys
import os
import signal
import select
import termios
import tty
import re

def flush_stdin():
    """
    Flush stdin to clear any leftover input.
    """
    try:
        termios.tcflush(sys.stdin, termios.TCIFLUSH)
    except:
        pass  # Ignore if flushing fails (e.g., on non-Unix systems)

def validate_uuid(uuid):
    """
    Validates if the given UUID matches the standard UUID format.
    """
    uuid_pattern = re.compile(r'^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$', re.IGNORECASE)
    return bool(uuid_pattern.match(uuid))

def validate_ip(ip_address):
    """
    Validates if the given IP address is in the correct IPv4 format.
    """
    ip_pattern = re.compile(r'^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$')
    return bool(ip_pattern.match(ip_address))

def validate_hex_uuid(uuid):
    """
    Validate the format of the UUID (all uppercase, 32 hex characters).
    """
    uuid_pattern = re.compile(r'^[A-F0-9]{32}$')
    return bool(uuid_pattern.match(uuid))

def print_warning_box(message):
    """
    Prints the given message inside a more proportionate box for emphasis.
    """
    lines = message.split('\n')
    longest_line = max(len(line) for line in lines)
    border = "*" * (longest_line + 4)  # Adjust the width based on the longest line

    print(border)
    for line in lines:
        print(f"* {line.ljust(longest_line)} *")
    print(border)

# Path to the configuration file
config_file_path = "/etc/sf/ims.conf"

# Fields to extract
fields_to_extract = ["SWVERSION", "SWBUILD", "MODEL", "APPLIANCE_UUID"]

def parse_config(file_path, keys_to_extract):
    """Parses the configuration file and returns specified key-value pairs."""
    config_data = {}
    try:
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                # Skip empty lines or comments
                if not line or line.startswith("#"):
                    continue
                if "=" in line:
                    key, value = line.split("=", 1)
                    key, value = key.strip(), value.strip()
                    if key in keys_to_extract:
                        config_data[key] = value
    except FileNotFoundError:
        print(f"Error: Configuration file '{file_path}' not found.")
    except Exception as e:
        print(f"Error reading configuration file: {e}")
    return config_data

def display_table(data):
    """Displays the configuration data in a prettier table format."""
    # Calculate column widths for alignment
    field_width = max(len(key) for key in data.keys()) + 2
    value_width = max(len(value) for value in data.values()) + 2
    
    # Top border
    table_width = field_width + value_width + 7
    print("+" + "-" * (table_width - 2) + "+")
    
    # Header
    print(f"| {'Field'.center(field_width)} | {'Value'.center(value_width)} |")
    print("+" + "-" * (table_width - 2) + "+")
    
    # Rows
    for key, value in data.items():
        print(f"| {key.ljust(field_width)} | {value.ljust(value_width)} |")
    
    # Bottom border
    print("+" + "-" * (table_width - 2) + "+")

def device_information():
    if not os.path.exists(config_file_path):
        print(f"Configuration file '{config_file_path}' does not exist.")
        return
    
    config_data = parse_config(config_file_path, fields_to_extract)
    if config_data:
        display_table(config_data)
    else:
        print("No matching fields found in the configuration file.")

def verify_connectivity():
    """
    Verify connectivity based on client or server role selection with a 10-second timeout.
    """
    role = input("Enter the role (client/server): ").strip().lower()

    if role == "server":
        # Flag to signal when to stop the server
        stop_event = threading.Event()

        def monitor_input():
            """Monitor for 'q' key press to stop the server gracefully."""
            while not stop_event.is_set():
                user_input = input()  # Use input() instead of blocking sys.stdin.read
                if user_input.strip().lower() == 'q':
                    print("\nStopping the server...")
                    stop_event.set()

        # Start a separate thread to monitor user input
        input_thread = threading.Thread(target=monitor_input, daemon=True)
        input_thread.start()

        # Server: Open port 8305 and listen for incoming connections
        print("Starting the server and listening on port 8305...(Press 'q' to stop)")
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Allow port reuse
            server_socket.bind(('0.0.0.0', 8305))
            server_socket.listen(1)
            print("Server is now listening for incoming connections on port 8305...")

            try:
                while not stop_event.is_set():
                    # Use `select` to wait for connections with a timeout to check `stop_event`
                    server_socket.settimeout(1)
                    try:
                        conn, addr = server_socket.accept()
                        print(f"Connection established with {addr[0]}:{addr[1]}")
                        print("Press 'q' to stop the server.")
                        conn.close()
                    except socket.timeout:
                        continue  # Timeout allows us to check the stop_event

            except Exception as e:
                print(f"Error: {e}")

        # Stop the server and ensure only one "Stopping the server..." message is shown
        print("Stopping the server...")

    elif role == "client":
        # Client: Prompt for server IP and test connectivity via telnet to port 8305
        server_ip = input("Enter the server IP address: ").strip()
        print(f"Attempting to telnet to {server_ip}:8305...")

        # Set a timeout of 10 seconds for the connection attempt
        start_time = time.time()
        try:
            result = subprocess.run(
                ["telnet", server_ip, "8305"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                timeout=10  # Timeout after 10 seconds
            )

            elapsed_time = time.time() - start_time

            if "Connected" in result.stdout:
                print(f"Successfully connected to {server_ip}:8305 in {elapsed_time:.2f} seconds")
            else:
                print(f"Failed to connect to {server_ip}:8305. Reason: {result.stderr.strip()}")
        except subprocess.TimeoutExpired:
            print(f"Connection attempt to {server_ip}:8305 timed out after 10 seconds.")
        except Exception as e:
            print(f"Error while trying to telnet: {e}")

    else:
        print("Invalid role selection. Please enter either 'client' or 'server'.")

    # Revert to main menu after completion of connectivity test
    return  # main() will be called after this function ends


def run_bandwidth_test():
    """
    Run the bandwidth test for the client or server.
    """
    role = input("Enter the role (client/server): ").strip().lower()

    if role == "server":
        stop_server = threading.Event()

        def monitor_input():
            """Monitor for 'q' key press to stop the server gracefully."""
            while not stop_server.is_set():
                # Use select for non-blocking input
                if sys.stdin in select.select([sys.stdin], [], [], 0.1)[0]:
                    user_input = sys.stdin.read(1)  # Read one character
                    if user_input.strip().lower() == 'q':
                        print("\nStopping the server...")
                        stop_server.set()

        input_thread = threading.Thread(target=monitor_input, daemon=True)
        input_thread.start()

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            server_socket.bind(('0.0.0.0', 8305))
            server_socket.listen(1)
            print("Server is now listening for incoming connections on port 8305... (Press 'q' to exit)\n")
            print(f"*** Note: If bandwidth is subject to high latency the test may take longer than expected. ***\n")

            try:
                while not stop_server.is_set():
                    server_socket.settimeout(1)  # Check stop condition every second
                    try:
                        conn, addr = server_socket.accept()
                        print(f"Connection established with {addr[0]}:{addr[1]}")
                        start_time = time.time()
                        bytes_received = 0

                        while True:
                            data = conn.recv(1024 * 1024)  # Receive 1MB chunks
                            if not data:
                                break
                            bytes_received += len(data)

                        elapsed_time = time.time() - start_time
                        print(f"Total data received: {bytes_received / (1024 * 1024):.2f} MB")
                        print(f"Elapsed time: {elapsed_time:.2f} seconds")
                        print(f"Approx. Bandwidth: {bytes_received * 8 / (elapsed_time * 1_000_000):.2f} Mbps")
                        conn.close()
                        print("Test completed. Returning to main menu.")
                        stop_server.set()  # Automatically stop the server after a test completes
                    except socket.timeout:
                        continue  # Check stop flag periodically
            except Exception as e:
                print(f"Server error: {e}")
            finally:
                print("Server has stopped.\n")

    elif role == "client":
        server_ip = input("Enter the server IP address: ").strip()
        test_duration = int(input("Enter the test duration in seconds: ").strip())
        print(f"Connecting to {server_ip} and starting bandwidth test for {test_duration} seconds...\n")
        print(f"*** Note: If bandwidth is subject to high latency the test may take longer than {test_duration} seconds. ***\n")

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((server_ip, 8305))
            print(f"Connected to server at {server_ip}:8305")

            start_time = time.time()
            bytes_sent = 0
            while time.time() - start_time < test_duration:
                try:
                    data = b'A' * (1024 * 1024)  # Send 1MB chunks
                    client_socket.sendall(data)
                    bytes_sent += len(data)
                except Exception as e:
                    print(f"Error: {e}")
                    break

            elapsed_time = time.time() - start_time
            print(f"Total data sent: {bytes_sent / (1024 * 1024):.2f} MB")
            print(f"Elapsed time: {elapsed_time:.2f} seconds")
            print(f"Approx. Bandwidth: {bytes_sent * 8 / (elapsed_time * 1_000_000):.2f} Mbps")

    else:
        print("Invalid role selection. Please enter either 'client' or 'server'.")

    # Return to main menu after test completes
    input("\nPress Enter to return to the main menu...")
    return

def verify_sftunnel_conf():
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

def verify_sftunnel_json():
    """
    Verify the contents of the sftunnel.json file by prompting for the peer's UUID.
    """
    print("To verify the sftunnel.json file, you need to provide the peer's UUID.")
    print("The peer's UUID can be found by running the 'show version' command on the peer device.")

    # Prompt the user to enter the UUID of the peer
    uuid = input("Enter the peer's UUID: ").strip()

    if not uuid:
        print("UUID cannot be empty.")
        input("\nPress Enter to return to the main menu...")
        return  # Return to the main menu if UUID is not provided

    # Construct the path to the sftunnel.json file
    json_path = f"/var/sf/peers/{uuid}/sftunnel.json"

    print(f"Displaying the contents of {json_path}...")

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
            print(f"Error reading {json_path}: {result.stderr.strip()}")
    except Exception as e:
        print(f"An error occurred while trying to read {json_path}: {e}")

    # Revert to main menu after checking sftunnel.json
    input("\nPress Enter to return to the main menu...")
    return

def validate_sftunnel_certificate():
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

def validate_database_table():
    """
    Validate a database table by querying the database for peer information.
    """
    print("To validate the database table, you need to provide the peer's UUID.")
    print("The peer's UUID can be found by running the 'show version' command on the peer device.")

    # Prompt the user to enter the UUID of the peer
    while True:
        uuid = input("Enter the peer's UUID: ").strip()

        if not uuid:
            print("UUID cannot be empty.")
            continue  # Prompt again if UUID is empty
        elif not validate_uuid(uuid):
            print("Invalid UUID format. Please enter a valid UUID.")
            continue  # Prompt again if UUID is invalid

        break  # Exit the loop once a valid UUID is provided

    # Construct the OmniQuery command to fetch peer data from the database, filtering by the provided UUID
    query_command = f"OmniQuery.pl -db mdb -e \"select name, ip, uuid, sw_version, role, active from EM_peers where uuid = '{uuid}';\""

    print(f"Running query for UUID {uuid}...")

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
                print("Query result:")
                print(output)
            else:
                print("No results found for the specified UUID.")
        else:
            print(f"Error executing query: {result.stderr.strip()}")
    except Exception as e:
        print(f"An error occurred while querying the database: {e}")

    # Revert to main menu after validating the database table
    input("\nPress Enter to return to the main menu...")
    return

def grep_logs():
    """
    Search logs based on the UUID and IP address and output to a file.
    """
    while True:
        uuid = input("Enter the UUID of the peer: ").strip()
        if not uuid:
            print("UUID cannot be empty.")
            continue
        elif not validate_uuid(uuid):
            print("Invalid UUID format. Please enter a valid UUID.")
            continue
        break  # Exit the loop once a valid UUID is provided

    while True:
        ip_address = input("Enter the IP address of the peer: ").strip()
        if not ip_address:
            print("IP address cannot be empty.")
            continue
        elif not validate_ip(ip_address):
            print("Invalid IP address format. Please enter a valid IP address.")
            continue
        break  # Exit the loop once a valid IP address is provided

    print(f"Gathering logs for UUID: {uuid}, IP Address: {ip_address}...")

    # Define output file name with timestamp
    output_file = f'{time.strftime("%Y%m%d_%H%M%S")}_filtered_logs.txt'

    try:
        # Construct the grep command to search for the UUID and IP address in the logs
        grep_command = f'grep -E "{uuid}|{ip_address}|sftunneld" /var/log/messages > {output_file}'

        # Run the grep command to search logs and write to the output file
        subprocess.run(grep_command, shell=True, check=True)

        print(f"Logs have been saved to {output_file}")

    except subprocess.CalledProcessError as e:
        print(f"Error occurred while gathering logs: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    # Revert to main menu after completing log gathering
    input("\nPress Enter to return to the main menu...")
    return

def em_peers():
    """
    Validate a database table by querying the database for peer information.
    """
    print("You can either enter a peer's UUID or leave it blank to get all peer data.")
    print("The peer's UUID can be found by running the 'show version' command on the peer device.")

    # Prompt the user to enter the UUID of the peer
    while True:
        uuid = input("Enter the peer's UUID (or leave blank to query all peers): ").strip()

        # If UUID is not empty, validate its format
        if uuid and not validate_uuid(uuid):
            print("Invalid UUID format. Please enter a valid UUID.")
            continue  # Prompt again if UUID is invalid

        break  # Exit the loop once a valid UUID or blank entry is provided

    # Construct the OmniQuery command based on whether the UUID is provided
    if uuid:
        query_command = f"OmniQuery.pl -db mdb -e \"select name, ip, uuid, sw_version, role, reg_state from EM_peers where uuid = '{uuid}';\""
    else:
        query_command = "OmniQuery.pl -db mdb -e \"select name, ip, uuid, sw_version, role, reg_state from EM_peers;\""

    print(f"Running query for UUID {uuid if uuid else 'all peers'}...")

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
                print("Query result:")
                print(output)
            else:
                print("No results found for the specified UUID or for all peers.")
        else:
            print(f"Error executing query: {result.stderr.strip()}")
    except Exception as e:
        print(f"An error occurred while querying the database: {e}")

    # Revert to main menu after validating the database table
    input("\nPress Enter to return to the main menu...")
    return

def ssl_peers():
    """
    Query the database for SSL peer information and provide the output.
    """
    print("Running query for SSL peer data...")

    # Construct the OmniQuery command to fetch SSL peer data from the database
    query_command = "OmniQuery.pl -db mdb -e \"select * from ssl_peer;\""

    try:
        # Execute the OmniQuery command and capture the output with explicit encoding handling
        result = subprocess.run(
            query_command,
            shell=True,  # Using shell=True to allow multi-part commands
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,  # Text mode to automatically decode
            encoding='utf-8',  # Try UTF-8 encoding, fallback can be added if needed
            errors='ignore'  # Ignore characters that can't be decoded
        )

        if result.returncode == 0:
            output = result.stdout.strip()
            if output:
                print("Query result:")
                print(output)
            else:
                print("No results found for SSL peer data.")
        else:
            print(f"Error executing query: {result.stderr.strip()}")
    except Exception as e:
        print(f"An error occurred while querying the SSL peer data: {e}")

    # Revert to main menu after querying the SSL peer data
    input("\nPress Enter to return to the main menu...")
    return

def notifications_table():
    """
    Prompt the user for notification status options and query the database accordingly.
    """
    while True:
        print("Choose a notification status to query:")
        print("1) All notifications")
        print("2) Failed notifications")
        print("3) Running notifications")
        print("0) Return to the previous menu")

        # Prompt for the user's choice
        choice = input("Enter your choice (1, 2, 3, 0): ").strip()

        if choice == '1':
            query_command = "OmniQuery.pl -db mdb -e \"SELECT seq, hex(uuid), notification_status.label, notification_status.status, body from notification JOIN notification_status ON notification.status = notification_status.status;\""
            break
        elif choice == '2':
            query_command = "OmniQuery.pl -db mdb -e \"SELECT seq, HEX(uuid), notification_status.label, notification_status.status, body FROM notification JOIN notification_status ON notification.status = notification_status.status WHERE notification.status = 13;\""
            break
        elif choice == '3':
            query_command = "OmniQuery.pl -db mdb -e \"SELECT seq, HEX(uuid), notification_status.label, notification_status.status, body FROM notification JOIN notification_status ON notification.status = notification_status.status WHERE notification.status = 7;\""
            break
        elif choice == '0':
            print("Returning to the previous menu...")
            return  # Exit the function to return to the previous menu
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 0.")

    print(f"Running query for {'all' if choice == '1' else 'failed' if choice == '2' else 'running'} notifications...")

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
                print("Query result:")
                print(output)
            else:
                print("No results found.")
        else:
            print(f"Error executing query: {result.stderr.strip()}")
    except Exception as e:
        print(f"An error occurred while querying the notifications table: {e}")

    # Revert to main menu after querying the notifications table
    input("\nPress Enter to return to the main menu...")
    return

def vdb_table():
    """
    Query the database for SSL peer information and provide the output.
    """
    print("Running query for VDB table data...")

    # Construct the OmniQuery command to fetch SSL peer data from the database
    query_command = "OmniQuery.pl -db mdb -e \"select * from rna_vdb_version;\""

    try:
        # Execute the OmniQuery command and capture the output with explicit encoding handling
        result = subprocess.run(
            query_command,
            shell=True,  # Using shell=True to allow multi-part commands
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,  # Text mode to automatically decode
            encoding='utf-8',  # Try UTF-8 encoding, fallback can be added if needed
            errors='ignore'  # Ignore characters that can't be decoded
        )

        if result.returncode == 0:
            output = result.stdout.strip()
            if output:
                print("Query result:")
                print(output)
            else:
                print("No results found for SSL peer data.")
        else:
            print(f"Error executing query: {result.stderr.strip()}")
    except Exception as e:
        print(f"An error occurred while querying the SSL peer data: {e}")

    # Revert to main menu after querying the SSL peer data
    input("\nPress Enter to return to the main menu...")
    return

def geodb_table():
    """
    Query the database for SSL peer information and provide the output.
    """
    print("Running query for GEO DB data...")

    # Construct the OmniQuery command to fetch SSL peer data from the database
    query_command = "OmniQuery.pl -db mdb -e \"select * from geodb_version;\""

    try:
        # Execute the OmniQuery command and capture the output with explicit encoding handling
        result = subprocess.run(
            query_command,
            shell=True,  # Using shell=True to allow multi-part commands
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,  # Text mode to automatically decode
            encoding='utf-8',  # Try UTF-8 encoding, fallback can be added if needed
            errors='ignore'  # Ignore characters that can't be decoded
        )

        if result.returncode == 0:
            output = result.stdout.strip()
            if output:
                print("Query result:")
                print(output)
            else:
                print("No results found for SSL peer data.")
        else:
            print(f"Error executing query: {result.stderr.strip()}")
    except Exception as e:
        print(f"An error occurred while querying the SSL peer data: {e}")

    # Revert to main menu after querying the SSL peer data
    input("\nPress Enter to return to the main menu...")
    return

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

def fail_deployment():
    """
    Prompt the user for a UUID and set the status of the notification to 'failed' (status=13).
    """
    print("WARNING: You are about to fail a deployment notification. Make sure you have the correct UUID.")
    print("If you're unsure, do not proceed with the action.")

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
    
def registration_troubleshooting():
    """
    Main menu for the script.
    """
    while True:  # Replace recursion with a loop for better performance
        flush_stdin()  # Ensure the input buffer is clean
        print("\n----- Registration Menu -----")
        print("1) Verify Connectivity")
        print("2) Run Bandwidth Test")
        print("3) Verify sftunnel.conf")
        print("4) Verify sftunnel.json")
        print("5) Validate Database Table")
        print("6) Validate sftunnel Certificate")
        print("7) Gather Logs")
        print("0) Return to Main Menu")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            verify_connectivity()
        elif choice == '2':
            run_bandwidth_test()
        elif choice == '3':
            verify_sftunnel_conf()
        elif choice == '4':
            verify_sftunnel_json()
        elif choice == '5':
            validate_database_table()
        elif choice == '6':
            validate_sftunnel_certificate()
        elif choice == '7':
            grep_logs()
        elif choice == '0':
            print("Returning to main menu.")
            break
        else:
            print("Invalid choice. Please try again.")
        flush_stdin()  # Flush input before returning to the menu

def database_troubleshooting():
    """
    Main menu for the script.
    """
    while True:  # Replace recursion with a loop for better performance
        flush_stdin()  # Ensure the input buffer is clean
        print("\n----- Database Menu -----")
        print("1) Check EM Peers Table")
        print("2) Check SSL Peer Table")
        print("3) Check Notifications Table")
        print("4) Check VDB Table")
        print("5) Check GeoDB Table")
        print("6) Delete Notification")
        print("7) Fail Stuck Deployment")
        print("0) Return to Main Menu")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            em_peers()
        elif choice == '2':
            ssl_peers()
        elif choice == '3':
            notifications_table()
        elif choice == '4':
            vdb_table()
        elif choice == '5':
            geodb_table()
        elif choice == '6':
            delete_notification()
        elif choice == '7':
            fail_deployment()
        elif choice == '0':
            print("Returning to main menu.")
            break
        else:
            print("Invalid choice. Please try again.")
        flush_stdin()  # Flush input before returning to the menu

def main_menu():
    while True:
        print("\n----- Main Menu -----")
        print("1) Device Information")
        print("2) Registration Troubleshooting")
        print("3) Database Troubleshooting")
        print("0) Exit")
        choice = input("Select an option: ")

        if choice == "1":
            device_information()
        elif choice == "2":
            registration_troubleshooting()
        elif choice == "3":
            database_troubleshooting()
        elif choice == "0":
            print("Exiting the script. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main_menu()
