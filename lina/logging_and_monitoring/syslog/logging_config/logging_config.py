from core.utils import get_and_parse_cli_output


def logging_config(suppress_output=False, help_requested=False):
    """Retrieves and optionally displays the Logging Configuration using 'show running-config logging'.
       If help_requested=True, it prints the help information instead.
    """

    logging_config_help = {
        'command': 'show running-config logging',
        'description': (
            "This command displays the current logging configuration on the device, including logging "
            "enablement, timestamp settings, logging levels, buffer sizes, and syslog server destinations. "
            "It also shows which specific syslog messages are enabled or suppressed.\n\n"
            "**Usage Notes & Troubleshooting:**\n"
            "- Use this command to verify that logging is properly configured.\n"
            "- If logs are not appearing as expected, check if logging is enabled (`logging enable`).\n"
            "- Review `logging list` entries to ensure the correct classes are included.\n"
            "- If buffer-based logging is used, verify `logging buffered` is enabled with an appropriate buffer size.\n"
            "- Suppressed messages (`no logging message <ID>`) may prevent expected logs from being recorded.\n"
            "- If logs are being forwarded to an external syslog server (`logging host`), verify network reachability.\n"
        ),
        'example_output': """
FTDv# show running-config logging
logging enable
logging timestamp
logging list MANAGER_VPN_EVENT_LIST level errors class auth
logging list MANAGER_VPN_EVENT_LIST level errors class vpn
logging buffer-size 52428800
logging buffered test
logging FMC MANAGER_VPN_EVENT_LIST
logging debug-trace persistent
logging permit-hostdown
no logging message 106015
no logging message 302015
logging message 711001 level warnings
        """
    }

    # If help is requested, print help content and exit the function
    if help_requested:
        print("\n" + "=" * 80)
        print(f"📖 Help for: {logging_config_help['command']}".center(80))
        print("=" * 80)
        print(f"\n{logging_config_help['description']}\n")
        print("Example Output:")
        print(logging_config_help['example_output'])
        return None  # No actual command execution

    command = "show running-config logging"

    try:
        output = get_and_parse_cli_output(command)

        if not suppress_output:
            print("\nLogging Configuration Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)

        return output

    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
