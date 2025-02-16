import re
from core.utils import get_and_parse_cli_output, traffic_table, convert_bps_to_readable


def traffic_dump(suppress_output=False):
    """
    Retrieves 'show traffic' output and prints it for traffic dump.
    """
    command = "show traffic"
    try:
        output = get_and_parse_cli_output(command)

        if not suppress_output:
            print("\nShow Traffic Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)

        return output

    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message


def traffic(help_requested=False):
    """
    Retrieves 'show traffic' output and passes it to traffic_calc for processing.
    """

    traffic_help_info = {
        'command': 'show traffic',
        'description': (
            "The 'show traffic' command provides real-time traffic statistics for all interfaces on the FTD, "
            "including input/output rates, packet counts, and protocol-level breakdowns. This is useful for "
            "monitoring network utilization and identifying potential congestion points."
        ),
        'example_output': """
    firepower# show traffic
    outside:
	    received (in 182383.660 secs):
		    142396064 packets	37156955209 bytes
		    3 pkts/sec	203023 bytes/sec
	    transmitted (in 182383.660 secs):
		    4669761 packets	135571422 bytes
		    2 pkts/sec	13 bytes/sec
        1 minute input rate 722 pkts/sec,  201563 bytes/sec
        1 minute output rate 0 pkts/sec,  35 bytes/sec
        1 minute drop rate, 599 pkts/sec
        5 minute input rate 5633 pkts/sec,  336869 bytes/sec
        5 minute output rate 4496 pkts/sec,  125937 bytes/sec
        5 minute drop rate, 1018 pkts/sec
        """,
        'notes': (
            "Key fields in the output include:\n"
            "  - **Interface**: The network interface where traffic is measured.\n"
            "  - **Received/Transmitted Packets & Bytes**: Shows the total traffic processed per interface.\n"
            "  - **Input/Output Rate**: Displays the real-time data transfer rate in kbps and packets per second (pps).\n"
            "  - **Protocol-level breakdown**: Shows traffic statistics per protocol (not included in this example)."
        ),
        'related_commands': [
            {'command': 'show conn count', 'description': 'Displays the number of active connections.'},
            {'command': 'show xlate', 'description': 'Shows NAT translations and statistics.'},
            {'command': 'show interface',
             'description': 'Provides detailed statistics on FTD interfaces, including errors.'},
            {'command': 'show service-policy', 'description': 'Displays how traffic is affected by service policies.'},
        ]
    }

    if help_requested:
        print("\n" + "-" * 80)
        print(f"📖 Help for: {traffic_help_info['command']}".center(80))
        print("-" * 80)
        print(f"\nDescription:\n{traffic_help_info['description']}\n")
        print("Example Output:")
        print(traffic_help_info['example_output'])
        print("\nNotes:")
        print(traffic_help_info['notes'])
        print("\nRelated Commands:")
        for related in traffic_help_info['related_commands']:
            print(f"  - {related['command']}: {related['description']}")
        return None

    command = "show traffic"
    try:
        output = get_and_parse_cli_output(command)
        return traffic_calc(output)  # Pass output to calculation function
    except Exception as e:
        print(f"[!] Error retrieving traffic data: {e}")
        return None


def traffic_calc(output):
    """
    Parses 'show traffic' output and calculates 1-minute and 5-minute input/output rates.
    Detects possible traffic loops if any interface has 2x the traffic of all others combined.
    """
    input_rates_1m, input_rates_5m = {}, {}
    output_rates_1m, output_rates_5m = {}, {}

    lines = output.splitlines()
    interface = None
    stop_processing = False
    loop_warnings = []  # Store loop detection warnings to print them last

    for line in lines:
        line = line.strip()

        # Stop processing when "Physical Interface" appears
        if "Physical Interface" in line:
            stop_processing = True
            continue

        if stop_processing:
            continue  # Ignore everything after "Physical Interface"

        # Detect interface names
        if re.match(r'^\S+:$', line):  # Matches 'outside:', 'inside:', etc.
            interface = line[:-1]  # Remove the trailing colon (:)

        elif "1 minute input rate" in line and interface:
            values = re.findall(r'(\d+) pkts/sec, *(\d+) bytes/sec', line)
            if values:
                input_rates_1m[interface] = [int(values[0][1]), int(values[0][0])]  # [bps, pps]

        elif "1 minute output rate" in line and interface:
            values = re.findall(r'(\d+) pkts/sec, *(\d+) bytes/sec', line)
            if values:
                output_rates_1m[interface] = [int(values[0][1]), int(values[0][0])]  # [bps, pps]

        elif "5 minute input rate" in line and interface:
            values = re.findall(r'(\d+) pkts/sec, *(\d+) bytes/sec', line)
            if values:
                input_rates_5m[interface] = [int(values[0][1]), int(values[0][0])]  # [bps, pps]

        elif "5 minute output rate" in line and interface:
            values = re.findall(r'(\d+) pkts/sec, *(\d+) bytes/sec', line)
            if values:
                output_rates_5m[interface] = [int(values[0][1]), int(values[0][0])]  # [bps, pps]

    # Detect possible traffic loops (store warnings for later)
    loop_warnings += detect_traffic_loop(input_rates_1m, "input")
    loop_warnings += detect_traffic_loop(output_rates_1m, "output")

    # Calculate total traffic
    total_input_1m, total_input_5m = sum(v[0] for v in input_rates_1m.values()), sum(v[0] for v in input_rates_5m.values())
    total_output_1m, total_output_5m = sum(v[0] for v in output_rates_1m.values()), sum(v[0] for v in output_rates_5m.values())

    total_input_pps_1m, total_input_pps_5m = sum(v[1] for v in input_rates_1m.values()), sum(v[1] for v in input_rates_5m.values())
    total_output_pps_1m, total_output_pps_5m = sum(v[1] for v in output_rates_1m.values()), sum(v[1] for v in output_rates_5m.values())

    # Print tables
    print("\nINPUT TRAFFIC RATES:")
    traffic_table(["Interface", "1-Min Input (Bps)", "1-Min Input (pps)", "5-Min Input (Bps)", "5-Min Input (pps)"],
                  [[iface] + input_rates_1m.get(iface, [0, 0]) + input_rates_5m.get(iface, [0, 0]) for iface in input_rates_1m])

    print("\nOUTPUT TRAFFIC RATES:")
    traffic_table(["Interface", "1-Min Output (Bps)", "1-Min Output (pps)", "5-Min Output (Bps)", "5-Min Output (pps)"],
                  [[iface] + output_rates_1m.get(iface, [0, 0]) + output_rates_5m.get(iface, [0, 0]) for iface in output_rates_1m])

    # Print Total Summary
    print("\nTOTAL TRAFFIC SUMMARY:")
    traffic_table(["Traffic Type", "1-Min Total (Bps)", "1-Min Total (pps)", "5-Min Total (Bps)", "5-Min Total (pps)"],
                  [["Total", total_input_1m + total_output_1m, total_input_pps_1m + total_output_pps_1m,
                    total_input_5m + total_output_5m, total_input_pps_5m + total_output_pps_5m]])

    # Print Bandwidth Usage
    print("\nTOTAL BANDWIDTH USAGE:")
    traffic_table(["Traffic Type", "1-Min Bandwidth", "5-Min Bandwidth"],
                  [["Input", convert_bps_to_readable(total_input_1m), convert_bps_to_readable(total_input_5m)],
                   ["Output", convert_bps_to_readable(total_output_1m), convert_bps_to_readable(total_output_5m)]])

    # Print Bandwidth Calculation
    print("\n**Bandwidth Usage Calculation**:")
    print("  - Formula: (Total Bytes * 8) / 1024")
    print(f"  - Example: ( {total_input_1m} * 8) / 1024 = {convert_bps_to_readable(total_input_1m)}")

    # Print Average Packet Size
    print("\nAVERAGE PACKET SIZE:")
    traffic_table(["Traffic Type", "1-Min Avg Packet (bytes)", "5-Min Avg Packet (bytes)"],
                  [["Input", total_input_1m // total_input_pps_1m if total_input_pps_1m else 0,
                            total_input_5m // total_input_pps_5m if total_input_pps_5m else 0],
                   ["Output", total_output_1m // total_output_pps_1m if total_output_pps_1m else 0,
                             total_output_5m // total_output_pps_5m if total_output_pps_5m else 0]])

    print("\n**Packet Size Calculation**:")
    print("  - Formula: (Total Bytes) / (Total Packets)")
    print(f"  - Example: ( {total_input_1m} / {total_input_pps_1m} ) = {total_input_1m // total_input_pps_1m if total_input_pps_1m else 0} bytes")

    # Print Loop Detection Warnings (LAST)
    if loop_warnings:
        print("\nTRAFFIC LOOP DETECTION WARNINGS:")
        for warning in loop_warnings:
            print(warning)


def detect_traffic_loop(rates, direction):
    """Detects possible traffic loops if an interface has 2x the traffic of all others combined."""
    warnings = []
    total_traffic = sum(v[0] for v in rates.values())

    for interface, (traffic, _) in rates.items():
        other_traffic = total_traffic - traffic
        if other_traffic > 0 and traffic >= 2 * other_traffic:
            warnings.append(f"⚠️ WARNING - Possible traffic loop detected on **{interface}** ({direction} traffic) - WARNING ⚠️")
            warnings.append(f"  - {interface} is handling {traffic} Bps, which is ≥ 2x the traffic of all other interfaces ({other_traffic} Bps).")
            warnings.append("-" * 80)

    return warnings  # Return warnings to be printed later
