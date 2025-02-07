
from core.utils import get_and_parse_cli_output

def nat_detail(suppress_output=False):
    """Retrieves and optionally displays the NAT Detail Table using 'show nat detail'."""

    command = "show nat detail"

    try:
        output = get_and_parse_cli_output(command)

        if not suppress_output:
            print("\nNAT Detail Table Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)

        return output

    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
