from core.utils import get_and_parse_cli_output


def bgp_rib_failure(suppress_output=False):
    """Retrieves and optionally displays the BGP RIB failures using 'show bgp rib-failure'."""

    command = "show bgp rib-failure"

    try:
        output = get_and_parse_cli_output(command)

        if not suppress_output:
            print("\nBGP RIB Failure Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)

        return output

    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message

