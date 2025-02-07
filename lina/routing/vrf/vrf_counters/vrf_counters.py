from core.utils import get_and_parse_cli_output


def vrf_counters(suppress_output=False):
    """Retrieves and optionally displays VRF counters using the 'show vrf counters' command."""

    command = "show vrf counters"

    try:
        output = get_and_parse_cli_output(command)

        # Conditionally print the output
        if not suppress_output:
            print("\nVRF Counters Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)

        return output

    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message

