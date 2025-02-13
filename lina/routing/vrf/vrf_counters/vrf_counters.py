from core.utils import get_and_parse_cli_output


def vrf_counters(suppress_output=False, help_requested=False):
    """Retrieves and optionally displays VRF counters using the 'show vrf counters' command.
       If help_requested=True, it prints the help information instead.
    """

    vrf_counters_help = {
        'command': 'show vrf counters',
        'description': (
            "Displays VRF-related traffic counters, including packet and byte statistics per VRF. "
            "This command helps in monitoring traffic flow between VRFs and diagnosing connectivity issues."
        ),
        'example_output': """
VRF Counters:

VRF Name        In-Packets    In-Bytes     Out-Packets   Out-Bytes  
VRF1            12345         6789012      23456         8901234
VRF2            54321         2345678      65432         4567890
        """
    }

    # If help is requested, print help content and exit the function
    if help_requested:
        print("\n" + "-" * 80)
        print(f"Help for: {vrf_counters_help['command']}".center(80))
        print("-" * 80)
        print(f"\n{vrf_counters_help['description']}\n")
        print("Example Output:")
        print(vrf_counters_help['example_output'])
        return None  # No actual command execution

    # Execute the VRF Counters command
    command = "show vrf counters"
    try:
        output = get_and_parse_cli_output(command)
        if not suppress_output:
            print("\nVRF Counters Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)
        return output
    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
