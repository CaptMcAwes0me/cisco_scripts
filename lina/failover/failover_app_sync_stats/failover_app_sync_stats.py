from core.utils import get_and_parse_cli_output


def failover_app_sync_stats(suppress_output=False, help_requested=False):
    """Retrieves and optionally displays failover application synchronization statistics using
       'show failover app-sync stats'. If help_requested=True, it prints the help information instead.
    """

    failover_app_sync_stats_help = {
        'command': 'show failover app-sync stats',
        'description': (
            "Displays synchronization statistics for applications using failover app-sync. "
            "This command helps in troubleshooting application state synchronization issues "
            "between the active and standby units. It shows data about messages exchanged, "
            "timeouts, and failures during synchronization."
        ),
        'example_output': """
FTDv# show failover app-sync stats

App-Sync Messages Sent:      150
App-Sync Messages Received:  148
App-Sync Messages Dropped:   2
App-Sync Failures:           1
Last Sync Time:              17:50:22 UTC Feb 14 2025
        """
    }

    # If help is requested, print help content and exit the function
    if help_requested:
        print("\n" + "=" * 80)
        print(f"📖 Help for: {failover_app_sync_stats_help['command']}".center(80))
        print("=" * 80)
        print(f"\n{failover_app_sync_stats_help['description']}\n")
        print("Example Output:")
        print(failover_app_sync_stats_help['example_output'])
        return None  # No actual command execution

    # Execute the Failover App-Sync Stats command
    command = "show failover app-sync stats"
    try:
        output = get_and_parse_cli_output(command)

        if not suppress_output:
            print("\nFailover App-Sync Stats Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)

        return output

    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
