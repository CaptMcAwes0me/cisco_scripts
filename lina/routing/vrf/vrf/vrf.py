from core.utils import get_and_parse_cli_output

def vrf(suppress_output=False, help_requested=False):
    """Retrieves and optionally displays VRF information using the 'show vrf' command.
       If help_requested=True, it prints the help information instead.
    """

    vrf_help = {
        'command': 'show vrf',
        'description': (
            "Displays all configured VRFs, including their Route Distinguisher (RD) values, "
            "associated interfaces, and VRF-specific settings. This command is useful for verifying "
            "VRF configurations and debugging routing issues in multi-VRF environments."
        ),
        'example_output': """
VRF Table:

Name       RD            Interfaces
VRF1       100:1         GigabitEthernet0/1
VRF2       200:1         GigabitEthernet0/2
        """
    }

    # If help is requested, print help content and exit the function
    if help_requested:
        print("\n" + "-" * 80)
        print(f"Help for: {vrf_help['command']}".center(80))
        print("-" * 80)
        print(f"\n{vrf_help['description']}\n")
        print("Example Output:")
        print(vrf_help['example_output'])
        return None  # No actual command execution

    # Execute the VRF command
    command = "show vrf"
    try:
        output = get_and_parse_cli_output(command)
        if not suppress_output:
            print("\nVRF Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)
        return output
    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
