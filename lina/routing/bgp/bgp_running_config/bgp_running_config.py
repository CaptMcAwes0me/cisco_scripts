from core.utils import get_and_parse_cli_output


def bgp_running_config(suppress_output=False, help_requested=False):
    """Retrieves and optionally displays the BGP running configuration using 'show running-config all router bgp'.
       If help_requested=True, it prints the help information instead.
    """

    bgp_running_config_help = {
        'command': 'show running-config all router bgp',
        'description': (
            "Displays the complete running configuration of BGP, including all parameters, policies, "
            "and settings that are currently applied. This is useful for verifying BGP configuration "
            "and troubleshooting misconfigurations."
        ),
        'example_output': """
router bgp 65001
 bgp router-id 203.0.113.1
 bgp log-neighbor-changes
 neighbor 203.0.113.2 remote-as 65002
 neighbor 203.0.113.2 description PEER-1
 neighbor 198.51.100.3 remote-as 65003
 address-family ipv4 unicast
  network 10.10.10.0 mask 255.255.255.0
  neighbor 203.0.113.2 activate
  neighbor 198.51.100.3 activate
 exit-address-family
        """
    }

    # If help is requested, print help content and exit the function
    if help_requested:
        print("\n" + "-" * 80)
        print(f"Help for: {bgp_running_config_help['command']}".center(80))
        print("-" * 80)
        print(f"\n{bgp_running_config_help['description']}\n")
        print("Example Output:")
        print(bgp_running_config_help['example_output'])
        return None  # No actual command execution

    # Execute the BGP Running Configuration command
    command = "show running-config all router bgp"

    try:
        output = get_and_parse_cli_output(command)

        if not suppress_output:
            print("\nBGP Running Configuration Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)

        return output

    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
