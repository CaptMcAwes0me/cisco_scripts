from core.utils import get_and_parse_cli_output


def ospf_traffic(suppress_output=False):
    """Retrieves and optionally displays OSPF traffic information using the 'show ospf traffic' command."""
    command = "show ospf traffic"
    try:
        output = get_and_parse_cli_output(command)
        if not suppress_output:
            print("\nOSPF Traffic Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)
        return output
    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message

