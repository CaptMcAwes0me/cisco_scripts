from core.utils import get_and_parse_cli_output


def vpn_sessiondb_anyconnect():
    """Retrieves and displays AnyConnect VPN session database information, with optional filtering by username."""

    username = input("Enter username to filter (Press Enter for all sessions): ").strip()

    if username:
        command = f"show vpn-sessiondb anyconnect filter name {username}"
    else:
        command = "show vpn-sessiondb anyconnect"

    try:
        output = get_and_parse_cli_output(command)

        print(f"\n{command} Output:")
        print("-" * 80)
        print(output)
        print("-" * 80)

        return output

    except Exception as e:
        error_message = f"[!] Error: {e}"
        print(error_message)
        return error_message
