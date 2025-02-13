from core.utils import get_and_parse_cli_output


def bgp_rib_failure(suppress_output=False, help_requested=False):
    """Retrieves and optionally displays the BGP RIB failures using 'show bgp rib-failure'.
       If help_requested=True, it prints the help information instead.
    """

    bgp_rib_failure_help = {
        'command': 'show bgp rib-failure',
        'description': (
            "Displays BGP routes that have failed to be installed in the Routing Information Base (RIB). "
            "This is useful for diagnosing why certain BGP-learned routes are not being added to the forwarding table."
        ),
        'example_output': """
Network          Next Hop            Reason
10.10.10.0/24    203.0.113.2         Higher admin distance
10.180.10.0/24   203.0.113.2         Best path is from IGP
172.16.30.0/24   203.0.113.2         Not selected as best path
        """
    }

    # If help is requested, print help content and exit the function
    if help_requested:
        print("\n" + "-" * 80)
        print(f"Help for: {bgp_rib_failure_help['command']}".center(80))
        print("-" * 80)
        print(f"\n{bgp_rib_failure_help['description']}\n")
        print("Example Output:")
        print(bgp_rib_failure_help['example_output'])
        return None  # No actual command execution

    # Execute the BGP RIB Failure command
    command = "show bgp rib-failure"

    try:
        output = get_and_parse_cli_output(command)

        if not suppress_output:
            print("\nBGP RIB Failure Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)

        return output

    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
