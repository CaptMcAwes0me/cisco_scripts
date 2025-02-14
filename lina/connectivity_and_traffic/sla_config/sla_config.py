# Description: This script retrieves and optionally displays the SLA Configuration using 'show sla monitor configuration'.

from core.utils import get_and_parse_cli_output


def sla_config(suppress_output=False, help_requested=False):
    """
    Retrieves and optionally displays the SLA Configuration using 'show sla monitor configuration'.
    If help_requested=True, it prints the help information instead.
    """

    sla_config_help_info = {
        'command': 'show sla monitor configuration',
        'description': (
            "The 'show sla monitor configuration' command displays the configured IP SLA monitors, including "
            "their parameters, frequency, thresholds, and action settings. This command helps verify if SLA monitors "
            "are correctly configured to track network performance metrics such as latency, jitter, and reachability."
        ),
        'example_output': """
ciscoasa# show sla monitor configuration
SLA ID: 1
Type: ICMP Echo
Target address: 8.8.8.8
Data Size: 28
Timeout: 5000 ms
Threshold: 500 ms
Frequency: 10 seconds
Verify data: No
        """,
        'notes': (
            "Key fields in the output include:\n"
            "  - **SLA ID**: Identifies the SLA monitor instance.\n"
            "  - **Type**: The type of SLA probe being used (e.g., ICMP Echo, HTTP, UDP Jitter).\n"
            "  - **Target address**: The destination IP address the SLA monitor is probing.\n"
            "  - **Timeout**: Maximum time to wait for a response before declaring a failure.\n"
            "  - **Threshold**: The acceptable round-trip time before considering the connection degraded.\n"
            "  - **Frequency**: The interval at which the SLA probe runs (in seconds)."
        ),
        'related_commands': [
            {'command': 'show sla monitor operational-state', 'description': 'Displays the current status and statistics of SLA operations.'},
            {'command': 'show track', 'description': 'Shows the tracking status of objects, often used in conjunction with SLA monitors.'},
            {'command': 'debug sla monitor trace', 'description': 'Displays the progress of the SLA echo operation for troubleshooting.'},
            {'command': 'debug sla monitor error', 'description': 'Shows errors encountered by the SLA monitor process.'},
        ]
    }

    if help_requested:
        print("\n" + "-" * 80)
        print(f"📖 Help for: {sla_config_help_info['command']}".center(80))
        print("-" * 80)
        print(f"\nDescription:\n{sla_config_help_info['description']}\n")
        print("Example Output:")
        print(sla_config_help_info['example_output'])
        print("\nNotes:")
        print(sla_config_help_info['notes'])
        print("\nRelated Commands:")
        for related in sla_config_help_info['related_commands']:
            print(f"  - {related['command']}: {related['description']}")
        return None

    command = "show sla monitor configuration"

    try:
        output = get_and_parse_cli_output(command)

        if not suppress_output:
            print("\nSLA Configuration Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)

        return output

    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
