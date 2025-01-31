
from core.utils import get_and_parse_cli_output

def xlate_detail(suppress_output=False):
    """Retrieves and optionally displays the Xlate Detail Table using 'show xlate detail'."""

    command = "show xlate detail"

    try:
        output = get_and_parse_cli_output(command)

        if not suppress_output:
            print("\nXlate Detail Table Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)

        return output

    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
