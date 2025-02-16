import re
from core.utils import get_and_parse_cli_output

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
    Returns structured data for printing in a CLI table.
    """
    input_rates_1m = {}
    input_rates_5m = {}
    output_rates_1m = {}
    output_rates_5m = {}

    lines = output.splitlines()
    interface = None

    for line in lines:
        line = line.strip()

        # Detect interface names
        if re.match(r'^\S+:$', line):  # Matches 'outside:', 'inside:', etc.
            interface = line[:-1]  # Remove the trailing colon (:)

        elif "1 minute input rate" in line and interface:
            values = re.findall(r'(\d+) pkts/sec, *(\d+) bytes/sec', line)
            if values:
                input_rates_1m[interface] = (int(values[0][1]), int(values[0][0]))  # (bps, pps)

        elif "1 minute output rate" in line and interface:
            values = re.findall(r'(\d+) pkts/sec, *(\d+) bytes/sec', line)
            if values:
                output_rates_1m[interface] = (int(values[0][1]), int(values[0][0]))  # (bps, pps)

        elif "5 minute input rate" in line and interface:
            values = re.findall(r'(\d+) pkts/sec, *(\d+) bytes/sec', line)
            if values:
                input_rates_5m[interface] = (int(values[0][1]), int(values[0][0]))  # (bps, pps)

        elif "5 minute output rate" in line and interface:
            values = re.findall(r'(\d+) pkts/sec, *(\d+) bytes/sec', line)
            if values:
                output_rates_5m[interface] = (int(values[0][1]), int(values[0][0]))  # (bps, pps)

    # Convert dictionaries to list format for table function
    input_table_data = []
    output_table_data = []
    total_input_1m, total_input_5m, total_input_pps_1m, total_input_pps_5m = 0, 0, 0, 0
    total_output_1m, total_output_5m, total_output_pps_1m, total_output_pps_5m = 0, 0, 0, 0

    for interface in sorted(input_rates_1m.keys() | output_rates_1m.keys()):  # Include all interfaces
        in_1m_bps, in_1m_pps = input_rates_1m.get(interface, (0, 0))
        in_5m_bps, in_5m_pps = input_rates_5m.get(interface, (0, 0))
        out_1m_bps, out_1m_pps = output_rates_1m.get(interface, (0, 0))
        out_5m_bps, out_5m_pps = output_rates_5m.get(interface, (0, 0))

        # Accumulate totals
        total_input_1m += in_1m_bps
        total_input_pps_1m += in_1m_pps
        total_input_5m += in_5m_bps
        total_input_pps_5m += in_5m_pps

        total_output_1m += out_1m_bps
        total_output_pps_1m += out_1m_pps
        total_output_5m += out_5m_bps
        total_output_pps_5m += out_5m_pps

        input_table_data.append([interface, in_1m_bps, in_1m_pps, in_5m_bps, in_5m_pps])
        output_table_data.append([interface, out_1m_bps, out_1m_pps, out_5m_bps, out_5m_pps])

    # Add total row
    input_table_data.append(["**Total**", total_input_1m, total_input_pps_1m, total_input_5m, total_input_pps_5m])
    output_table_data.append(["**Total**", total_output_1m, total_output_pps_1m, total_output_5m, total_output_pps_5m])

    # Define headers
    input_headers = ["Interface", "1-Min Input (bps)", "1-Min Input (pps)", "5-Min Input (bps)", "5-Min Input (pps)"]
    output_headers = ["Interface", "1-Min Output (bps)", "1-Min Output (pps)", "5-Min Output (bps)", "5-Min Output (pps)"]

    # Print tables
    print("\nINPUT TRAFFIC RATES:")
    traffic_table(input_headers, input_table_data)
    print("\nOUTPUT TRAFFIC RATES:")
    traffic_table(output_headers, output_table_data)


def traffic_table(headers, data):
    """
    Prints a well-formatted CLI table using only native Python libraries.
    """
    col_widths = [max(len(str(item)) for item in col) for col in zip(headers, *data)]

    format_str = " | ".join(f"{{:<{w}}}" for w in col_widths)
    border = "-+-".join("-" * w for w in col_widths)

    print(border)
    print(format_str.format(*headers))
    print(border)
    for row in data:
        print(format_str.format(*row))
    print(border)


# Run the script when called
if __name__ == "__main__":
    traffic()
