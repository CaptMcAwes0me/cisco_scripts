
from core.utils import get_and_parse_cli_output

def logging_queue(suppress_output=False):
    """Retrieves and optionally displays the Logging Queue using 'show logging queue'."""

    command = "show logging queue"

    try:
        output = get_and_parse_cli_output(command)

        if not suppress_output:
            print("\nLogging Queue Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)

        return output

    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
