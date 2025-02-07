
from core.utils import get_and_parse_cli_output

def ssl_errors(suppress_output=False):
    """Retrieves and optionally displays the SSL Error using 'show ssl errors'."""

    command = "show ssl errors"

    try:
        output = get_and_parse_cli_output(command)

        if not suppress_output:
            print("\nSSL Error Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)

        return output

    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
