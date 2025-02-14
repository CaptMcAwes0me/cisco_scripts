from core.utils import get_and_parse_cli_output


def logging_message(suppress_output=False, help_requested=False):
    """Retrieves and optionally displays the Logging Message using 'show logging message'.
       If help_requested=True, it prints the help information instead.
    """

    logging_message_help = {
        'command': 'show logging message',
        'description': (
            "This command provides details about specific syslog messages, including their severity level and logging configuration.\n\n"
            "**Usage Notes & Troubleshooting:**\n"
            "- Use this command to verify which syslog messages are enabled or disabled.\n"
            "- If specific messages are missing, check if they are filtered using `no logging message <message_id>`.\n"
            "- To change the severity level of a log message, use `logging message <message_id> level <severity>`.\n"
            "- If logs are not appearing in your syslog server, confirm that the required messages are enabled and at the correct severity level."
        ),
        'example_output': """
FTDv# show logging message
Syslog message    Logging Level
---------------------------------
106023           Disabled
302016           Enabled (Level: Informational)
302021           Enabled (Level: Warnings)
711001           Enabled (Level: Warnings)
        """
    }

    # If help is requested, print help content and exit the function
    if help_requested:
        print("\n" + "=" * 80)
        print(f"📖 Help for: {logging_message_help['command']}".center(80))
        print("=" * 80)
        print(f"\n{logging_message_help['description']}\n")
        print("Example Output:")
        print(logging_message_help['example_output'])
        return None  # No actual command execution

    command = "show logging message"

    try:
        output = get_and_parse_cli_output(command)

        if not suppress_output:
            print("\nLogging Message Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)

        return output

    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
