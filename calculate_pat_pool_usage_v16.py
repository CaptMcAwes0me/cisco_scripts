'''

Legal Disclaimer:

This script is provided for educational and informational purposes only. The author (programmer) makes no representations or warranties of any kind, express or implied, about the completeness, accuracy, reliability, suitability, or availability with respect to the script or the information, products, services, or related graphics contained in the script for any purpose. Any reliance you place on such information is therefore strictly at your own risk.

In no event will the author be liable for any loss or damage including without limitation, indirect or consequential loss or damage, or any loss or damage whatsoever arising from loss of data or profits arising out of or in connection with the use of this script.

By using this script, you agree that you are solely responsible for any consequences that may arise from its use. The author disclaims any responsibility for any actions taken by users of this script.

Usage of this script constitutes acceptance of these terms and conditions.

Authored by Garrett McCollum - Cisco Systems Inc. (2024)

'''

import os

def parse_units(file_path):
    with open(file_path, 'r') as file:
        content = file.readlines()

    units = []
    current_unit = None
    for line in content:
        if line.startswith("unit-"):
            if current_unit:
                units.append(current_unit)
            current_unit = {'name': line.strip(), 'data': []}
        elif current_unit is not None:
            current_unit['data'].append(line.strip())

    # Append the last unit after loop finishes
    if current_unit:
        units.append(current_unit)

    return units

def count_allocated_ports_per_ip(unit_data):
    ip_allocations = {}
    total_allocated_ports = {'TCP': 0, 'UDP': 0, 'ICMP': 0}

    for line in unit_data:
        if "allocated" in line:
            parts = line.split(", ")
            protocol = parts[0].split(" ")[0]  # Extracting the protocol (TCP/UDP/ICMP)
            ip_address = parts[1].split(" ")[-1]  # Extracting the IP address
            allocated_part = parts[-1].split(" ")[-1]  # Extract the allocated part
            # Check if the allocated part contains only digits
            if allocated_part.isdigit():
                allocated = int(allocated_part)
                if ip_address not in ip_allocations:
                    ip_allocations[ip_address] = {'TCP': 0, 'UDP': 0, 'ICMP': 0}
                ip_allocations[ip_address][protocol] += allocated
                total_allocated_ports[protocol] += allocated

    return ip_allocations, total_allocated_ports

def print_boxed_message(message):
    lines = message.split('\n')
    box_width = len(max(lines, key=len)) + 4
    print("┌" + "─" * (box_width - 2) + "┐")
    for line in lines:
        padding = (box_width - len(line) - 4) // 2
        print("│ " + " " * padding + line + " " * (box_width - len(line) - 4 - padding) + " │")
    print("└" + "─" * (box_width - 2) + "┘")

def format_output(units, num_of_units, threshold):
    output = []
    threshold_exceed_output = []
    total_ports = 65535 - 1024  # Total possible ports for TCP and UDP
    max_ports_per_unit = total_ports / num_of_units

    for unit in units:
        output.append(f"Unit: {unit['name']}")
        ip_allocations, total_allocated_ports = count_allocated_ports_per_ip(unit['data'])
        output.append("┌────────────────┬─────────────────────┬───────────────────────────────┬─────────────────────┬───────────────────────────────┬─────────────────────┬───────────────────────────────┐")
        output.append("│ IP Address     │ TCP Allocated ports │ Percentage of TCP allocation  │ UDP Allocated ports │ Percentage of UDP allocation  │ ICMP Allocated ports│ Percentage of ICMP allocation │")
        output.append("├────────────────┼─────────────────────┼───────────────────────────────┼─────────────────────┼───────────────────────────────┼─────────────────────┼───────────────────────────────┤")

        threshold_exceed_output.append(f"Threshold Exceedances for Unit: {unit['name']}")
        threshold_exceed_output.append("┌────────────────┬─────────────────────┬───────────────────────────────┬─────────────────────┬───────────────────────────────┬─────────────────────┬───────────────────────────────┐")
        threshold_exceed_output.append("│ IP Address     │ TCP Allocated ports │ Percentage of TCP allocation  │ UDP Allocated ports │ Percentage of UDP allocation  │ ICMP Allocated ports│ Percentage of ICMP allocation │")
        threshold_exceed_output.append("├────────────────┼─────────────────────┼───────────────────────────────┼─────────────────────┼───────────────────────────────┼─────────────────────┼───────────────────────────────┤")

        # Sorting IP addresses based on the total allocations
        sorted_ip_allocations = sorted(ip_allocations.items(), key=lambda x: sum(x[1].values()), reverse=True)

        for ip, allocations in sorted_ip_allocations:
            tcp_percentage = (allocations['TCP'] / max_ports_per_unit) * 100 if max_ports_per_unit else 0
            udp_percentage = (allocations['UDP'] / max_ports_per_unit) * 100 if max_ports_per_unit else 0
            icmp_percentage = (allocations['ICMP'] / 65535) * 100 if 65535 else 0

            output.append(f"│ {ip:<14} │ {allocations['TCP']:<19} │ {tcp_percentage:<27.2f}%  │ {allocations['UDP']:<19} │ {udp_percentage:<27.2f}%  │ {allocations['ICMP']:<19} │ {icmp_percentage:<27.2f}%  │")
            
            if tcp_percentage > threshold or udp_percentage > threshold or icmp_percentage > threshold:
                threshold_exceed_output.append(f"│ {ip:<14} │ {allocations['TCP']:<19} │ {tcp_percentage:<27.2f}%  │ {allocations['UDP']:<19} │ {udp_percentage:<27.2f}%  │ {allocations['ICMP']:<19} │ {icmp_percentage:<27.2f}% │")
        
        output.append("└────────────────┴─────────────────────┴───────────────────────────────┴─────────────────────┴───────────────────────────────┴─────────────────────┴───────────────────────────────┘")
        output.append("")  # Add an empty line for better readability

        threshold_exceed_output.append("└────────────────┴─────────────────────┴───────────────────────────────┴─────────────────────┴───────────────────────────────┴─────────────────────┴───────────────────────────────┘")
        threshold_exceed_output.append("")  # Add an empty line for better readability

    return output, threshold_exceed_output

def get_choice(prompt, choices):
    while True:
        choice = input(prompt).strip().lower()
        if choice in choices:
            return choice
        print(f"Invalid choice. Please enter one of {choices}.")

def main():
    disclaimer = "!!!! DISCLAIMER !!!!!\nThis script will provide accurate data if the 'cluster-member-limit' matches that of the total amount of units in the cluster,\nor if single unit cluster it will account for half the ports being reserved.\nIf not, then the data output may be unreliable.\n\nNote: This script does not support extended, flat, include-reserve, etc."
    print_boxed_message(disclaimer)

    while True:
        file_path = input("Enter the path of the file of 'cluster exec show nat pool': ")
        if os.path.exists(file_path):
            break
        else:
            print("Invalid file path. Please enter a valid file path.")

    units = parse_units(file_path)

    num_of_units = len(units)
    if num_of_units == 1:
        num_of_units = 2

    while True:
        try:
            threshold = float(input("Enter the threshold percentage (70-99): "))
            if 70 <= threshold <= 99:
                break
            else:
                print("Invalid threshold. Please enter a value between 70 and 99.")
        except ValueError:
            print("Invalid input. Please enter a numeric value between 70 and 99.")

    output, threshold_exceed_output = format_output(units, num_of_units, threshold)

    choice = get_choice("Do you want to print the output to the screen or write to a file? (print/file): ", ['print', 'file'])

    if choice == 'file':
        dir_choice = get_choice("Do you want to save the file to the current directory or specify a directory? (current/specify): ", ['current', 'specify'])
        if dir_choice == 'current':
            output_dir = os.getcwd()
        elif dir_choice == 'specify':
            while True:
                output_dir = input("Enter the directory path: ")
                if os.path.exists(output_dir):
                    break
                else:
                    print("Invalid directory path. Please enter a valid directory path.")
        
        file_name = input("Enter the file name: ")
        output_file = os.path.join(output_dir, file_name)

        with open(output_file, 'w') as file:
            file.write("\n".join(output))
            file.write("\n\nThreshold Exceedances:\n")
            file.write("\n".join(threshold_exceed_output))
        print(f"Output written to {output_file}")
    elif choice == 'print':
        for line in output:
            print(line)
        print("\nThreshold Exceedances:\n")
        for line in threshold_exceed_output:
            print(line)

if __name__ == "__main__":
    main()
