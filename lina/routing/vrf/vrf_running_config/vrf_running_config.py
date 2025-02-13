from core.utils import get_and_parse_cli_output


def vrf_running_config(suppress_output=False, help_requested=False):
    """Retrieves and optionally displays the VRF running configuration using the
       'show running-config all vrf' command. If help_requested=True, it prints the help information instead.
    """

    vrf_running_config_help = {
        'command': 'show running-config all vrf',
        'description': (
            "Displays the full VRF running configuration, including defined VRFs, Route Distinguisher (RD) values, "
            "associated interfaces, and routing protocol settings per VRF. This command is essential for verifying "
            "VRF-based network segmentation."
        ),
        'example_output': """
VRF Running Configuration:

vrf definition VRF1
 rd 100:1
 !
 address-family ipv4
  route-target export 100:1
  route-target import 100:1
  exit-address-family
 !
vrf definition VRF2
 rd 200:1
 !
 address-family ipv4
  route-target export 200:1
  route-target import 200:1
  exit-address-family
        """
    }

    # If help is requested, print help content and exit the function
    if help_requested:
        print("\n" + "-" * 80)
        print(f"Help for: {vrf_running_config_help['command']}".center(80))
        print("-" * 80)
        print(f"\n{vrf_running_config_help['description']}\n")
        print("Example Output:")
        print(vrf_running_config_help['example_output'])
        return None  # No actual command execution

    # Execute the VRF Running Configuration command
    command = "show running-config all vrf"
    try:
        output = get_and_parse_cli_output(command)
        if not suppress_output:
            print("\nVRF Running Configuration Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)
        return output
    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
