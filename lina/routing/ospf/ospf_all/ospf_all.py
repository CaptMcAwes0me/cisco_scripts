from core.utils import get_and_parse_cli_output

def ospf_all(suppress_output=False):
    """Retrieves and optionally displays OSPF all information using the 'show ospf all' command."""
    command = "show ospf all"
    try:
        output = get_and_parse_cli_output(command)
        if not suppress_output:
            print("\nOSPF All Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)
        return output
    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message

