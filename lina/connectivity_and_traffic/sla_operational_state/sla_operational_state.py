# Description: This script retrieves and optionally displays the SLA Operational State using 'show sla monitor operational-state'.

from core.utils import get_and_parse_cli_output

def sla_operational_state(suppress_output=False, help_requested=False):
    """
    Retrieves and optionally displays the SLA Operational State using 'show sla monitor operational-state'.
    If help_requested=True, it prints the help information instead.
    """

    sla_help_info = {
        'command': 'show sla monitor operational-state',
        'description': (
            "The 'show sla monitor operational-state' command displays the current operational statistics of "
            "configured IP Service Level Agreements (SLAs) on the FTD. This includes details such as the number "
            "of operations attempted, success and failure counts, round-trip time (RTT) statistics, and the overall "
            "operational state of each SLA monitor."
        ),
        'example_output': """
firepower# show sla monitor operational-state
Entry number: 1
Modification time: 15:49:47.686 UTC Sat Jun 1 2013
Number of Octets Used by this Entry: 1480
Number of operations attempted: 6
Number of operations skipped: 0
Current seconds left in Life: Forever
Operational state of entry: Active
Last time this entry was reset: Never
Connection loss occurred: FALSE
Timeout occurred: FALSE
Over thresholds occurred: FALSE
Latest RTT (milliseconds): 10
Latest operation start time: 15:54:47.702 UTC Sat Jun 1 2013
Latest operation return code: OK
RTT Values:
  RTTAvg: 10       RTTMin: 10       RTTMax: 10
  NumOfRTT: 1      RTTSum: 10       RTTSum2: 100
        """,
        'notes': (
            "Key fields in the output include:\n"
            "  - **Entry number**: Identifier for the SLA monitor.\n"
            "  - **Operational state of entry**: Indicates if the SLA monitor is currently active or inactive.\n"
            "  - **Latest RTT (milliseconds)**: The most recent round-trip time measurement.\n"
            "  - **Latest operation return code**: Result of the latest SLA operation (e.g., OK, Timeout).\n"
            "  - **RTT Values**: Statistics on round-trip times, including average, minimum, and maximum values."
        ),
        'related_commands': [
            {'command': 'show sla monitor configuration', 'description': 'Displays the configuration settings of the SLA monitor.'},
            {'command': 'show track', 'description': 'Shows the tracking status of objects, often used in conjunction with SLA monitors.'},
        ]
    }

    if help_requested:
        print("\n" + "-" * 80)
        print(f"📖 Help for: {sla_help_info['command']}".center(80))
        print("-" * 80)
        print(f"\nDescription:\n{sla_help_info['description']}\n")
        print("Example Output:")
        print(sla_help_info['example_output'])
        print("\nNotes:")
        print(sla_help_info['notes'])
        print("\nRelated Commands:")
        for related in sla_help_info['related_commands']:
            print(f"  - {related['command']}: {related['description']}")
        return None

    command = "show sla monitor operational-state"

    try:
        output = get_and_parse_cli_output(command)

        if not suppress_output:
            print("\nSLA Operational State Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)

        return output

    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
