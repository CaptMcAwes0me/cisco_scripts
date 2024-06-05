'''

Legal Disclaimer:

This script is provided for educational and informational purposes only. The author (programmer) makes no representations or warranties of any kind, express or implied, about the completeness, accuracy, reliability, suitability, or availability with respect to the script or the information, products, services, or related graphics contained in the script for any purpose. Any reliance you place on such information is therefore strictly at your own risk.

In no event will the author be liable for any loss or damage including without limitation, indirect or consequential loss or damage, or any loss or damage whatsoever arising from loss of data or profits arising out of or in connection with the use of this script.

By using this script, you agree that you are solely responsible for any consequences that may arise from its use. The author disclaims any responsibility for any actions taken by users of this script.

Usage of this script constitutes acceptance of these terms and conditions.

Authored by Garrett McCollum - Cisco Systems Inc. (2024)

'''

import re
import ipaddress
from collections import defaultdict
import os

# Function to convert subnet to CIDR notation
def subnet_to_cidr(subnet):
    return ipaddress.ip_network(subnet, strict=False).with_prefixlen

# Function to parse route table from file content
def parse_route_table(file_content):
    # Initialize nested defaultdict to store route information per VRF and protocol
    vrf_routes = defaultdict(lambda: defaultdict(list))
    current_vrf = None  # Initialize current VRF as None

    # Mapping of routing protocols to their full names
    protocol_map = {
        'L': 'Local',
        'C': 'Connected',
        'S': 'Static',
        'R': 'RIP',
        'M': 'Mobile',
        'B': 'BGP',
        'D': 'EIGRP',
        'EX': 'EIGRP External',
        'O': 'OSPF',
        'IA': 'OSPF Inter Area',
        'N1': 'OSPF NSSA External Type 1',
        'N2': 'OSPF NSSA External Type 2',
        'E1': 'OSPF External Type 1',
        'E2': 'OSPF External Type 2',
        'V': 'VPN',
        'i': 'IS-IS',
        'su': 'IS-IS Summary',
        'L1': 'IS-IS Level-1',
        'L2': 'IS-IS Level-2',
        'ia': 'IS-IS Inter Area',
        '*': 'Candidate Default',
        'U': 'Per-User Static Route',
        'o': 'ODR',
        'P': 'Periodic Downloaded Static Route',
        '+': 'Replicated Route',
        'SI': 'Static InterVRF',
        'BI': 'BGP InterVRF'
    }

    # Iterate over each line in the file content
    for line in file_content.splitlines():
        # Check if the line indicates a new routing table (VRF)
        if line.startswith("Routing Table:"):
            current_vrf = line.split(":")[1].strip()
        else:
            if not current_vrf:
                current_vrf = "default"  # Assume default VRF if no "Routing Table:" line is found
            # Regex pattern to match route entries
            match = re.match(r"(\S+)\s+(\d+\.\d+\.\d+\.\d+)\s+(\d+\.\d+\.\d+\.\d+)\s+\[(\d+)/(\d+)\]\s+via\s+(\d+\.\d+\.\d+\.\d+)", line)
            if match:
                # Extract route attributes
                protocol = match.group(1)
                network = match.group(2)
                subnet = match.group(3)
                admin_distance = int(match.group(4))
                metric = int(match.group(5))
                next_hop = match.group(6)
                # Convert subnet to CIDR notation
                cidr_network = subnet_to_cidr(f"{network}/{subnet}")
                # Append route information to the corresponding VRF and protocol
                vrf_routes[current_vrf][protocol_map.get(protocol, protocol)].append((cidr_network, next_hop, admin_distance, metric))
            else:
                # Regex pattern to match directly connected routes
                match = re.match(r"(\S+)\s+(\d+\.\d+\.\d+\.\d+)\s+(\d+\.\d+\.\d+\.\d+)\s+is\s+directly\s+connected", line)
                if match:
                    # Extract route attributes
                    protocol = match.group(1)
                    network = match.group(2)
                    subnet = match.group(3)
                    # Convert subnet to CIDR notation
                    cidr_network = subnet_to_cidr(f"{network}/{subnet}")
                    # Append directly connected route information
                    vrf_routes[current_vrf][protocol_map.get(protocol, protocol)].append((cidr_network, "directly connected", 0, 0))

    return vrf_routes

# Function to display routes based on selected VRFs and target subnet
def display_routes(vrf_routes, selected_vrfs, target_subnet):
    output = []

    # Iterate over selected VRFs
    for vrf in selected_vrfs:
        # Check if the selected VRF exists in the parsed route table
        if vrf not in vrf_routes:
            continue
        output.append(f"VRF: {vrf}")
        # Iterate over protocols and their associated routes in the selected VRF
        for protocol, routes in vrf_routes[vrf].items():
            filtered_routes = []
            # Filter routes based on the target subnet if provided
            if target_subnet:
                target_ip = ipaddress.ip_address(target_subnet.split("/")[0])  # Extract IP address from subnet
                max_prefix_len = -1
                max_specific_route = None
                for route in routes:
                    network = ipaddress.ip_network(route[0])
                    if target_ip in network and network.prefixlen > max_prefix_len:
                        max_prefix_len = network.prefixlen
                        max_specific_route = route
                if max_specific_route:
                    filtered_routes.append(max_specific_route)
            else:
                filtered_routes = routes
            
            if filtered_routes:
                # Display filtered routes in a formatted table
                output.append(f"  Protocol: {protocol}")
                header = f"  ┌{'─' * 20}┬{'─' * 20}┬{'─' * 6}┬{'─' * 6}──┐"
                output.append(header)
                output.append(f"  │ {'Network (CIDR)':<18} │ {'Next Hop':<18} │ {'AD':<4} │ {'Metric':<6} │")
                output.append(f"  ├{'─' * 20}┼{'─' * 20}┼{'─' * 6}┼{'─' * 6}──┤")
                for network, next_hop, admin_distance, metric in filtered_routes:
                    output.append(f"  │ {network:<18} │ {next_hop:<18} │ {admin_distance:<4} │ {metric:<6} │")
                output.append(f"  └{'─' * 20}┴{'─' * 20}┴{'─' * 6}┴{'─' * 6}──┘")
                output.append("")  # Add an empty line for better readability

    return "\n".join(output)

# Main function to execute the script
def main():
    file_path = input("Please enter the path to the route table file: ")
    try:
        # Open and read the route table file
        with open(file_path, 'r') as file:
            file_content = file.read()
            # Parse route table
            vrf_routes = parse_route_table(file_content)
            
            # Get list of VRFs from parsed route table
            vrfs = list(vrf_routes.keys())
            # Create dictionary to map numeric choices to VRFs
            vrf_choices = {str(i + 1): vrf for i, vrf in enumerate(vrfs)}
            # Add option to select all
            vrf_choices[str(len(vrfs) + 1)] = 'all'

            # Prompt user to select VRF(s) to display
            print("Select the VRF(s) you want to display:")
            for num, vrf in vrf_choices.items():
                print(f"{num}.) {vrf}")

            # Loop until a valid choice is made for selected VRF(s)
            while True:
                choice = input("Enter the number corresponding to your choice: ").strip()
                if choice in vrf_choices:
                    selected_vrfs = vrfs if vrf_choices[choice] == 'all' else [vrf_choices[choice]]
                    break
                elif not choice:  # If no data entered, select all routes
                    selected_vrfs = vrfs
                    break
                else:
                    print("Invalid choice. Please enter a valid number or leave it blank to select all.")

            # Loop until a valid target subnet is provided
            while True:
                target_subnet = input("Please enter the subnet you want to filter by (Note: Use CIDR or leave blank for all): ").strip()
                if not target_subnet:  # If no data entered, select all routes
                    target_subnet = None
                    break
                try:
                    ipaddress.ip_network(target_subnet, strict=False)
                    break
                except ValueError:
                    print("Invalid subnet format. Please enter a valid CIDR subnet or leave it blank.")

            # Display routes based on user input
            output = display_routes(vrf_routes, selected_vrfs, target_subnet)

            # Loop until a valid action (print or write to file) is chosen
            while True:
                action_choice = input("Do you want to print the output or write to a file? (print/file): ").strip().lower()
                if action_choice == 'print':
                    print(output)
                    break
                elif action_choice == 'file':
                    # Loop until a valid directory choice is made
                    while True:
                        directory_choice = input("Do you want to write to the current directory or specify a directory? (current/specify): ").strip().lower()
                        if directory_choice == 'current':
                            directory = os.getcwd()
                            break
                        elif directory_choice == 'specify':
                            directory = input("Please enter the directory path: ").strip()
                            if not os.path.isdir(directory):
                                print(f"Invalid directory: {directory}")
                            else:
                                break
                        else:
                            print("Invalid choice. Please enter 'current' or 'specify'.")

                    # Prompt user for the output file name
                    file_name = input("Please enter the name of the output file: ").strip()
                    output_file_path = os.path.join(directory, file_name)
                    # Write output to file
                    with open(output_file_path, 'w') as output_file:
                        output_file.write(output)
                    print(f"Output written to {output_file_path}")
                    break
                else:
                    print("Invalid choice. Please enter 'print' or 'file'.")
    except FileNotFoundError:
        print(f"File not found: {file_path}")

if __name__ == "__main__":
    main()
