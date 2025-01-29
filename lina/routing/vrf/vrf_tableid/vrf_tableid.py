from core.utils import get_and_parse_cli_output


def vrf_tableid(suppress_output=False):
    """Retrieves and optionally displays VRF table ID using the 'show vrf tableid' command."""

    command = "show vrf tableid"

    try:
        output = get_and_parse_cli_output(command)

        # Conditionally print the output
        if not suppress_output:
            print("\nVRF Table ID Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)

        return output

    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message

