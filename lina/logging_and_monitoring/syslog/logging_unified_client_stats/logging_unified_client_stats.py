
from core.utils import get_and_parse_cli_output

def logging_unified_client_stats(suppress_output=False):
    """Retrieves and optionally displays the Logging Unified-client Stats using 'show logging unified-client statistics'."""

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
