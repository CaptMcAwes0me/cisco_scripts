from core.utils import get_and_parse_cli_output


def ospf_running_config(suppress_output=False):
    """Retrieves and optionally displays OSPF running config information using the 'show run all router ospf' command."""
    command = "show run all router ospf"
    try:
        output = get_and_parse_cli_output(command)
        if not suppress_output:
            print("\nOSPF Running Config Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)
        return output
    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message

