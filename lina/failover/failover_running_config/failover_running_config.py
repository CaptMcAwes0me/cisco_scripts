
from core.utils import get_and_parse_cli_output

def failover_running_config(suppress_output=False):
    """Retrieves and optionally displays the Failover Running Configuration using 'show run all failover'."""

    command = "show run all failover"

    try:
        output = get_and_parse_cli_output(command)

        if not suppress_output:
            print("\nFailover Running Configuration Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)

        return output

    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
