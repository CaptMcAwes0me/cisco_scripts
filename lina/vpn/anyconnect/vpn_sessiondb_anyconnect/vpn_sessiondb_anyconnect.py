from core.utils import get_and_parse_cli_output


def vpn_sessiondb_anyconnect(tunnel_group):
    """
    Retrieves and displays AnyConnect VPN session database information
    from the previously selected tunnel-group.
    """
    try:
        print("=" * 80)
        print(f"VPN-Sessiondb Information for {tunnel_group}".center(80))
        print("=" * 80)
        command = f"show vpn-sessiondb anyconnect filter tunnel-group {tunnel_group}"
        output = get_and_parse_cli_output(command)
        print(output)
        print("=" * 80 + "\n")
        return output

    except Exception as e:
        error_message = f"[!] Error: {e}"
        print(error_message)
        return error_message
