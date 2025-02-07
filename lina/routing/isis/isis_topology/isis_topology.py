from core.utils import get_and_parse_cli_output


def isis_topology(suppress_output=False):
    """Retrieves and optionally displays the ISIS topology."""
    command = "show isis topology"
    try:
        output = get_and_parse_cli_output(command)
        if not suppress_output:
            print("\nISIS Topology Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)
        return output
    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message

