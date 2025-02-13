from core.utils import get_and_parse_cli_output


def show_route_all(suppress_output=False, help_requested=False):
    """Retrieves and optionally displays all routes using the 'show route all' command.
       If help_requested=True, it prints the help information instead.
    """

    show_route_all_help = {
        'command': 'show route all',
        'description': (
            "Displays the full routing table, showing routes learned via different protocols "
            "(OSPF, BGP, EIGRP, ISIS, static). This command helps in verifying best paths and "
            "troubleshooting routing inconsistencies."
        ),
        'example_output': """
Routing Table:

Prefix              Next Hop          Interface        Protocol
10.1.1.0/24        192.168.1.2       GigabitEthernet0/1  OSPF
10.2.2.0/24        192.168.1.3       GigabitEthernet0/2  BGP
0.0.0.0/0          192.168.1.1       GigabitEthernet0/1  Static
        """
    }

    # If help is requested, print help content and exit the function
    if help_requested:
        print("\n" + "-" * 80)
        print(f"Help for: {show_route_all_help['command']}".center(80))
        print("-" * 80)
        print(f"\n{show_route_all_help['description']}\n")
        print("Example Output:")
        print(show_route_all_help['example_output'])
        return None  # No actual command execution

    # Execute the Show Route All command
    command = "show route all"
    try:
        output = get_and_parse_cli_output(command)
        if not suppress_output:
            print("\nRoute All Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)
        return output
    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
