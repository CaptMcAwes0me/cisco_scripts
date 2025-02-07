from core.utils import get_and_parse_cli_output


def crypto_ipsec_sa_detail_dump(suppress_output=False):
    """Retrieves and optionally displays detailed IPSec Security Association (SA) information."""

    command = "show crypto ipsec sa detail"

    try:
        output = get_and_parse_cli_output(command)

        if not suppress_output:  # Only print output if suppression is disabled
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
