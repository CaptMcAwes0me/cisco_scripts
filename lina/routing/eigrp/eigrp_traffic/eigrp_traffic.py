# Description: This script retrieves and displays EIGRP traffic.

from core.utils import get_and_parse_cli_output


def eigrp_traffic(suppress_output=False, help_requested=False):
    """Retrieves and optionally displays EIGRP traffic using the 'show eigrp traffic' command.
       If help_requested=True, it prints the help information instead.
    """

    eigrp_traffic_help = {
        'command': 'show eigrp traffic',
        'description': (
            "Displays statistics on EIGRP packet exchanges, including Hello, Update, Query, and Reply messages. "
            "This command is useful for monitoring EIGRP activity and diagnosing excessive traffic issues."
        ),
        'example_output': """
EIGRP Traffic Statistics for AS 100

Hello packets sent/received: 120/118
Update packets sent/received: 40/38
Query packets sent/received: 5/4
Reply packets sent/received: 4/4
ACK packets sent/received: 40/38
Input queue: 0 messages, 0 drops
Output queue: 0 messages, 0 drops
        """
    }

    # If help is requested, print help content and exit the function
    if help_requested:
        print("\n" + "-" * 80)
        print(f"Help for: {eigrp_traffic_help['command']}".center(80))
        print("-" * 80)
        print(f"\n{eigrp_traffic_help['description']}\n")
        print("Example Output:")
        print(eigrp_traffic_help['example_output'])
        return None  # No actual command execution

    # Execute the EIGRP Traffic command
    command = "show eigrp traffic"

    try:
        output = get_and_parse_cli_output(command)

        # Conditionally print the output
        if not suppress_output:
            print("\nEIGRP Traffic Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)

        return output

    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
