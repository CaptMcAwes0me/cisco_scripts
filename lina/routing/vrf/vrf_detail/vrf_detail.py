from core.utils import get_and_parse_cli_output


def vrf_detail(suppress_output=False, help_requested=False):
    """Retrieves and optionally displays detailed VRF information using the 'show vrf detail' command.
       If help_requested=True, it prints the help information instead.
    """

    vrf_detail_help = {
        'command': 'show vrf detail',
        'description': (
            "Displays detailed VRF information, including VRF Route Distinguisher (RD), Route Target (RT) import/export policies, "
            "associated interfaces, and additional protocol-specific details. This command is useful for verifying VRF-based "
            "segmentation, ensuring correct routing policies, and troubleshooting reachability between VRFs."
        ),
        'example_output': """
VRF Detailed Information:

VRF: VRF1 (VRF ID = 1); default RD 100:1; default VPN ID not present
 Interfaces:
   GigabitEthernet0/1
 Address-family ipv4 unicast:
   Import VPN Targets: 
     100:1
   Export VPN Targets:
     100:1
   No global export VPN target
 Address-family ipv6 unicast:
   Import VPN Targets:
     100:1
   Export VPN Targets:
     100:1
        """
    }

    # If help is requested, print help content and exit the function
    if help_requested:
        print("\n" + "-" * 80)
        print(f"Help for: {vrf_detail_help['command']}".center(80))
        print("-" * 80)
        print(f"\n{vrf_detail_help['description']}\n")
        print("Example Output:")
        print(vrf_detail_help['example_output'])
        return None  # No actual command execution

    # Execute the VRF Detail command
    command = "show vrf detail"
    try:
        output = get_and_parse_cli_output(command)
        if not suppress_output:
            print("\nVRF Detail Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)
        return output
    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
