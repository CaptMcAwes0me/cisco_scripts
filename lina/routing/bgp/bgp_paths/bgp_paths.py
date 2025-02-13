from core.utils import get_and_parse_cli_output


def bgp_paths(suppress_output=False, help_requested=False):
    """Retrieves and optionally displays the BGP paths using 'show bgp paths'.
       If help_requested=True, it prints the help information instead.
    """

    bgp_paths_help = {
        'command': 'show bgp paths',
        'description': (
            "Displays all BGP paths in the BGP table, showing how networks are reached via different AS paths. "
            "Useful for analyzing the available paths for a given prefix and for troubleshooting AS path selection."
        ),
        'example_output': """
Path #1: Received by speaker 0
Advertised to update-groups:
   1
200
  203.0.113.2 from 203.0.113.2 (203.0.113.2)
    Origin IGP, metric 0, localpref 100, valid, external, best
        """
    }

    # If help is requested, print help content and exit the function
    if help_requested:
        print("\n" + "-" * 80)
        print(f"Help for: {bgp_paths_help['command']}".center(80))
        print("-" * 80)
        print(f"\n{bgp_paths_help['description']}\n")
        print("Example Output:")
        print(bgp_paths_help['example_output'])
        return None  # No actual command execution

    # Execute the BGP Paths command
    command = "show bgp paths"

    try:
        output = get_and_parse_cli_output(command)

        if not suppress_output:
            print("\nBGP Paths Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)

        return output

    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
