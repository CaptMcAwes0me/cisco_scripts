from core.utils import get_and_parse_cli_output


def isis_hostname(suppress_output=False, help_requested=False):
    """Retrieves and optionally displays the ISIS hostname using the 'show isis hostname' command.
       If help_requested=True, it prints the help information instead.
    """

    isis_hostname_help = {
        'command': 'show isis hostname',
        'description': (
            "Displays the hostnames assigned to ISIS system IDs. This command helps in mapping system IDs "
            "to human-readable names, making it easier to interpret ISIS neighbor relationships and topology."
        ),
        'example_output': """
ISIS Hostname Mapping:

System ID             Hostname
1921.6800.1001.00     R1
1921.6800.1002.00     R2
1921.6800.1003.00     R3
        """
    }

    # If help is requested, print help content and exit the function
    if help_requested:
        print("\n" + "-" * 80)
        print(f"Help for: {isis_hostname_help['command']}".center(80))
        print("-" * 80)
        print(f"\n{isis_hostname_help['description']}\n")
        print("Example Output:")
        print(isis_hostname_help['example_output'])
        return None  # No actual command execution

    # Execute the ISIS Hostname command
    command = "show isis hostname"
    try:
        output = get_and_parse_cli_output(command)
        if not suppress_output:
            print("\nISIS Hostname Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)
        return output
    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
