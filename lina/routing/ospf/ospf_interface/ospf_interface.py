from core.utils import get_and_parse_cli_output


def ospf_interface(suppress_output=False, help_requested=False):
    """Retrieves and optionally displays OSPF interface information using the 'show ospf interface' command.
       If help_requested=True, it prints the help information instead.
    """

    ospf_interface_help = {
        'command': 'show ospf interface',
        'description': (
            "Displays detailed OSPF interface information, including network type, cost, priority, "
            "Hello and Dead timers, and adjacency state. This command is useful for troubleshooting OSPF neighbor "
            "formation and verifying interface configurations."
        ),
        'example_output': """
OSPF Interface Information for Process ID 1

Interface    Area    Cost   State    Neighbors  Hello  Dead
Gi0/1        0       10     FULL     2          10     40
Gi0/2        0       20     DOWN     0          10     40
        """
    }

    # If help is requested, print help content and exit the function
    if help_requested:
        print("\n" + "-" * 80)
        print(f"Help for: {ospf_interface_help['command']}".center(80))
        print("-" * 80)
        print(f"\n{ospf_interface_help['description']}\n")
        print("Example Output:")
        print(ospf_interface_help['example_output'])
        return None  # No actual command execution

    # Execute the OSPF Interface command
    command = "show ospf interface"
    try:
        output = get_and_parse_cli_output(command)
        if not suppress_output:
            print("\nOSPF Interface Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)
        return output
    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
