
from core.utils import get_and_parse_cli_output

def failover_config_sync_status(suppress_output=False):
    """Retrieves and optionally displays the Failover Config-sync Status using 'show failover config-sync status'."""

    command = "show failover config-sync status"

    try:
        output = get_and_parse_cli_output(command)

        if not suppress_output:
            print("\nFailover Config-sync Status Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)

        return output

    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
