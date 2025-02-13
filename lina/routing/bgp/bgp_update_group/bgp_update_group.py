from core.utils import get_and_parse_cli_output


def bgp_update_group(suppress_output=False, help_requested=False):
    """Retrieves and optionally displays the BGP update groups using 'show bgp update-group'.
       If help_requested=True, it prints the help information instead.
    """

    bgp_update_group_help = {
        'command': 'show bgp update-group',
        'description': (
            "Displays information about BGP update groups, which are sets of BGP neighbors "
            "that share the same outbound policies. Understanding update groups is essential "
            "for optimizing BGP updates and reducing processing overhead."
        ),
        'example_output': """
BGP router identifier 203.0.113.1, local AS number 65001

Update-group 1, IPv4 Unicast, distribution: 2 peers
  Neighbor        AS        MsgRcvd  MsgSent  Up/Down   State/PfxRcd
  203.0.113.2     65002     45       60       00:14:25  12
  198.51.100.3    65003     32       48       00:05:32   8
        """
    }

    # If help is requested, print help content and exit the function
    if help_requested:
        print("\n" + "-" * 80)
        print(f"Help for: {bgp_update_group_help['command']}".center(80))
        print("-" * 80)
        print(f"\n{bgp_update_group_help['description']}\n")
        print("Example Output:")
        print(bgp_update_group_help['example_output'])
        return None  # No actual command execution

    # Execute the BGP Update Group command
    command = "show bgp update-group"

    try:
        output = get_and_parse_cli_output(command)

        if not suppress_output:
            print("\nBGP Update-group Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)

        return output

    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
