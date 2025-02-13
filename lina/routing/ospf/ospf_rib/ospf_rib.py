from core.utils import get_and_parse_cli_output


def ospf_rib(suppress_output=False, help_requested=False):
    """Retrieves and optionally displays OSPF RIB (Routing Information Base) using the 'show ospf rib' command.
       If help_requested=True, it prints the help information instead.
    """

    ospf_rib_help = {
        'command': 'show ospf rib',
        'description': (
            "Displays the OSPF Routing Information Base (RIB), which contains the best OSPF-learned routes "
            "installed in the routing table. This command is useful for verifying which OSPF routes are actively "
            "being used and troubleshooting route selection."
        ),
        'example_output': """
OSPF RIB for Process ID 1

Prefix           Next Hop        Interface        Metric  Type
10.10.10.0/24   192.168.1.2     Gi0/1            20      intra-area
192.168.2.0/24  192.168.1.3     Gi0/2            30      inter-area
        """
    }

    # If help is requested, print help content and exit the function
    if help_requested:
        print("\n" + "-" * 80)
        print(f"Help for: {ospf_rib_help['command']}".center(80))
        print("-" * 80)
        print(f"\n{ospf_rib_help['description']}\n")
        print("Example Output:")
        print(ospf_rib_help['example_output'])
        return None  # No actual command execution

    # Execute the OSPF RIB command
    command = "show ospf rib"
    try:
        output = get_and_parse_cli_output(command)
        if not suppress_output:
            print("\nOSPF RIB Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)
        return output
    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
