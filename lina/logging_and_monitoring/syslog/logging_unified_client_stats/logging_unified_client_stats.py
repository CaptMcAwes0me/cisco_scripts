from core.utils import get_and_parse_cli_output


def logging_unified_client_stats(suppress_output=False, help_requested=False):
    """Retrieves and optionally displays the Logging Unified-client Stats using 'show logging unified-client statistics'.
       If help_requested=True, it prints the help information instead.
    """

    logging_unified_client_stats_help = {
        'command': 'show logging unified-client statistics',
        'description': (
            "This command provides statistics on the Unified Logging Client, including its registration state, "
            "service uptime, configuration pushes, and log message transmissions.\n\n"
            "**Usage Notes & Troubleshooting:**\n"
            "- Verify that the **Loggerd service status** is `Up`. If it's `Down`, logs may not be sent.\n"
            "- Check if the client has successfully registered (`Total register messages Tx` should be >0).\n"
            "- Look for recent configuration pushes (`Number of configuration pushes`).\n"
            "- Ensure `Total register-ack messages Rx` is nonzero, indicating successful registration acknowledgment.\n"
            "- If `Last service down time` is recent, logs may have been lost during downtime."
        ),
        'example_output': """
FTDv# show logging unified-client statistics

Log client details:
  Name                                             : Lina
  Id                                               : 4772
  Init time                                        : Fri Feb 14 13:19:21 2025
  Status                                           : Registered

Loggerd service up/down statistics:
  Service status                                   : Up
  Instance-id                                      : 4505
  Last service down time                           : Fri Feb 14 15:05:18 2025

Log client register/unregister statistics:
  Total register messages Tx                       : 2
  Total unregister messages Tx                     : 0
  Last register message Tx time                    : Fri Feb 14 15:05:39 2025
  Total register-ack messages Rx                   : 2
  Last register-ack Rx time                        : Fri Feb 14 15:05:40 2025
  Total configuration sent messages Tx             : 3
  Number of configuration pushes                   : 1
        """
    }

    # If help is requested, print help content and exit the function
    if help_requested:
        print("\n" + "=" * 80)
        print(f"📖 Help for: {logging_unified_client_stats_help['command']}".center(80))
        print("=" * 80)
        print(f"\n{logging_unified_client_stats_help['description']}\n")
        print("Example Output:")
        print(logging_unified_client_stats_help['example_output'])
        return None  # No actual command execution

    command = "show logging unified-client statistics"

    try:
        output = get_and_parse_cli_output(command)

        if not suppress_output:
            print("\nLogging Unified-client Stats Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)

        return output

    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
