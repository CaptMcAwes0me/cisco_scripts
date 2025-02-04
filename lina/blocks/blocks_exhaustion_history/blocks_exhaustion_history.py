
from core.utils import get_and_parse_cli_output

def blocks_exhaustion_history(suppress_output=False):
    """Retrieves and optionally displays the Blocks Exhaustion History using 'show blocks exhaustion history'."""

    command = "show blocks exhaustion history"

    try:
        output = get_and_parse_cli_output(command)

        if not suppress_output:
            print("\nBlocks Exhaustion History Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)

        return output

    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
