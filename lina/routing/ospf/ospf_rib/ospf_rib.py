from core.utils import get_and_parse_cli_output


def ospf_rib(suppress_output=False):
    """Retrieves and optionally displays OSPF RIB (Routing Information Base) using the 'show ospf rib' command."""
    command = "show ospf rib"
    try:
        output = get_and_parse_cli_output(command)
        if not suppress_output:
            print("\nOSPF RIB Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)
        return output
    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message

