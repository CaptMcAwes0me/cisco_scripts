from core.utils import get_and_parse_cli_output

def eigrp_running_config(suppress_output=False, help_requested=False):
    """Retrieves and optionally displays EIGRP running config information using 'show run all router eigrp'.
       If help_requested=True, it prints the help information instead.
    """

    eigrp_running_config_help = {
        'command': 'show run all router eigrp',
        'description': (
            "Displays the complete running configuration of EIGRP, including autonomous system (AS) numbers, "
            "network statements, and other routing parameters. This command helps verify EIGRP settings and troubleshoot configuration issues."
        ),
        'example_output': """
router eigrp 100
 eigrp router-id 192.168.1.1
 network 10.0.0.0 0.0.0.255
 network 192.168.1.0 0.0.0.255
 passive-interface default
 no passive-interface GigabitEthernet0/1
 timers active-time 3
 metric maximum-hops 100
 auto-summary
        """
    }

    # If help is requested, print help content and exit the function
    if help_requested:
        print("\n" + "-" * 80)
        print(f"Help for: {eigrp_running_config_help['command']}".center(80))
        print("-" * 80)
        print(f"\n{eigrp_running_config_help['description']}\n")
        print("Example Output:")
        print(eigrp_running_config_help['example_output'])
        return None  # No actual command execution

    # Execute the EIGRP Running Configuration command
    command = "show run all router eigrp"
    try:
        output = get_and_parse_cli_output(command)
        if not suppress_output:
            print("\nEIGRP Running Config Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)
        return output
    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
