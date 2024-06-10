'''

Legal Disclaimer:

This script is provided for educational and informational purposes only. The author (programmer) makes no representations or warranties of any kind, express or implied, about the completeness, accuracy, reliability, suitability, or availability with respect to the script or the information, products, services, or related graphics contained in the script for any purpose. Any reliance you place on such information is therefore strictly at your own risk.

In no event will the author be liable for any loss or damage including without limitation, indirect or consequential loss or damage, or any loss or damage whatsoever arising from loss of data or profits arising out of or in connection with the use of this script.

By using this script, you agree that you are solely responsible for any consequences that may arise from its use. The author disclaims any responsibility for any actions taken by users of this script.

Usage of this script constitutes acceptance of these terms and conditions.

Authored by Garrett McCollum - Cisco Systems Inc. (2024)

'''

import paramiko
import time
import getpass

def push_commands_to_router(router_ip, username, password, commands):
    try:
        # Initialize SSH client
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Connect to the router
        ssh.connect(router_ip, username=username, password=password)
        print(f"Connected to {router_ip}")

        # Open a shell
        remote_conn = ssh.invoke_shell()

        # Send each command
        for command in commands:
            remote_conn.send(command + '\n')
            time.sleep(1)  # Give the command some time to be processed

        # Close the connection
        ssh.close()
        print(f"Commands sent to {router_ip} and connection closed")

    except Exception as e:
        print(f"Failed to connect to {router_ip}: {e}")

# Prompt user for input
router_ips = input("Enter the IP addresses of the routers, separated by commas: ").split(',')
username = input("Enter the SSH username: ")
password = getpass.getpass("Enter the SSH password: ")

# Prompt user to enter path to the file containing commands
commands_file_path = input("Enter the path to the file containing commands: ")

# Read commands from the file
try:
    with open(commands_file_path, 'r') as file:
        commands = file.readlines()
        # Remove leading and trailing whitespace from each command
        commands = [command.strip() for command in commands if command.strip()]
except FileNotFoundError:
    print("File not found. Please check the path and try again.")
    exit()

# Iterate over each router IP and push the commands
for router_ip in router_ips:
    router_ip = router_ip.strip()  # Remove any extra spaces
    push_commands_to_router(router_ip, username, password, commands)

# Prompt user to enter command for verification
verification_command = input("Enter the command for verification (e.g., 'show run interface GigabitEthernet0/10'): ")

# Iterate over each router IP for verification
for router_ip in router_ips:
    try:
        # Initialize SSH client
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Connect to the router
        ssh.connect(router_ip, username=username, password=password)
        print(f"Connected to {router_ip}")

        # Execute the verification command
        stdin, stdout, stderr = ssh.exec_command(verification_command)
        verification_output = stdout.read().decode('utf-8')

        # Print the verification output
        print(f"Verification output for {router_ip}:\n{verification_output}")

        # Close the connection
        ssh.close()

    except Exception as e:
        print(f"Failed to connect to {router_ip} for verification: {e}")
