from core.utils import get_and_parse_cli_output

def ospf_statistics(suppress_output=False, help_requested=False):
    """Retrieves and optionally displays OSPF statistics using the 'show ospf statistics' command.
       If help_requested=True, it prints the help information instead.
    """

    ospf_statistics_help = {
        'command': 'show ospf statistics',
        'description': (
            "Displays various OSPF statistics, including packet counters, SPF calculations, "
            "LSA generation rates, and neighbor state changes. This command is useful for monitoring "
            "OSPF performance and diagnosing excessive protocol activity."
        ),
        'example_output': """
OSPF Statistics for Process ID 1

SPF Runs: 15
LSAs Received: 120
LSAs Generated: 30
Hello Packets Sent: 500
Hello Packets Received: 495
DB Description Packets Sent: 50
DB Description Packets Received: 50
        """
    }

    # If help is requested, print help content and exit the function
    if help_requested:
        print("\n" + "-" * 80)
        print(f"Help for: {ospf_statistics_help['command']}".center(80))
        print("-" * 80)
        print(f"\n{ospf_statistics_help['description']}\n")
        print("Example Output:")
        print(ospf_statistics_help['example_output'])
        return None  # No actual command execution

    # Execute the OSPF Statistics command
    command = "show ospf statistics"
    try:
        output = get_and_parse_cli_output(command)
        if not suppress_output:
            print("\nOSPF Statistics Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)
        return output
    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
