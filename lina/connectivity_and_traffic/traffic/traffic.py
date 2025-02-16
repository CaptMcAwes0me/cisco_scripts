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
    Parses 'show traffic' output and calculates 1-minute and 5-minute input/output rates.
    Detects possible traffic loops if any interface has 2x the traffic of all others combined.
    """
    input_rates_1m, input_rates_5m = {}, {}
    output_rates_1m, output_rates_5m = {}, {}

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

    # Detect possible traffic loops
    detect_traffic_loop(input_rates_1m, "input")
    detect_traffic_loop(output_rates_1m, "output")

    # Calculate total traffic
    total_input_1m = sum(v[0] for v in input_rates_1m.values())
    total_input_5m = sum(v[0] for v in input_rates_5m.values())
    total_output_1m = sum(v[0] for v in output_rates_1m.values())
    total_output_5m = sum(v[0] for v in output_rates_5m.values())

    total_input_pps_1m = sum(v[1] for v in input_rates_1m.values())
    total_input_pps_5m = sum(v[1] for v in input_rates_5m.values())
    total_output_pps_1m = sum(v[1] for v in output_rates_1m.values())
    total_output_pps_5m = sum(v[1] for v in output_rates_5m.values())

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


def detect_traffic_loop(rates, direction):
    """Detects possible traffic loops if an interface has 2x the traffic of all others combined."""
    total_traffic = sum(v[0] for v in rates.values())

    for interface, (traffic, _) in rates.items():
        other_traffic = total_traffic - traffic
        if other_traffic > 0 and traffic >= 2 * other_traffic:
            print(f"\n[⚠️ WARNING] Possible traffic loop detected on **{interface}** ({direction} traffic).")
            print(f"  - {interface} is handling {traffic} Bps, which is ≥ 2x the traffic of all other interfaces ({other_traffic} Bps).")
            print("-" * 80)

# Run the script when called
if __name__ == "__main__":
    traffic()
