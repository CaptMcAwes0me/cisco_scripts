# Description: This script retrieves and displays EIGRP neighbors.

from core.utils import get_and_parse_cli_output


def eigrp_neighbors(suppress_output=False, help_requested=False):
    """Retrieves and optionally displays EIGRP neighbors using the 'show eigrp neighbors' command.
       If help_requested=True, it prints the help information instead.
    """

    eigrp_neighbors_help = {
        'command': 'show eigrp neighbors',
        'description': (
            "Displays all active EIGRP neighbors, their hold time, uptime, and interface. "
            "This command is essential for verifying neighbor adjacencies and troubleshooting EIGRP connectivity issues."
        ),
        'example_output': """
EIGRP Neighbors for AS 100

H Address         Interface       Hold Time  Uptime     SRTT   RTO   Q C
0 192.168.1.2     Gi0/1           12         00:12:45   10     50    0 0
1 192.168.1.3     Gi0/2           14         00:08:21   15     75    0 0
        """
    }

    # If help is requested, print help content and exit the function
    if help_requested:
        print("\n" + "-" * 80)
        print(f"Help for: {eigrp_neighbors_help['command']}".center(80))
        print("-" * 80)
        print(f"\n{eigrp_neighbors_help['description']}\n")
        print("Example Output:")
        print(eigrp_neighbors_help['example_output'])
        return None  # No actual command execution

    # Execute the EIGRP Neighbors command
    command = "show eigrp neighbors"

    try:
        output = get_and_parse_cli_output(command)

        # Conditionally print the output
        if not suppress_output:
            print("\nEIGRP Neighbors Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)

        return output

    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
