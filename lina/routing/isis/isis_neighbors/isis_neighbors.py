from core.utils import get_and_parse_cli_output


def isis_neighbors(suppress_output=False, help_requested=False):
    """Retrieves and optionally displays ISIS neighbors using the 'show isis neighbors' command.
       If help_requested=True, it prints the help information instead.
    """

    isis_neighbors_help = {
        'command': 'show isis neighbors',
        'description': (
            "Displays information about ISIS neighbors, including their state, interface, and adjacency type. "
            "This command is useful for verifying ISIS adjacency formation and troubleshooting lost neighbors."
        ),
        'example_output': """
ISIS Neighbors:

System ID             Interface       State  Hold Time
1921.6800.1001.00     Gi0/1           UP     25
1921.6800.1002.00     Gi0/2           DOWN   0
        """
    }

    # If help is requested, print help content and exit the function
    if help_requested:
        print("\n" + "-" * 80)
        print(f"Help for: {isis_neighbors_help['command']}".center(80))
        print("-" * 80)
        print(f"\n{isis_neighbors_help['description']}\n")
        print("Example Output:")
        print(isis_neighbors_help['example_output'])
        return None  # No actual command execution

    # Execute the ISIS Neighbors command
    command = "show isis neighbors"
    try:
        output = get_and_parse_cli_output(command)
        if not suppress_output:
            print("\nISIS Neighbors Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)
        return output
    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
