# Description: This script retrieves and displays EIGRP interfaces.

from core.utils import get_and_parse_cli_output


def eigrp_interfaces(suppress_output=False, help_requested=False):
    """Retrieves and optionally displays EIGRP interfaces using the 'show eigrp interfaces' command.
       If help_requested=True, it prints the help information instead.
    """

    eigrp_interfaces_help = {
        'command': 'show eigrp interfaces',
        'description': (
            "Displays all interfaces participating in the EIGRP process, along with key attributes "
            "such as bandwidth, delay, and Hello interval settings. Useful for verifying EIGRP interface status and "
            "troubleshooting adjacency issues."
        ),
        'example_output': """
EIGRP interfaces for process 100

Interface       Peers   Xmit Queue  Mean SRTT  Pacing Time  Multicast Flow Timer
Gi0/1           2       0/0         12        0            0
Gi0/2           1       0/0         20        0            0
        """
    }

    # If help is requested, print help content and exit the function
    if help_requested:
        print("\n" + "-" * 80)
        print(f"Help for: {eigrp_interfaces_help['command']}".center(80))
        print("-" * 80)
        print(f"\n{eigrp_interfaces_help['description']}\n")
        print("Example Output:")
        print(eigrp_interfaces_help['example_output'])
        return None  # No actual command execution

    # Execute the EIGRP Interfaces command
    command = "show eigrp interfaces"

    try:
        output = get_and_parse_cli_output(command)

        # Conditionally print the output
        if not suppress_output:
            print("\nEIGRP Interfaces Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)

        return output

    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
