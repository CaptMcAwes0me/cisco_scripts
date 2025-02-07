from core.utils import get_and_parse_cli_output


def asp_table_routing_all(suppress_output=False):
    """Retrieves and optionally displays the ASP table routing information for all using the
    'show asp table routing all' command."""
    
    command = "show asp table routing all"
    
    try:
        output = get_and_parse_cli_output(command)

        # Conditionally print the output
        if not suppress_output:
            print("\nASP Table Routing All Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)

        return output

    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
