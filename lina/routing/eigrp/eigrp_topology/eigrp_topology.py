# Description: This script retrieves and displays EIGRP topology.

from core.utils import get_and_parse_cli_output


def eigrp_topology(suppress_output=False, help_requested=False):
    """Retrieves and optionally displays EIGRP topology using the 'show eigrp topology' command.
       If help_requested=True, it prints the help information instead.
    """

    eigrp_topology_help = {
        'command': 'show eigrp topology',
        'description': (
            "Displays the EIGRP topology table, which includes feasible successors, successors, and advertised distances. "
            "This command helps in verifying route calculations and ensuring alternate paths exist for redundancy."
        ),
        'example_output': """
EIGRP Topology Table for AS 100

P 10.10.10.0/24, 1 successors, FD is 256000
    via 192.168.1.2 (256000/128000), GigabitEthernet0/1
P 192.168.1.0/24, 1 successors, FD is 28160
    via Connected, GigabitEthernet0/1
        """
    }

    # If help is requested, print help content and exit the function
    if help_requested:
        print("\n" + "-" * 80)
        print(f"Help for: {eigrp_topology_help['command']}".center(80))
        print("-" * 80)
        print(f"\n{eigrp_topology_help['description']}\n")
        print("Example Output:")
        print(eigrp_topology_help['example_output'])
        return None  # No actual command execution

    # Execute the EIGRP Topology command
    command = "show eigrp topology"

    try:
        output = get_and_parse_cli_output(command)

        # Conditionally print the output
        if not suppress_output:
            print("\nEIGRP Topology Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)

        return output

    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
