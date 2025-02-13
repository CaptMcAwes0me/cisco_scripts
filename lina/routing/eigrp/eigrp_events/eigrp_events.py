# Description: This script retrieves and displays EIGRP events using the 'show eigrp events' command.

from core.utils import get_and_parse_cli_output


def eigrp_events(suppress_output=False, help_requested=False):
    """Retrieves and optionally displays EIGRP events using the 'show eigrp events' command.
       If help_requested=True, it prints the help information instead.
    """

    eigrp_events_help = {
        'command': 'show eigrp events',
        'description': (
            "Displays a log of significant EIGRP events, such as neighbor adjacency changes, route recalculations, "
            "and topology updates. Useful for troubleshooting EIGRP stability issues."
        ),
        'example_output': """
EIGRP event log for process 100

Timestamp       Event Type          Neighbor       Interface
12:45:33.123    Neighbor Up         192.168.1.2   Gi0/1
12:45:36.456    Route Installed     10.10.10.0/24
12:50:10.789    Neighbor Down       192.168.1.2   Gi0/1
        """
    }

    # If help is requested, print help content and exit the function
    if help_requested:
        print("\n" + "-" * 80)
        print(f"Help for: {eigrp_events_help['command']}".center(80))
        print("-" * 80)
        print(f"\n{eigrp_events_help['description']}\n")
        print("Example Output:")
        print(eigrp_events_help['example_output'])
        return None  # No actual command execution

    # Execute the EIGRP Events command
    command = "show eigrp events"

    try:
        output = get_and_parse_cli_output(command)

        # Conditionally print the output
        if not suppress_output:
            print("\nEIGRP Events Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)

        return output

    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
