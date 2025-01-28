from core.utils import get_and_parse_cli_output


def ospf_border_routers(suppress_output=False):
    """Retrieves and optionally displays OSPF border routers using the 'show ospf border-routers' command."""
    command = "show ospf border-routers"
    try:
        output = get_and_parse_cli_output(command)
        if not suppress_output:
            print("\nOSPF Border Routers Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)
        return output
    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message

