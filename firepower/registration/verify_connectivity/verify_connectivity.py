# Description: This script provides a simple connectivity test for client or server mode.

import socket
import subprocess
import time
import threading


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

        # Server: Open port 8305 and listen for incoming connections
        print("[+] Starting the server and listening on port 8305... (Press 'q' to stop)")

        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
                server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Allow port reuse
                server_socket.bind(('0.0.0.0', 8305))
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
        # Client: Prompt for server IP and test connectivity via telnet to port 8305
        server_ip = input("\nEnter the server IP address: ").strip()
        print(f"[+] Attempting to telnet to {server_ip}:8305...")

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
                print(f"[+] Successfully connected to {server_ip}:8305 in {elapsed_time:.2f} seconds")
            else:
                print(f"[!] Failed to connect to {server_ip}:8305. Reason: {result.stderr.strip()}")

        except subprocess.TimeoutExpired:
            print(f"[!] Connection attempt to {server_ip}:8305 timed out after 10 seconds.")
        except Exception as e:
            print(f"[!] Error while trying to telnet: {e}")

    else:
        print("\n[!] Invalid role selection. Please enter either 'client' or 'server'.")

    # Return to the main menu after completing the connectivity test
    input("\nPress Enter to return to the main menu...")
    return
