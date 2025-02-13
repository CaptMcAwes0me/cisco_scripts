from core.utils import get_and_parse_cli_output


def isis_topology(suppress_output=False, help_requested=False):
    """Retrieves and optionally displays the ISIS topology using the 'show isis topology' command.
       If help_requested=True, it prints the help information instead.
    """

    isis_topology_help = {
        'command': 'show isis topology',
        'description': (
            "Displays the ISIS network topology, including routers, links, and adjacencies. "
            "This command is useful for verifying the overall ISIS structure and ensuring proper connectivity."
        ),
        'example_output': """
ISIS Topology:

System ID             Interface       Level   Metric   State
1921.6800.1001.00     Gi0/1           L2      10       Up
1921.6800.1002.00     Gi0/2           L2      20       Up
1921.6800.1003.00     Gi0/3           L1      30       Up
        """
    }

    # If help is requested, print help content and exit the function
    if help_requested:
        print("\n" + "-" * 80)
        print(f"Help for: {isis_topology_help['command']}".center(80))
        print("-" * 80)
        print(f"\n{isis_topology_help['description']}\n")
        print("Example Output:")
        print(isis_topology_help['example_output'])
        return None  # No actual command execution

    # Execute the ISIS Topology command
    command = "show isis topology"
    try:
        output = get_and_parse_cli_output(command)
        if not suppress_output:
            print("\nISIS Topology Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)
        return output
    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
