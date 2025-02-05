from core.utils import get_and_parse_cli_output


def vpn_sessiondb_anyconnect_dump():
    """Retrieves and displays the full AnyConnect VPN session database."""

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
