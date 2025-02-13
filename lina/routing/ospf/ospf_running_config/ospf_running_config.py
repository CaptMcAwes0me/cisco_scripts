from core.utils import get_and_parse_cli_output


def ospf_running_config(suppress_output=False, help_requested=False):
    """Retrieves and optionally displays OSPF running config information using 'show run all router ospf'.
       If help_requested=True, it prints the help information instead.
    """

    ospf_running_config_help = {
        'command': 'show run all router ospf',
        'description': (
            "Displays the complete running configuration of OSPF, including process IDs, area definitions, "
            "network statements, cost settings, and redistribution rules. This command is useful for verifying "
            "OSPF configurations and troubleshooting routing inconsistencies."
        ),
        'example_output': """
router ospf 1
 ospf router-id 192.168.1.1
 network 10.0.0.0 0.0.0.255 area 0
 network 192.168.1.0 0.0.0.255 area 0
 passive-interface default
 no passive-interface GigabitEthernet0/1
 auto-cost reference-bandwidth 1000
        """
    }

    # If help is requested, print help content and exit the function
    if help_requested:
        print("\n" + "-" * 80)
        print(f"Help for: {ospf_running_config_help['command']}".center(80))
        print("-" * 80)
        print(f"\n{ospf_running_config_help['description']}\n")
        print("Example Output:")
        print(ospf_running_config_help['example_output'])
        return None  # No actual command execution

    # Execute the OSPF Running Configuration command
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
