# Description: This script retrieves and displays EIGRP routing table.

from core.utils import get_and_parse_cli_output


def eigrp_routing_table(suppress_output=False):
    """Retrieves and optionally displays EIGRP neighbors using the 'show route all eigrp' command."""

    command = "show route all eigrp"

    try:
        output = get_and_parse_cli_output(command)

        # Conditionally print the output
        if not suppress_output:
            print("\nEIGRP Routing Table Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)

        return output

    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
