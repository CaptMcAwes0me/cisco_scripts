from core.utils import get_and_parse_cli_output


def ospf_nsf(suppress_output=False, help_requested=False):
    """Retrieves and optionally displays OSPF NSF (Non-Stop Forwarding) information using the 'show ospf nsf' command.
       If help_requested=True, it prints the help information instead.
    """

    ospf_nsf_help = {
        'command': 'show ospf nsf',
        'description': (
            "Displays the Non-Stop Forwarding (NSF) status for OSPF. NSF allows a router to continue forwarding traffic "
            "while its OSPF process restarts, reducing downtime. This command helps verify NSF status and detect issues "
            "related to graceful OSPF recovery."
        ),
        'example_output': """
OSPF NSF Information for Process ID 1

Router ID       NSF Enabled   NSF Helper Mode   NSF Recovery
192.168.1.1     Yes           Yes               Successful
192.168.1.2     Yes           No                N/A
        """
    }

    # If help is requested, print help content and exit the function
    if help_requested:
        print("\n" + "-" * 80)
        print(f"Help for: {ospf_nsf_help['command']}".center(80))
        print("-" * 80)
        print(f"\n{ospf_nsf_help['description']}\n")
        print("Example Output:")
        print(ospf_nsf_help['example_output'])
        return None  # No actual command execution

    # Execute the OSPF NSF command
    command = "show ospf nsf"
    try:
        output = get_and_parse_cli_output(command)
        if not suppress_output:
            print("\nOSPF NSF Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)
        return output
    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
