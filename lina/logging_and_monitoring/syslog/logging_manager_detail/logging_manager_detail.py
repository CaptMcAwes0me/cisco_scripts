from core.utils import get_and_parse_cli_output


def logging_manager_detail(suppress_output=False, help_requested=False):
    """Retrieves and optionally displays the Logging Manager Detail using 'show logging manager detail'.
       If help_requested=True, it prints the help information instead.
    """

    logging_manager_detail_help = {
        'command': 'show logging manager detail',
        'description': (
            "This command displays detailed information about the logging manager, including syslog event monitoring, "
            "subscription levels, and configured destinations.\n\n"
            "**Usage Notes & Troubleshooting:**\n"
            "- Use this command to verify which syslog events are being monitored and their severity levels.\n"
            "- If syslog messages are missing, check the **Subscription details** section to ensure events are being logged.\n"
            "- If logs are not appearing in external syslog servers, ensure `logging host` is correctly configured.\n"
            "- Use `logging trap <severity>` to modify which severity levels are sent to external syslog servers."
        ),
        'example_output': """
FTDv# show logging manager detail
FMC syslog event monitoring: Enabled
Subscription details:
   ID    Level
-------- -----
 109010    3
 109011    2
 109016    3
 109018    3
 109019    3
 109020    3
 109023    3
 109026    3
 109032    3
 109035    3
 109037    3
 109038    3
        """
    }

    # If help is requested, print help content and exit the function
    if help_requested:
        print("\n" + "=" * 80)
        print(f"📖 Help for: {logging_manager_detail_help['command']}".center(80))
        print("=" * 80)
        print(f"\n{logging_manager_detail_help['description']}\n")
        print("Example Output:")
        print(logging_manager_detail_help['example_output'])
        return None  # No actual command execution

    command = "show logging manager detail"

    try:
        output = get_and_parse_cli_output(command)

        if not suppress_output:
            print("\nLogging Manager Detail Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)

        return output

    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
