from core.utils import get_and_parse_cli_output


def ospf_all(suppress_output=False, help_requested=False):
    """Retrieves and optionally displays OSPF all information using the 'show ospf all' command.
       If help_requested=True, it prints the help information instead.
    """

    ospf_all_help = {
        'command': 'show ospf all',
        'description': (
            "Displays a comprehensive summary of OSPF status, including router ID, process ID, areas, "
            "neighbor relationships, and general OSPF operational details. This command is useful for getting "
            "a complete OSPF overview in a single output."
        ),
        'example_output': """
OSPF Process ID 1 VRF default
Router ID 192.168.1.1
Number of areas: 1
Area 0: Number of interfaces: 2
SPF Runs: 10
LSA Count: 20
Neighbor Count: 3
        """
    }

    # If help is requested, print help content and exit the function
    if help_requested:
        print("\n" + "-" * 80)
        print(f"Help for: {ospf_all_help['command']}".center(80))
        print("-" * 80)
        print(f"\n{ospf_all_help['description']}\n")
        print("Example Output:")
        print(ospf_all_help['example_output'])
        return None  # No actual command execution

    # Execute the OSPF All command
    command = "show ospf all"
    try:
        output = get_and_parse_cli_output(command)
        if not suppress_output:
            print("\nOSPF All Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)
        return output
    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
