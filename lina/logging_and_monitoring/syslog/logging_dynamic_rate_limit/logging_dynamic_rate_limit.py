
from core.utils import get_and_parse_cli_output

def logging_dynamic_rate_limit(suppress_output=False):
    """Retrieves and optionally displays the Logging Dynamic-rate-limit using 'show logging dynamic-rate-limit'."""

    command = "show logging dynamic-rate-limit"

    try:
        output = get_and_parse_cli_output(command)

        if not suppress_output:
            print("\nLogging Dynamic-rate-limit Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)

        return output

    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
