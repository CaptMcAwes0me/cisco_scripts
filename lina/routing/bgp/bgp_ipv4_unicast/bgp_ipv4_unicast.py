from core.utils import get_and_parse_cli_output


def bgp_ipv4_unicast(suppress_output=False):
    """Retrieves and optionally displays the BGP IPv4 unicast table using 'show bgp ipv4 unicast'."""

    command = "show bgp ipv4 unicast"

    try:
        output = get_and_parse_cli_output(command)

        if not suppress_output:
            print("\nBGP IPv4 Unicast Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)

        return output

    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message

