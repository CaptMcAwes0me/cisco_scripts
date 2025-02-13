# Description: This script retrieves and displays EIGRP routing table.

from core.utils import get_and_parse_cli_output


def eigrp_routing_table(suppress_output=False, help_requested=False):
    """Retrieves and optionally displays EIGRP routing table using the 'show route all eigrp' command.
       If help_requested=True, it prints the help information instead.
    """

    eigrp_routing_table_help = {
        'command': 'show route all eigrp',
        'description': (
            "Displays the routing table entries learned via EIGRP. This command shows the EIGRP routes installed "
            "in the RIB, along with next-hop information, administrative distance, and metric values. "
            "It is useful for verifying the EIGRP-learned routes and troubleshooting routing issues."
        ),
        'example_output': """
EIGRP Routing Table for AS 100

D    10.10.10.0/24 [90/256000] via 192.168.1.2, 00:12:45, GigabitEthernet0/1
D    192.168.2.0/24 [90/28160] via 192.168.1.3, 00:08:21, GigabitEthernet0/2
D    172.16.30.0/24 [90/512000] via 192.168.1.4, 00:05:10, GigabitEthernet0/3
        """
    }

    # If help is requested, print help content and exit the function
    if help_requested:
        print("\n" + "-" * 80)
        print(f"Help for: {eigrp_routing_table_help['command']}".center(80))
        print("-" * 80)
        print(f"\n{eigrp_routing_table_help['description']}\n")
        print("Example Output:")
        print(eigrp_routing_table_help['example_output'])
        return None  # No actual command execution

    # Execute the EIGRP Routing Table command
    command = "show route all eigrp"

    try:
        output = get_and_parse_cli_output(command)

        # Conditionally print the output
        if not suppress_output:
            print("\nEIGRP Routing Table Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)

        return output

    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
