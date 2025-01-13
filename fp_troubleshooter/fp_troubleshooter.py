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
    print("\n" + "=" * 80)
    print(" Connectivity Test: Client or Server Mode ".center(80, "="))
    print("=" * 80)

    role = input("\nEnter the role (client/server): ").strip().lower()

    if role == "server":
        # Flag to signal when to stop the server
        stop_event = threading.Event()

        def monitor_input():
            """Monitor for 'q' key press to stop the server gracefully."""
            while not stop_event.is_set():
                user_input = input()  # Use input() instead of blocking sys.stdin.read
                if user_input.strip().lower() == 'q':
                    print("\n[!] Stopping the server...")
                    stop_event.set()

        # Start a separate thread to monitor user input
        input_thread = threading.Thread(target=monitor_input, daemon=True)
        input_thread.start()

        # Server: Open port 12345 and listen for incoming connections
        print("[+] Starting the server and listening on port 12345... (Press 'q' to stop)")

        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
                server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Allow port reuse
                server_socket.bind(('0.0.0.0', 12345))
                server_socket.listen(1)
                print("[+] Server is now listening for incoming connections...")

                while not stop_event.is_set():
                    server_socket.settimeout(1)  # Check stop_event periodically
                    try:
                        conn, addr = server_socket.accept()
                        print(f"\n[+] Connection established with {addr[0]}:{addr[1]}")
                        print("[+] Press 'q' to stop the server.")
                        conn.close()
                    except socket.timeout:
                        continue  # Timeout allows us to check stop_event

        except Exception as e:
            print(f"[!] Error: {e}")

        # Ensure only one "Stopping the server..." message is shown
        print("[!] Stopping the server...")

    elif role == "client":
        # Client: Prompt for server IP and test connectivity via telnet to port 12345
        server_ip = input("\nEnter the server IP address: ").strip()
        print(f"[+] Attempting to telnet to {server_ip}:12345...")

        # Set a timeout of 10 seconds for the connection attempt
        start_time = time.time()

        try:
            result = subprocess.run(
                ["telnet", server_ip, "12345"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                timeout=10  # Timeout after 10 seconds
            )

            elapsed_time = time.time() - start_time

            if "Connected" in result.stdout:
                print(f"[+] Successfully connected to {server_ip}:12345 in {elapsed_time:.2f} seconds")
            else:
                print(f"[!] Failed to connect to {server_ip}:12345. Reason: {result.stderr.strip()}")

        except subprocess.TimeoutExpired:
            print(f"[!] Connection attempt to {server_ip}:12345 timed out after 10 seconds.")
        except Exception as e:
            print(f"[!] Error while trying to telnet: {e}")

    else:
        print("\n[!] Invalid role selection. Please enter either 'client' or 'server'.")

    # Return to the main menu after completing the connectivity test
    input("\nPress Enter to return to the main menu...")
    return

def run_bandwidth_test():
    """
    Run the bandwidth test for the client or server.
    """
    print("\n" + "=" * 80)
    print(" Bandwidth Test: Client or Server Mode ".center(80, "="))
    print("=" * 80)

    role = input("\nEnter the role (client/server): ").strip().lower()

    if role == "server":
        stop_server = threading.Event()

        def monitor_input():
            """Monitor for 'q' key press to stop the server gracefully."""
            while not stop_server.is_set():
                # Use select for non-blocking input
                if sys.stdin in select.select([sys.stdin], [], [], 0.1)[0]:
                    user_input = sys.stdin.read(1)  # Read one character
                    if user_input.strip().lower() == 'q':
                        print("\n[!] Stopping the server...")
                        stop_server.set()

        input_thread = threading.Thread(target=monitor_input, daemon=True)
        input_thread.start()

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            server_socket.bind(('0.0.0.0', 12345))
            server_socket.listen(1)
            print(f"\n[+] Server is now listening on port 12345... (Press 'q' to stop the server)\n")
            print(f"*** Note: The test may take longer if bandwidth experiences high latency. ***\n")

            try:
                while not stop_server.is_set():
                    server_socket.settimeout(1)  # Check stop condition every second
                    try:
                        conn, addr = server_socket.accept()
                        print(f"\n[+] Connection established with {addr[0]}:{addr[1]}")
                        start_time = time.time()
                        bytes_received = 0

                        while True:
                            data = conn.recv(1024 * 1024)  # Receive 1MB chunks
                            if not data:
                                break
                            bytes_received += len(data)

                        elapsed_time = time.time() - start_time
                        print(f"\n[+] Total data received: {bytes_received / (1024 * 1024):.2f} MB")
                        print(f"[+] Elapsed time: {elapsed_time:.2f} seconds")
                        print(f"[+] Approx. Bandwidth: {bytes_received * 8 / (elapsed_time * 1_000_000):.2f} Mbps")
                        conn.close()
                        print("\n[+] Test completed. Stopping server...\n")
                        stop_server.set()  # Automatically stop the server after the test
                    except socket.timeout:
                        continue  # Check stop flag periodically
            except Exception as e:
                print(f"[!] Server error: {e}")
            finally:
                print("\n[!] Server has stopped.\n")

    elif role == "client":
        server_ip = input("\nEnter the server IP address: ").strip()
        test_duration = int(input("Enter the test duration in seconds: ").strip())
        print(f"\n[+] Connecting to {server_ip} for a bandwidth test of {test_duration} seconds...\n")
        print(f"*** Note: The test may take longer if bandwidth experiences high latency. ***\n")

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((server_ip, 12345))
            print(f"[+] Connected to server at {server_ip}:12345")

            start_time = time.time()
            bytes_sent = 0
            while time.time() - start_time < test_duration:
                try:
                    data = b'A' * (1024 * 1024)  # Send 1MB chunks
                    client_socket.sendall(data)
                    bytes_sent += len(data)
                except Exception as e:
                    print(f"[!] Error: {e}")
                    break

            elapsed_time = time.time() - start_time
            print(f"\n[+] Total data sent: {bytes_sent / (1024 * 1024):.2f} MB")
            print(f"[+] Elapsed time: {elapsed_time:.2f} seconds")
            print(f"[+] Approx. Bandwidth: {bytes_sent * 8 / (elapsed_time * 1_000_000):.2f} Mbps")

    else:
        print("\n[!] Invalid role selection. Please enter either 'client' or 'server'.")

    # Return to main menu after test completes
    input("\nPress Enter to return to the main menu...")
    return

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

def display_disk_usage():
    """
    Display disk usage with 'df -TH'.
    """
    try:
        result = subprocess.run(["df", "-TH"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print(result.stdout)
    except Exception as e:
        print(f"An error occurred while running 'df -TH': {e}")

def find_large_files():
    """
    Find files greater than a user-specified size.
    """
    while True:
        try:
            size = input("\nEnter the file size (e.g., 100M, 1G) or '0' to return to the menu: ").strip()
            if size == '0':
                print("\nReturning to the previous menu...")
                break
            find_command = f"find / -type f -size +{size} 2>/dev/null"
            print(f"\nFinding files greater than {size}...\n")
            result = subprocess.run(find_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            if result.stdout:
                print(result.stdout)
            else:
                print(f"\n[!] No files found greater than {size}.")
        except Exception as e:
            print(f"An error occurred while finding large files: {e}")

def gather_deleted_files_info():
    """
    Gather information about deleted files with 'lsof | grep -i deleted' and save it to a file.
    """
    try:
        # Get current date and time
        current_time = time.strftime("%Y%m%d_%H%M%S")
        output_file = f"/var/common/{current_time}_deleted_files.txt"

        # Run the command to find deleted files
        result = subprocess.run("lsof | grep -i deleted", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # Write the output to a file
        with open(output_file, 'w') as file:
            file.write(result.stdout)

        print(f"\nDeleted file information has been saved to {output_file}")

    except Exception as e:
        print(f"An error occurred while gathering deleted file information: {e}")

def registration_troubleshooting():
    while True:  # Replace recursion with a loop for better performance
        flush_stdin()  # Ensure the input buffer is clean
        print("\n" + "=" * 80)
        print(" Registration Menu ".center(80, "="))
        print("=" * 80)
        print("1) Verify Connectivity")
        print("2) Run Bandwidth Test")
        print("3) Check sftunnel.conf")
        print("4) Check sftunnel.json")
        print("5) Check EM Peers Table")
        print("6) Check sftunnel Certificate")
        print("7) Gather Logs")
        print("0) Return to Main Menu")
        print("=" * 80)

        # Prompt for the user's choice
        choice = input("Enter your choice (0-7): ").strip()

        # Process the user's choice
        if choice == '1':
            print("\n" + "-" * 80)
            print("Verifying Connectivity...".center(80))
            print("-" * 80)
            verify_connectivity()
        elif choice == '2':
            print("\n" + "-" * 80)
            print("Running Bandwidth Test...".center(80))
            print("-" * 80)
            run_bandwidth_test()
        elif choice == '3':
            print("\n" + "-" * 80)
            print("Checking sftunnel.conf...".center(80))
            print("-" * 80)
            sftunnel_conf()
        elif choice == '4':
            print("\n" + "-" * 80)
            print("Checking sftunnel.json...".center(80))
            print("-" * 80)
            sftunnel_json()
        elif choice == '5':
            print("\n" + "-" * 80)
            print("Checking EM Peers Table...".center(80))
            print("-" * 80)
            em_peers()
        elif choice == '6':
            print("\n" + "-" * 80)
            print("Checking sftunnel Certificate...".center(80))
            print("-" * 80)
            sftunnel_certificate()
        elif choice == '7':
            print("\n" + "-" * 80)
            print("Gathering Logs...".center(80))
            print("-" * 80)
            grep_logs()
        elif choice == '0':
            print("\nReturning to main menu...")
            break
        else:
            print("\n[!] Invalid choice. Please enter a number between 0 and 7.")


def database_troubleshooting():
    """
    Main menu for database troubleshooting.
    """
    while True:
        flush_stdin()  # Ensure the input buffer is clean

        print("\n" + "=" * 80)
        print(" Database Troubleshooting Menu ".center(80, "="))
        print("=" * 80)
        print("1) Check EM Peers Table")
        print("2) Check SSL Peer Table")
        print("3) Check Notifications Table")
        print("4) Check VDB Table")
        print("5) Check GeoDB Table")
        print("6) Delete Peer from EM Peer Table")
        print("7) Delete Notification")
        print("8) Fail Stuck Deployment")
        print("0) Return to Main Menu")
        print("=" * 80)

        # Prompt the user for their choice
        choice = input("Enter your choice (0-7): ").strip()

        # Process the user's choice
        if choice == '1':
            print("\n" + "-" * 80)
            print("Checking EM Peers Table...".center(80))
            print("-" * 80)
            em_peers()
        elif choice == '2':
            print("\n" + "-" * 80)
            print("Checking SSL Peer Table...".center(80))
            print("-" * 80)
            ssl_peers()
        elif choice == '3':
            print("\n" + "-" * 80)
            print("Checking Notifications Table...".center(80))
            print("-" * 80)
            notifications_table()
        elif choice == '4':
            print("\n" + "-" * 80)
            print("Checking VDB Table...".center(80))
            print("-" * 80)
            vdb_table()
        elif choice == '5':
            print("\n" + "-" * 80)
            print("Checking GeoDB Table...".center(80))
            print("-" * 80)
            geodb_table()
        elif choice == '6':
            print("\n" + "-" * 80)
            print("Delete Peer...".center(80))
            print("-" * 80)
            remove_peer()
        elif choice == '7':
            print("\n" + "-" * 80)
            print("Delete Notification...".center(80))
            print("-" * 80)
            delete_notification()
        elif choice == '8':
            print("\n" + "-" * 80)
            print("Fail Stuck Deployment...".center(80))
            print("-" * 80)
            fail_deployment()
        elif choice == '0':
            print("\nReturning to the main menu...")
            break
        else:
            print("\n[!] Invalid choice. Please enter a number between 0 and 7.")

        flush_stdin()  # Flush input before returning to the menu

def disk_usage_troubleshooting():
    """
    Disk usage troubleshooting menu.
    """
    while True:
        print("\n" + "=" * 80)
        print(" Disk Usage Troubleshooting Menu ".center(80, "="))
        print("=" * 80)
        print("1) Display disk usage (df -TH)")
        print("2) Find large files")
        print("3) Gather deleted file information")
        print("0) Return to Main Menu")
        print("=" * 80)

        choice = input("Select an option (0-3): ").strip()

        if choice == "1":
            print("\n" + "-" * 80)
            print("Displaying disk usage...".center(80))
            print("-" * 80)
            display_disk_usage()
        elif choice == "2":
            print("\n" + "-" * 80)
            print("Finding large files...".center(80))
            print("-" * 80)
            find_large_files()
        elif choice == "3":
            print("\n" + "-" * 80)
            print("Gathering deleted file information...".center(80))
            print("-" * 80)
            gather_deleted_files_info()
        elif choice == "0":
            print("\nReturning to the main menu...")
            break
        else:
            print("\n[!] Invalid choice. Please enter a number between 0 and 3.")

def main_menu():
    while True:
        print("\n" + "=" * 80)
        print(" Main Menu ".center(80, "="))
        print("=" * 80)
        print("1) Device Information")
        print("2) Registration Troubleshooting")
        print("3) Database Troubleshooting")
        print("4) Disk Usage Troubleshooting")
        print("0) Exit")
        print("=" * 80)

        # Prompt the user for their choice
        choice = input("Select an option (0-3): ").strip()

        # Process the user's choice
        if choice == "1":
            print("\n" + "-" * 80)
            print("Accessing Device Information...".center(80))
            print("-" * 80)
            device_information()
        elif choice == "2":
            print("\n" + "-" * 80)
            print("Accessing Registration Troubleshooting...".center(80))
            print("-" * 80)
            registration_troubleshooting()
        elif choice == "3":
            print("\n" + "-" * 80)
            print("Accessing Database Troubleshooting...".center(80))
            print("-" * 80)
            database_troubleshooting()
        elif choice == "4":
            print("\n" + "-" * 80)
            print("Accessing Disk Usage Troubleshooting...".center(80))
            print("-" * 80)
            disk_usage_troubleshooting()
        elif choice == "0":
            print("\nExiting the script. Goodbye!")
            break
        else:
            print("\n[!] Invalid choice. Please enter a number between 0 and 3.")


if __name__ == "__main__":
    main_menu()
