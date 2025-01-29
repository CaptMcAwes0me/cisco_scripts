from core.utils import get_and_parse_cli_output


def vrf_detail(suppress_output=False):
    """Retrieves and optionally displays detailed VRF information using the 'show vrf detail' command."""

    command = "show vrf detail"

    try:
        output = get_and_parse_cli_output(command)

        # Conditionally print the output
        if not suppress_output:
            print("\nVRF Detail Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)

        return output

    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message

