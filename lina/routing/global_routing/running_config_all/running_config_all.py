from core.utils import get_and_parse_cli_output


def running_config_all(suppress_output=False, config_type="route"):
    """Retrieves and optionally displays the running configuration for either all routes or all routers."""
    
    # Determine the correct command based on the config_type
    if config_type == "route":
        command = "show running-config all route"
    elif config_type == "router":
        command = "show running-config all router"
    else:
        raise ValueError("[!] Invalid config_type. Expected 'route' or 'router'.")
    
    try:
        output = get_and_parse_cli_output(command)

        # Conditionally print the output
        if not suppress_output:
            print(f"\nRunning Config All {config_type.capitalize()} Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)

        return output

    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message

