from core.utils import get_and_parse_cli_output


def bgp_pending_prefixes(suppress_output=False, help_requested=False):
    """Retrieves and optionally displays the BGP pending prefixes using 'show bgp pending-prefixes'.
       If help_requested=True, it prints the help information instead.
    """

    bgp_pending_prefixes_help = {
        'command': 'show bgp pending-prefixes',
        'description': (
            "Displays prefixes that are pending advertisement to BGP neighbors. "
            "This helps in troubleshooting BGP advertisements and understanding which prefixes "
            "are currently queued for transmission to BGP peers."
        ),
        'example_output': """
Prefix               Neighbor
10.10.10.0/24        203.0.113.2
10.180.10.0/24       203.0.113.2
172.16.30.0/24       203.0.113.2
        """
    }

    # If help is requested, print help content and exit the function
    if help_requested:
        print("\n" + "-" * 80)
        print(f"Help for: {bgp_pending_prefixes_help['command']}".center(80))
        print("-" * 80)
        print(f"\n{bgp_pending_prefixes_help['description']}\n")
        print("Example Output:")
        print(bgp_pending_prefixes_help['example_output'])
        return None  # No actual command execution

    # Execute the BGP Pending Prefixes command
    command = "show bgp pending-prefixes"

    try:
        output = get_and_parse_cli_output(command)

        if not suppress_output:
            print("\nBGP Pending Prefixes Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)

        return output

    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
