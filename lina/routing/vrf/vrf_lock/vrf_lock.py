from core.utils import get_and_parse_cli_output


def vrf_lock(suppress_output=False, help_requested=False):
    """Retrieves and optionally displays VRF lock status using the 'show vrf lock' command.
       If help_requested=True, it prints the help information instead.
    """

    vrf_lock_help = {
        'command': 'show vrf lock',
        'description': (
            "Displays information about VRF locking mechanisms used for route table consistency. "
            "VRF locks prevent unintended changes to routing instances that could cause inconsistencies "
            "in the forwarding table. This command helps in identifying locked VRFs and debugging issues "
            "related to route updates or deletions."
        ),
        'example_output': """
VRF Lock Status:

VRF Name        Locked Status
VRF1            Locked
VRF2            Unlocked
        """
    }

    # If help is requested, print help content and exit the function
    if help_requested:
        print("\n" + "-" * 80)
        print(f"Help for: {vrf_lock_help['command']}".center(80))
        print("-" * 80)
        print(f"\n{vrf_lock_help['description']}\n")
        print("Example Output:")
        print(vrf_lock_help['example_output'])
        return None  # No actual command execution

    # Execute the VRF Lock command
    command = "show vrf lock"
    try:
        output = get_and_parse_cli_output(command)
        if not suppress_output:
            print("\nVRF Lock Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)
        return output
    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
