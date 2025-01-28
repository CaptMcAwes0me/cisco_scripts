# Description: This script retrieves and displays EIGRP interfaces.

from core.utils import get_and_parse_cli_output


def eigrp_interfaces(suppress_output=False):
    """Retrieves and optionally displays EIGRP interfaces using the 'show eigrp events' command."""

    command = "show eigrp interfaces"

    try:
        output = get_and_parse_cli_output(command)

        # Conditionally print the output
        if not suppress_output:
            print("\nEIGRP Interfaces Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)

        return output

    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
