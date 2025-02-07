from core.utils import get_and_parse_cli_output


def vrf_running_config(suppress_output=False):
    """Retrieves and optionally displays the VRF running configuration using the 'show running-config all vrf' command."""

    command = "show running-config all vrf"

    try:
        output = get_and_parse_cli_output(command)

        # Conditionally print the output
        if not suppress_output:
            print("\nVRF Running Configuration Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)

        return output

    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message

