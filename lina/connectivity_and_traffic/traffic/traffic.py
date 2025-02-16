import re
from core.utils import get_and_parse_cli_output, traffic_table, convert_bps_to_readable


def traffic():
    """
    Retrieves 'show traffic' output and passes it to traffic_calc for processing.
    """
    command = "show traffic"
    try:
        output = get_and_parse_cli_output(command)
        return traffic_calc(output)  # Pass output to calculation function
    except Exception as e:
        print(f"[!] Error retrieving traffic data: {e}")
        return None


def traffic_calc(output):
    """
    Parses the traffic output and calculates 1-minute and 5-minute input/output rates.
    Detects possible traffic loops if any interface has 2x the traffic of all others combined.
    """
    input_rates_1m = {}
    input_rates_5m = {}
    output_rates_1m = {}
    output_rates_5m = {}

    lines = output.splitlines()
    interface = None
    stop_processing = False

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
                input_rates_1m[interface] = int(values[0][1])  # Bytes per second

        elif "1 minute output rate" in line and interface:
            values = re.findall(r'(\d+) pkts/sec, *(\d+) bytes/sec', line)
            if values:
                output_rates_1m[interface] = int(values[0][1])  # Bytes per second

        elif "5 minute input rate" in line and interface:
            values = re.findall(r'(\d+) pkts/sec, *(\d+) bytes/sec', line)
            if values:
                input_rates_5m[interface] = int(values[0][1])  # Bytes per second

        elif "5 minute output rate" in line and interface:
            values = re.findall(r'(\d+) pkts/sec, *(\d+) bytes/sec', line)
            if values:
                output_rates_5m[interface] = int(values[0][1])  # Bytes per second

    # Check for possible traffic loops
    detect_traffic_loop(input_rates_1m, "input")
    detect_traffic_loop(output_rates_1m, "output")

    # Calculate total traffic for all interfaces
    total_input_1m = sum(input_rates_1m.values())
    total_input_5m = sum(input_rates_5m.values())
    total_output_1m = sum(output_rates_1m.values())
    total_output_5m = sum(output_rates_5m.values())

    # Print Total Row Separately
    print("\nTOTAL TRAFFIC SUMMARY:")
    traffic_table(["Traffic Type", "1-Min Total (Bps)", "5-Min Total (Bps)"], [
        ["Total", total_input_1m, total_input_5m]
    ])

    # Total bandwidth usage table
    print("\nTOTAL BANDWIDTH USAGE:")
    traffic_table(["Traffic Type", "1-Min Bandwidth (Bps)", "5-Min Bandwidth (Bps)"], [
        ["Input", convert_bps_to_readable(total_input_1m), convert_bps_to_readable(total_input_5m)],
        ["Output", convert_bps_to_readable(total_output_1m), convert_bps_to_readable(total_output_5m)]
    ])

    print("\n**Bandwidth Usage Calculation**:")
    print("  - Formula: (Total Bytes * 8) / 1024")
    print(f"  - 1-Min Input: ({total_input_1m} * 8) / 1024 = {convert_bps_to_readable(total_input_1m)}")
    print(f"  - 5-Min Input: ({total_input_5m} * 8) / 1024 = {convert_bps_to_readable(total_input_5m)}")
    print(f"  - 1-Min Output: ({total_output_1m} * 8) / 1024 = {convert_bps_to_readable(total_output_1m)}")
    print(f"  - 5-Min Output: ({total_output_5m} * 8) / 1024 = {convert_bps_to_readable(total_output_5m)}")

    # Print Average Packet Size Table
    print("\nAVERAGE PACKET SIZE:")
    traffic_table(["Traffic Type", "1-Min Avg Packet (bytes)", "5-Min Avg Packet (bytes)"], [
        ["Input", total_input_1m // sum(input_rates_1m.values()) if sum(input_rates_1m.values()) else 0,
                  total_input_5m // sum(input_rates_5m.values()) if sum(input_rates_5m.values()) else 0],
        ["Output", total_output_1m // sum(output_rates_1m.values()) if sum(output_rates_1m.values()) else 0,
                   total_output_5m // sum(output_rates_5m.values()) if sum(output_rates_5m.values()) else 0]
    ])

    print("\n**Packet Size Calculation**:")
    print("  - Formula: (Total Bytes) / (Total Packets)")
    print(f"  - 1-Min Input: ({total_input_1m} / {sum(input_rates_1m.values())}) = {total_input_1m // sum(input_rates_1m.values()) if sum(input_rates_1m.values()) else 0} bytes")
    print(f"  - 1-Min Output: ({total_output_1m} / {sum(output_rates_1m.values())}) = {total_output_1m // sum(output_rates_1m.values()) if sum(output_rates_1m.values()) else 0} bytes")


def detect_traffic_loop(rates, direction):
    """
    Detects possible traffic loops in the given input/output rate dictionary.
    If any interface has 2x the cumulative traffic of all others combined, issue a warning.
    """
    total_traffic = sum(rates.values())

    for interface, traffic in rates.items():
        other_traffic = total_traffic - traffic  # Traffic of all other interfaces
        if other_traffic > 0 and traffic >= 2 * other_traffic:
            print(f"\n[⚠️ WARNING] Possible traffic loop detected on **{interface}** ({direction} traffic).")
            print(f"  - {interface} is handling {traffic} Bps, which is ≥ 2x the traffic of all other interfaces ({other_traffic} Bps).")
            print("  - Check for network loops, spanning-tree issues, or incorrect configurations.")
            print("-" * 80)
