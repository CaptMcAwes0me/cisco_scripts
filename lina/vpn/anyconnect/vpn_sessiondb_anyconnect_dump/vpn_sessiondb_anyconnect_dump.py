from core.utils import get_and_parse_cli_output


def vpn_sessiondb_anyconnect_dump(suppress_output=False):
    """Retrieves and optionally displays the full AnyConnect VPN session database."""

    command = "show vpn-sessiondb anyconnect"

    try:
        output = get_and_parse_cli_output(command)

        if not suppress_output:  # Suppress output if True
            print(f"\n{command} Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)

        return output

    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
