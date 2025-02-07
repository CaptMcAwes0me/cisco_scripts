# Description: This script retrieves and displays EIGRP traffic.

from core.utils import get_and_parse_cli_output


def eigrp_traffic(suppress_output=False):
    """Retrieves and optionally displays EIGRP traffic using the 'show eigrp traffic' command."""

    command = "show eigrp traffic"

    try:
        output = get_and_parse_cli_output(command)

        # Conditionally print the output
        if not suppress_output:
            print("\nEIGRP Traffic Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)

        return output

    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
