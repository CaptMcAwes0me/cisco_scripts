from core.utils import get_and_parse_cli_output


def bgp_summary(suppress_output=False, help_requested=False):
    """Retrieves and optionally displays the BGP summary using 'show bgp summary'.
       If help_requested=True, it prints the help information instead.
    """

    bgp_summary_help = {
        'command': 'show bgp summary',
        'description': (
            "Displays a summary of BGP neighbors, including AS numbers, state, "
            "messages sent/received, and uptime. This command is useful for quickly "
            "assessing the status of BGP peers."
        ),
        'example_output': """
BGP router identifier 203.0.113.1, local AS number 65001
BGP table version is 7, main routing table version 7
Neighbor        V    AS MsgRcvd MsgSent TblVer  InQ OutQ Up/Down  State/PfxRcd
203.0.113.2     4  65002      45      60       7    0    0 00:14:25       12
198.51.100.3    4  65003      32      48       7    0    0 00:05:32        8
        """
    }

    # If help is requested, print help content and exit the function
    if help_requested:
        print("\n" + "-" * 80)
        print(f"Help for: {bgp_summary_help['command']}".center(80))
        print("-" * 80)
        print(f"\n{bgp_summary_help['description']}\n")
        print("Example Output:")
        print(bgp_summary_help['example_output'])
        return None  # No actual command execution

    # Execute the BGP Summary command
    command = "show bgp summary"

    try:
        output = get_and_parse_cli_output(command)

        if not suppress_output:
            print("\nBGP Summary Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)

        return output

    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
