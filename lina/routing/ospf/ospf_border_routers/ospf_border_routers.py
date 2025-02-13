from core.utils import get_and_parse_cli_output


def ospf_border_routers(suppress_output=False, help_requested=False):
    """Retrieves and optionally displays OSPF border routers using the 'show ospf border-routers' command.
       If help_requested=True, it prints the help information instead.
    """

    ospf_border_routers_help = {
        'command': 'show ospf border-routers',
        'description': (
            "Displays information about OSPF border routers, including Autonomous System Border Routers (ASBRs) "
            "and Area Border Routers (ABRs). This command helps in verifying inter-area and external route distribution."
        ),
        'example_output': """
OSPF Border Routers for Process ID 1

  Type   Router ID     Advertising Router      Path Type      Cost
  ABR    192.168.1.2   192.168.1.2             intra-area     10
  ASBR   192.168.2.1   192.168.2.1             E2             20
        """
    }

    # If help is requested, print help content and exit the function
    if help_requested:
        print("\n" + "-" * 80)
        print(f"Help for: {ospf_border_routers_help['command']}".center(80))
        print("-" * 80)
        print(f"\n{ospf_border_routers_help['description']}\n")
        print("Example Output:")
        print(ospf_border_routers_help['example_output'])
        return None  # No actual command execution

    # Execute the OSPF Border Routers command
    command = "show ospf border-routers"
    try:
        output = get_and_parse_cli_output(command)
        if not suppress_output:
            print("\nOSPF Border Routers Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)
        return output
    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
