from core.utils import get_and_parse_cli_output

def xlate_count(suppress_output=False, help_requested=False):
    """
    Retrieves and optionally displays the current and maximum number of Network Address Translation (NAT) translations using the 'show xlate count' command.
    If help_requested=True, it prints the help information instead.
    """

    xlate_count_help = {
        'command': 'show xlate count',
        'description': (
            "Displays the current and maximum number of NAT translations (xlates) through the FTD. "
            "A translation is a mapping of an internal address to an external address and can be a one-to-one mapping (NAT) or a many-to-one mapping (PAT). "
            "This command is useful for monitoring the number of active translations and assessing the load on the FTD."
        ),
        'example_output': """
84 in use, 218 most used
        """
    }

    # If help is requested, print help content and exit the function
    if help_requested:
        print("\n" + "-" * 80)
        print(f"Help for: {xlate_count_help['command']}".center(80))
        print("-" * 80)
        print(f"\n{xlate_count_help['description']}\n")
        print("Example Output:")
        print(xlate_count_help['example_output'])
        return None  # No actual command execution

    # Execute the 'show xlate count' command
    command = "show xlate count"
    try:
        output = get_and_parse_cli_output(command)
        if not suppress_output:
            print("\nXlate Count Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)
        return output
    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
