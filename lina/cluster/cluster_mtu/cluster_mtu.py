from core.utils import get_and_parse_cli_output

def cluster_mtu(suppress_output=False, help_requested=False):
    """
    Retrieves and optionally displays the All MTUs Configured using 'show running-config | include mtu'.
    If help_requested=True, it prints command information instead of executing the command.
    """

    cluster_mtu_help = {
        'command': 'show running-config mtu',
        'description': (
            "Displays the configured Maximum Transmission Unit (MTU) settings for all interfaces, including "
            "the Cluster Control Link (CCL). Proper MTU configuration ensures efficient packet transmission "
            "without fragmentation. The CCL MTU should be set at least 100 bytes larger than data interfaces "
            "to ensure stable cluster communication."
        ),
        'example_output': """
firepower# show running-config | include mtu
mtu inside 1500
mtu outside 1500
mtu dmz 1400
mtu Cluster-Interface 1600
        """
    }

    # If help is requested, print help content and exit the function
    if help_requested:
        print("\n" + "=" * 80)
        print(f"Help for: {cluster_mtu_help['command']}".center(80))
        print("=" * 80)
        print(f"\n{cluster_mtu_help['description']}\n")
        print("Example Output:")
        print(cluster_mtu_help['example_output'])
        return None  # No actual command execution

    # Execute command to retrieve MTU settings
    command = "show running-config mtu"

    try:
        output = get_and_parse_cli_output(command)

        if not suppress_output:
            print("\nAll MTUs Configured Output:")
            print("=" * 80)
            print(output)
            print("=" * 80)
            print(
                "⚠️ The Cluster Control Link (CCL) MTU should be at least **100 bytes larger** than "
                "the Data Interface MTUs to ensure stable cluster communication and prevent packet fragmentation. ⚠️ \n"
            )

        return output

    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
