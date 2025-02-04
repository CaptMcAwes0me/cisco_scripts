
from core.utils import get_and_parse_cli_output

def blocks_queue_history_detail(suppress_output=False):
    """Retrieves and optionally displays the Blocks Queue History Detail using 'show blocks queue history detail'."""

    command = "show blocks queue history detail"

    try:
        output = get_and_parse_cli_output(command)

        if not suppress_output:
            print("\nBlocks Queue History Detail Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)

        return output

    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
