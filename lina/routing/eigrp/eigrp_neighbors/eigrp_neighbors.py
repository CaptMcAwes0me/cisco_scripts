# Description: This script retrieves and displays EIGRP interfaces.

from core.utils import get_and_parse_cli_output


def eigrp_neighbors(suppress_output=False):
    """Retrieves and optionally displays EIGRP neighbors using the 'show eigrp neighbors' command."""

    command = "show eigrp neighbors"

    try:
        output = get_and_parse_cli_output(command)

        # Conditionally print the output
        if not suppress_output:
            print("\nEIGRP Neighbors Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)

        return output

    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
