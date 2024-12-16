#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: Garrett McCollum
Date: 2024-12-14
Description:
    This script performs various network-related tasks, including verifying connectivity,
    running bandwidth tests, checking configuration files, validating certificates, and
    tailing logs for peer devices.

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
            print("Press 'q' to stop the server gracefully...")
            while not stop_event.is_set():
                user_input = input()  # Use input() instead of blocking sys.stdin.read
                if user_input.strip().lower() == 'q':
                    print("\nStopping the server...")
                    stop_event.set()

        # Start a separate thread to monitor user input
        input_thread = threading.Thread(target=monitor_input, daemon=True)
        input_thread.start()

        # Server: Open port 8305 and listen for incoming connections
        print("Starting the server and listening on port 8305...")
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
                        conn.close()
                        break  # Accept only one connection for this test
                    except socket.timeout:
                        continue  # Timeout allows us to check the stop_event
            except Exception as e:
                print(f"Error: {e}")
            finally:
                print("Server stopped. Returning to main menu...")

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
    main()

def run_bandwidth_test():
    """
    Run the bandwidth test for the client or server.
    """
    role = input("Enter the role (client/server): ").strip().lower()

    if role == "server":
        print("Starting the server and listening on port 8305...")
        stop_server = threading.Event()

        def monitor_input():
            """Monitor for 'q' key press to stop the server gracefully."""
            print("Press 'q' to stop the server gracefully...")
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
            print("Server is now listening for incoming connections on port 8305... (Press 'q' to exit)")

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
        print(f"Connecting to {server_ip} and starting bandwidth test for {test_duration} seconds...")

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
    main()


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
    main()

def verify_sftunnel_json():
    """
    Verify the contents of the sftunnel.json file by prompting for the peer's UUID.
    """
    print("To verify the sftunnel.json file, you need to provide the peer's UUID.")
    print("The peer's UUID can be found by running the 'show version' command on the peer device.")

    # Prompt the user to enter the UUID of the peer
    uuid = input("Enter the peer's UUID: ").strip()

    if not uuid:
        print("UUID cannot be empty. Returning to the main menu.")
        main()  # Return to the main menu if UUID is not provided

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
    main()

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
    main()

def validate_database_table():
    """
    Validate a database table by querying the database for peer information and formatting the output.
    """
    print("To validate the database table, you need to provide the peer's UUID.")
    print("The peer's UUID can be found by running the 'show version' command on the peer device.")

    # Prompt the user to enter the UUID of the peer
    uuid = input("Enter the peer's UUID: ").strip()

    if not uuid:
        print("UUID cannot be empty. Returning to the main menu.")
        main()  # Return to the main menu if UUID is not provided

    # Construct the OmniQuery command to fetch peer data from the database
    query_command = f"OmniQuery.pl -db mdb -e \"select name,ip,uuid,role,active from EM_peers;\" | grep {uuid}"

    print(f"Running query for UUID {uuid}...")

    try:
        # Execute the OmniQuery command and capture the output
        result = subprocess.run(
            query_command,
            shell=True,  # Using shell=True to allow pipes and multi-part commands
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        if result.returncode == 0:
            # Format the output as a table
            output = result.stdout.strip()
            if output:
                # Add table headers and format the output accordingly
                print("+---------------+---------------+--------------------------------------+------+" )
                print("| name          | ip            | uuid                                 | role | active |")
                print("+---------------+---------------+--------------------------------------+------+" )

                # Split the output into rows and print each one
                for line in output.splitlines():
                    columns = line.split("|")
                    formatted_line = "|".join([col.strip() for col in columns])
                    print(f"{formatted_line}|")
                print("+---------------+---------------+--------------------------------------+------+" )
            else:
                print("No results found for the specified UUID.")
        else:
            print(f"Error executing query: {result.stderr.strip()}")
    except Exception as e:
        print(f"An error occurred while querying the database: {e}")

    # Revert to main menu after validating the database table
    main()

def tail_logs():
    """
    Tail the logs based on user input and allow stopping with 'q'.
    """
    uuid = input("Enter the UUID of the peer: ").strip()
    ip_address = input("Enter the IP address of the peer: ").strip()

    if not uuid or not ip_address:
        print("UUID or IP address cannot be empty. Returning to main menu.")
        return

    print(f"Tailing logs for UUID: {uuid}, IP Address: {ip_address}... (Press 'q' to stop)")

    # Save original terminal settings
    orig_settings = termios.tcgetattr(sys.stdin)

    try:
        # Set terminal to raw mode
        tty.setraw(sys.stdin.fileno())

        # Start the subprocess to tail logs
        tail_process = subprocess.Popen(
            f"pigtail --outfile /var/log/{time.strftime('%Y%m%d_%H%M%S')}_pigtail_registration | grep -E {uuid}|{ip_address}|sftunneld",
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        # Monitor for 'q' key press
        while True:
            if sys.stdin.read(1) == 'q':
                print("\nStopping log tailing...")
                tail_process.terminate()
                break

        tail_process.wait()

    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Restore original terminal settings
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, orig_settings)

    # Revert to main menu after tailing logs
    main()

def main():
    """
    Main menu for the script.
    """
    print("\n----- Main Menu -----")
    print("1) Verify Connectivity")
    print("2) Run Bandwidth Test")
    print("3) Verify sftunnel.conf")
    print("4) Verify sftunnel.json")
    print("5) Validate Database Table")
    print("6) Validate sftunnel Certificate")
    print("7) Tail Logs")
    print("0) Exit")

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
        tail_logs()
    elif choice == '0':
        print("Exiting the script. Goodbye!")
    else:
        print("Invalid choice. Please try again.")
        main()

if __name__ == "__main__":
    main()
