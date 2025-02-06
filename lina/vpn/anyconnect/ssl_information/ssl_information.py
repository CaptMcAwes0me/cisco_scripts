
from core.utils import get_and_parse_cli_output

def ssl_information(suppress_output=False):
    """Retrieves and optionally displays the SSL Information using 'show ssl information'."""

    command = "show ssl information"

    try:
        output = get_and_parse_cli_output(command)

        if not suppress_output:
            print("\nSSL Information Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)

        return output

    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
