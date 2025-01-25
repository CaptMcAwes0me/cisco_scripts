# Description: This script is used to test the bandwidth between the client and server.

import socket
import time
import threading
import sys
import select


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
            server_socket.bind(('0.0.0.0', 8305))
            server_socket.listen(1)
            print(f"\n[+] Server is now listening on port 8305... (Press 'q' to stop the server)\n")
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
            client_socket.connect((server_ip, 8305))
            print(f"[+] Connected to server at {server_ip}:8305")

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
