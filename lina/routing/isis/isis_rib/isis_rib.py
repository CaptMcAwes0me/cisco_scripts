from core.utils import get_and_parse_cli_output


def isis_rib(suppress_output=False, help_requested=False):
    """Retrieves and optionally displays the ISIS Routing Information Base (RIB) using the 'show isis rib' command.
       If help_requested=True, it prints the help information instead.
    """

    isis_rib_help = {
        'command': 'show isis rib',
        'description': (
            "Displays the ISIS Routing Information Base (RIB), showing routes learned via ISIS, "
            "including prefixes, next-hop addresses, metric values, and interface details. This command "
            "is useful for verifying ISIS route installation and troubleshooting forwarding issues."
        ),
        'example_output': """
ISIS RIB:

Prefix              Next Hop          Interface        Metric
10.1.1.0/24        192.168.1.2       GigabitEthernet0/1  10
10.2.2.0/24        192.168.1.3       GigabitEthernet0/2  20
        """
    }

    # If help is requested, print help content and exit the function
    if help_requested:
        print("\n" + "-" * 80)
        print(f"Help for: {isis_rib_help['command']}".center(80))
        print("-" * 80)
        print(f"\n{isis_rib_help['description']}\n")
        print("Example Output:")
        print(isis_rib_help['example_output'])
        return None  # No actual command execution

    # Execute the ISIS RIB command
    command = "show isis rib"
    try:
        output = get_and_parse_cli_output(command)
        if not suppress_output:
            print("\nISIS RIB Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)
        return output
    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
