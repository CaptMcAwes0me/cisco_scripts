from core.utils import get_and_parse_cli_output


def failover_interface(suppress_output=False, help_requested=False):
    """Retrieves and optionally displays failover interface status using 'show failover interface'.
       If help_requested=True, it prints the help information instead.
    """

    failover_interface_help = {
        'command': 'show failover interface',
        'description': (
            "Displays the detailed status of failover-enabled interfaces, including operational state, link status, "
            "interface names, IP addresses, monitored status, and last detected failures. "
            "This command is useful for troubleshooting failover-related connectivity issues."
        ),
        'example_output': """
FTDv# show failover interface

Failover LAN Interface: failover GigabitEthernet0/2 (up)
   Link Status: Up
   IP Address: 192.168.255.1
   Peer IP Address: 192.168.255.2

Monitored Interfaces:
   Interface OUTSIDE (192.168.1.1)   : Normal
   Interface INSIDE (192.168.2.1)    : Normal
   Interface DMZ (192.168.3.1)       : FAILED (Waiting)
   Last interface failure at: 17:21:43 UTC Feb 14 2025
        """
    }

    # If help is requested, print help content and exit the function
    if help_requested:
        print("\n" + "=" * 80)
        print(f"📖 Help for: {failover_interface_help['command']}".center(80))
        print("=" * 80)
        print(f"\n{failover_interface_help['description']}\n")
        print("Example Output:")
        print(failover_interface_help['example_output'])
        return None  # No actual command execution

    # Execute the Failover Interface command
    command = "show failover interface"
    try:
        output = get_and_parse_cli_output(command)

        if not suppress_output:
            print("\nFailover Interface Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)

        return output

    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
