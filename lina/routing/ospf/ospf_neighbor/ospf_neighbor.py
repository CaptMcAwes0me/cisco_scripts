from core.utils import get_and_parse_cli_output


def ospf_neighbor(suppress_output=False, help_requested=False):
    """Retrieves and optionally displays OSPF neighbor information using the 'show ospf neighbor' command.
       If help_requested=True, it prints the help information instead.
    """

    ospf_neighbor_help = {
        'command': 'show ospf neighbor',
        'description': (
            "Displays information about OSPF neighbors, including their state, priority, designated router (DR), "
            "backup designated router (BDR), and interface details. This command is useful for diagnosing adjacency "
            "formation and verifying neighbor relationships."
        ),
        'example_output': """
OSPF Neighbor Information for Process ID 1

Neighbor ID     Priority  State   Dead Time   Address        Interface
192.168.1.2     1         FULL    00:00:39    10.0.0.2       GigabitEthernet0/1
192.168.1.3     0         2WAY    00:00:36    10.0.0.3       GigabitEthernet0/2
        """
    }

    # If help is requested, print help content and exit the function
    if help_requested:
        print("\n" + "-" * 80)
        print(f"Help for: {ospf_neighbor_help['command']}".center(80))
        print("-" * 80)
        print(f"\n{ospf_neighbor_help['description']}\n")
        print("Example Output:")
        print(ospf_neighbor_help['example_output'])
        return None  # No actual command execution

    # Execute the OSPF Neighbor command
    command = "show ospf neighbor"
    try:
        output = get_and_parse_cli_output(command)
        if not suppress_output:
            print("\nOSPF Neighbor Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)
        return output
    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
