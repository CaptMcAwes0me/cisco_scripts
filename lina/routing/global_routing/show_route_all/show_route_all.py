from core.utils import get_and_parse_cli_output


def show_route_all(suppress_output=False):
    """Retrieves and optionally displays all routes using the 'show route all' command."""
    
    command = "show route all"
    
    try:
        output = get_and_parse_cli_output(command)

        # Conditionally print the output
        if not suppress_output:
            print("\nRoute All Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)

        return output

    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message

