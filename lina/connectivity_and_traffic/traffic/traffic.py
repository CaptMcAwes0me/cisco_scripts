# Description: This script retrieves and optionally displays the Traffic statistics using 'show traffic'.

from core.utils import get_and_parse_cli_output


def traffic(suppress_output=False, help_requested=False):
    """
    Retrieves and optionally displays Traffic statistics using 'show traffic'.
    If help_requested=True, it prints the help information instead.
    """

    traffic_help_info = {
        'command': 'show traffic',
        'description': (
            "The 'show traffic' command provides real-time traffic statistics for all interfaces on the ASA, "
            "including input/output rates, packet counts, and protocol-level breakdowns. This is useful for "
            "monitoring network utilization and identifying potential congestion points."
        ),
        'example_output': """
ciscoasa# show traffic
Interface outside:
  Received:  500000 packets, 400000000 bytes
  Transmitted:  750000 packets, 600000000 bytes
  Input rate: 500 kbps, 1000 pps
  Output rate: 750 kbps, 1500 pps

Interface inside:
  Received:  200000 packets, 150000000 bytes
  Transmitted:  350000 packets, 250000000 bytes
  Input rate: 250 kbps, 500 pps
  Output rate: 400 kbps, 900 pps
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
            {'command': 'show interface', 'description': 'Provides detailed statistics on ASA interfaces, including errors.'},
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

        if not suppress_output:
            print("\nTraffic Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)

        return output

    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
