from core.utils import get_and_parse_cli_output


def ospf_neighbor(suppress_output=False):
    """Retrieves and optionally displays OSPF neighbor information using the 'show ospf neighbor' command."""
    command = "show ospf neighbor"
    try:
        output = get_and_parse_cli_output(command)
        if not suppress_output:
            print("\nOSPF Neighbor Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)
        return output
    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message

