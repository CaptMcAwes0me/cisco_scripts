# Description: This script retrieves and optionally displays the conn table using 'show conn detail' or a filtered version.

from core.utils import get_and_parse_cli_output


def conn_detail(suppress_output=False):
    """Retrieves and optionally displays the conn table using 'show conn detail' or a filtered version."""

    # Prompt user for an IP address to filter
    ip_filter = input("Enter an IP address to filter by (or press enter to show all): ").strip()

    # Modify the command based on user input
    command = f"show conn address {ip_filter}" if ip_filter else "show conn detail"

    try:
        output = get_and_parse_cli_output(command)

        if not suppress_output:
            print("\nConn Detail Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)

        return output

    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message


def conn_detail_dump(suppress_output=False):
    """Retrieves and optionally displays the conn using 'show conn detail'."""

    command = "show conn detail"

    try:
        output = get_and_parse_cli_output(command)

        if not suppress_output:
            print("\nConn Detail Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)

        return output

    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
