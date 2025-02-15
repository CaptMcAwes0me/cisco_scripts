from core.utils import get_and_parse_cli_output


def failover_config_sync_status(suppress_output=False, help_requested=False):
    """Retrieves and optionally displays failover configuration synchronization status using
       'show failover config-sync status'. If help_requested=True, it prints the help information instead.
    """

    failover_config_sync_status_help = {
        'command': 'show failover config-sync status',
        'description': (
            "Displays the current status of configuration synchronization between failover units. "
            "It helps in determining whether the standby unit has successfully synchronized its configuration "
            "with the active unit. Useful for diagnosing failover sync issues and ensuring redundancy integrity."
        ),
        'example_output': """
FTDv# show failover config-sync status

Config Sync Status: Success
  Last Sync Result: Successful
  Last Sync Time:   17:45:02 UTC Feb 14 2025
  Config Differences: None
        """
    }

    # If help is requested, print help content and exit the function
    if help_requested:
        print("\n" + "=" * 80)
        print(f"📖 Help for: {failover_config_sync_status_help['command']}".center(80))
        print("=" * 80)
        print(f"\n{failover_config_sync_status_help['description']}\n")
        print("Example Output:")
        print(failover_config_sync_status_help['example_output'])
        return None  # No actual command execution

    # Execute the Failover Config-Sync Status command
    command = "show failover config-sync status"
    try:
        output = get_and_parse_cli_output(command)

        if not suppress_output:
            print("\nFailover Config-Sync Status Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)

        return output

    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
