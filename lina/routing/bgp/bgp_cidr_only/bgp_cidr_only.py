from core.utils import get_and_parse_cli_output


def bgp_cidr_only(suppress_output=False, help_requested=False):
    """Retrieves and optionally displays the BGP CIDR-only table using 'show bgp cidr-only'.
       If help_requested=True, it prints the help information instead.
    """

    bgp_cidr_only_help = {
        'command': 'show bgp cidr-only',
        'description': (
            "Displays only the routes in the BGP table that are represented in Classless Inter-Domain Routing (CIDR) format. "
            "This command is useful for viewing summarized routes and ensuring efficient route aggregation."
        ),
        'example_output': """
BGP table version is 7, local router ID is 203.0.113.1
Status codes: s suppressed, d damped, h history, * valid, > best, i - internal,
              r RIB-failure, S Stale, m multipath
Origin codes: i - IGP, e - EGP, ? - incomplete

   Network          Next Hop            Metric LocPrf Weight Path
*> 10.10.10.0/24    203.0.113.2              0             0 200 i
*> 10.106.44.0/24   0.0.0.0                  0         32768 i
*> 10.180.10.0/24   203.0.113.2              0             0 200 i
*> 172.16.20.0/24   0.0.0.0                  0         32768 i
*> 172.16.30.0/24   203.0.113.2              0             0 200 i
        """
    }

    # If help is requested, print help content and exit the function
    if help_requested:
        print("\n" + "-" * 80)
        print(f"Help for: {bgp_cidr_only_help['command']}".center(80))
        print("-" * 80)
        print(f"\n{bgp_cidr_only_help['description']}\n")
        print("Example Output:")
        print(bgp_cidr_only_help['example_output'])
        return None  # No actual command execution

    # Execute the BGP CIDR-Only command
    command = "show bgp cidr-only"

    try:
        output = get_and_parse_cli_output(command)

        if not suppress_output:
            print("\nBGP CIDR-Only Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)

        return output

    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
