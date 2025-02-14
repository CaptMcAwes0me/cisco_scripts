from core.utils import get_and_parse_cli_output


def logging_unified_client(suppress_output=False, help_requested=False):
    """Retrieves and optionally displays the Logging Unified Client using 'show logging unified-client'.
       If help_requested=True, it prints the help information instead.
    """

    logging_unified_client_help = {
        'command': 'show logging unified-client',
        'description': (
            "This command displays detailed information about registered log clients, their connection status, "
            "initialization time, and other logging-related details.\n\n"
            "**Usage Notes & Troubleshooting:**\n"
            "- If logs are not being received, verify that the client is `Registered`.\n"
            "- Check if the logging server is correctly configured (`show running-config logging`).\n"
            "- If the client is not registered, ensure logging is enabled and restart the logging service.\n"
            "- Look for firewall rules that may be blocking syslog traffic between the device and the logging server.\n"
            "- If issues persist, restart the logging service or check for any licensing restrictions."
        ),
        'example_output': """
FTDv# show logging unified-client

Log client details:
  Name                                             : Lina
  Id                                               : 4772
  Init time                                        : Fri Feb 14 13:19:21 2025
  Status                                           : Registered
        """
    }

    # If help is requested, print help content and exit the function
    if help_requested:
        print("\n" + "=" * 80)
        print(f"📖 Help for: {logging_unified_client_help['command']}".center(80))
        print("=" * 80)
        print(f"\n{logging_unified_client_help['description']}\n")
        print("Example Output:")
        print(logging_unified_client_help['example_output'])
        return None  # No actual command execution

    command = "show logging unified-client"

    try:
        output = get_and_parse_cli_output(command)

        if not suppress_output:
            print("\nLogging Unified Client Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)

        return output

    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
