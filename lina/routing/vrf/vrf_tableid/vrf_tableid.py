from core.utils import get_and_parse_cli_output


def vrf_tableid(suppress_output=False, help_requested=False):
    """Retrieves and optionally displays VRF table ID using the 'show vrf tableid' command.
       If help_requested=True, it prints the help information instead.
    """

    vrf_tableid_help = {
        'command': 'show vrf tableid',
        'description': (
            "Displays the VRF table ID, which is used internally by the system for routing "
            "and forwarding. Each VRF is assigned a unique table ID that differentiates it "
            "from other VRFs and helps maintain separate routing instances. This command is "
            "useful for troubleshooting route lookups and verifying VRF assignments."
        ),
        'example_output': """
VRF Table ID Information:

VRF Name        Table ID
VRF1            1001
VRF2            1002
        """
    }

    # If help is requested, print help content and exit the function
    if help_requested:
        print("\n" + "-" * 80)
        print(f"Help for: {vrf_tableid_help['command']}".center(80))
        print("-" * 80)
        print(f"\n{vrf_tableid_help['description']}\n")
        print("Example Output:")
        print(vrf_tableid_help['example_output'])
        return None  # No actual command execution

    # Execute the VRF Table ID command
    command = "show vrf tableid"
    try:
        output = get_and_parse_cli_output(command)
        if not suppress_output:
            print("\nVRF Table ID Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)
        return output
    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
