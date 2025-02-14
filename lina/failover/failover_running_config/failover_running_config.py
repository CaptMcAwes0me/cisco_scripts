from core.utils import get_and_parse_cli_output

def failover_running_config(suppress_output=False, help_requested=False):
    """Retrieves and optionally displays the Failover Running Configuration using 'show run all failover'.
       If help_requested=True, it prints the help information instead.
    """

    failover_running_config_help = {
        'command': 'show run all failover',
        'description': (
            "Displays the complete running configuration for failover, including failover interface, "
            "primary/secondary unit roles, failover state synchronization settings, and monitored interfaces. "
            "This command is useful for verifying high availability (HA) settings and debugging failover issues."
        ),
        'example_output': """
failover
failover lan unit primary
failover lan interface FAILOVER GigabitEthernet0/2
failover link STATEFUL GigabitEthernet0/3
failover interface ip FAILOVER 192.168.1.1 255.255.255.0 standby 192.168.1.2
failover interface ip STATEFUL 192.168.2.1 255.255.255.0 standby 192.168.2.2
failover polltime unit 2 holdtime 5
failover polltime interface 5 holdtime 15
failover replication http
failover replication rate 1000
failover replication timeout 10
        """
    }

    # If help is requested, print help content and exit the function
    if help_requested:
        print("\n" + "=" * 80)
        print(f"📖 Help for: {failover_running_config_help['command']}".center(80))
        print("=" * 80)
        print(f"\n{failover_running_config_help['description']}\n")
        print("Example Output:")
        print(failover_running_config_help['example_output'])
        return None  # No actual command execution

    # Execute the Failover Running Configuration command
    command = "show run all failover"
    try:
        output = get_and_parse_cli_output(command)

        if not suppress_output:
            print("\nFailover Running Configuration Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)

        return output

    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
