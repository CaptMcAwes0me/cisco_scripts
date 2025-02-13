from core.utils import get_and_parse_cli_output

def ospf_traffic(suppress_output=False, help_requested=False):
    """Retrieves and optionally displays OSPF traffic information using the 'show ospf traffic' command.
       If help_requested=True, it prints the help information instead.
    """

    ospf_traffic_help = {
        'command': 'show ospf traffic',
        'description': (
            "Displays OSPF packet exchange statistics, including Hello, Database Description (DBD), "
            "Link-State Request (LSR), Link-State Update (LSU), and Link-State Acknowledgment (LSAck) packets. "
            "This command helps in diagnosing OSPF network activity and detecting excessive traffic issues."
        ),
        'example_output': """
OSPF Traffic Statistics for Process ID 1

Hello Packets Sent/Received: 1200 / 1185
DBD Packets Sent/Received: 60 / 58
LSR Packets Sent/Received: 30 / 32
LSU Packets Sent/Received: 80 / 75
LSAck Packets Sent/Received: 55 / 53
Input Queue: 0 messages, 0 drops
Output Queue: 0 messages, 0 drops
        """
    }

    # If help is requested, print help content and exit the function
    if help_requested:
        print("\n" + "-" * 80)
        print(f"Help for: {ospf_traffic_help['command']}".center(80))
        print("-" * 80)
        print(f"\n{ospf_traffic_help['description']}\n")
        print("Example Output:")
        print(ospf_traffic_help['example_output'])
        return None  # No actual command execution

    # Execute the OSPF Traffic command
    command = "show ospf traffic"
    try:
        output = get_and_parse_cli_output(command)
        if not suppress_output:
            print("\nOSPF Traffic Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)
        return output
    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
