from core.utils import get_and_parse_cli_output

def running_config_all(suppress_output=False, config_type="route", help_requested=False):
    """Retrieves and optionally displays the running configuration for either all routes or all routers.
       If help_requested=True, it prints the help information instead.
    """

    # Help information for both command variations
    running_config_help = {
        "route": {
            'command': 'show running-config all route',
            'description': (
                "Displays the full running configuration related to routing settings. "
                "This includes static routes, dynamic routing protocol configurations, "
                "and policy-based routing configurations."
            ),
            'example_output': """
Running Config - Route:

route outside 0.0.0.0 0.0.0.0 192.168.1.1
route inside 10.1.1.0 255.255.255.0 10.1.1.1
            """
        },
        "router": {
            'command': 'show running-config all router',
            'description': (
                "Displays the full running configuration for all routing protocols. "
                "This includes configurations for OSPF, BGP, EIGRP, and ISIS."
            ),
            'example_output': """
Running Config - Router:

router ospf 1
 network 10.1.1.0 0.0.0.255 area 0
router bgp 65000
 neighbor 192.168.1.2 remote-as 65001
            """
        }
    }

    # If help is requested, print help content and exit the function
    if help_requested:
        if config_type in running_config_help:
            help_data = running_config_help[config_type]
            print("\n" + "-" * 80)
            print(f"Help for: {help_data['command']}".center(80))
            print("-" * 80)
            print(f"\n{help_data['description']}\n")
            print("Example Output:")
            print(help_data['example_output'])
        else:
            print(f"\n[!] No help available for config type: {config_type}")
        return None  # No actual command execution

    # Determine the correct command based on the config_type
    if config_type not in running_config_help:
        raise ValueError("[!] Invalid config_type. Expected 'route' or 'router'.")

    command = running_config_help[config_type]['command']

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
