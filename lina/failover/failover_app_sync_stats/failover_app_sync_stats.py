
from core.utils import get_and_parse_cli_output

def failover_app_sync_stats(suppress_output=False):
    """Retrieves and optionally displays the Failover App-sync Stats using 'show failover app-sync stats'."""

    command = "show failover app-sync stats"

    try:
        output = get_and_parse_cli_output(command)

        if not suppress_output:
            print("\nFailover App-sync Stats Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)

        return output

    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
