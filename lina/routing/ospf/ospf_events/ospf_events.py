from core.utils import get_and_parse_cli_output

def ospf_events(suppress_output=False, help_requested=False):
    """Retrieves and optionally displays OSPF events using the 'show ospf events' command.
       If help_requested=True, it prints the help information instead.
    """

    ospf_events_help = {
        'command': 'show ospf events',
        'description': (
            "Displays a log of significant OSPF events, such as adjacency changes, SPF recalculations, "
            "and route updates. This command is useful for monitoring OSPF stability and troubleshooting "
            "unexpected topology changes."
        ),
        'example_output': """
OSPF Event Log for Process ID 1

Timestamp       Event Type            Router ID     Interface       Description
12:45:33.123    Neighbor Up           192.168.1.2   Gi0/1           FULL state reached
12:45:36.456    SPF Calculation       192.168.1.1   -               New route installed
12:50:10.789    Neighbor Down         192.168.1.3   Gi0/2           Dead timer expired
        """
    }

    # If help is requested, print help content and exit the function
    if help_requested:
        print("\n" + "-" * 80)
        print(f"Help for: {ospf_events_help['command']}".center(80))
        print("-" * 80)
        print(f"\n{ospf_events_help['description']}\n")
        print("Example Output:")
        print(ospf_events_help['example_output'])
        return None  # No actual command execution

    # Execute the OSPF Events command
    command = "show ospf events"
    try:
        output = get_and_parse_cli_output(command)
        if not suppress_output:
            print("\nOSPF Events Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)
        return output
    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
