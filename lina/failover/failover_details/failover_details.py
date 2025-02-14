from core.utils import get_and_parse_cli_output


def failover_details(suppress_output=False, help_requested=False):
    """Retrieves and optionally displays detailed Failover information using 'show failover details'.
       If help_requested=True, it prints the help information instead.
    """

    failover_details_help = {
        'command': 'show failover details',
        'description': (
            "Displays detailed failover status, including unit roles (Primary/Secondary), active/standby state, "
            "failover mode (LAN-based, Stateful), sync status, monitored interfaces, failover reason, and uptime. "
            "This command provides deeper insight into HA synchronization issues, failover transitions, and interface health."
        ),
        'example_output': """
FTDv# show failover details

Failover On
Failover unit Primary
Failover LAN Interface: failover GigabitEthernet0/2 (up)
Unit Poll frequency 1 seconds, holdtime 15 seconds
Interface Poll frequency 5 seconds, holdtime 25 seconds
Monitored Interfaces 3 of 3 total, 1 failed
   Outside (192.168.1.1): Normal
   Inside (192.168.2.1): Normal
   DMZ (192.168.3.1): FAILED (Waiting)
This host: Primary - Active
   Active time: 1h 10m 15s
   slot 0: ASA5516 up, mate ASA5516 up
   Last Failover at: 17:21:43 UTC Feb 14 2025
   Last Failover Reason: Interface Failure
   Stateful Failover Logical Update Statistics
      Link: failover GigabitEthernet0/2 (up)
      Stateful Obj xmit xerr rcv rerr
         TCP 1500 0 1500 0
         UDP 750 0 750 0
         ICMP 100 0 100 0
Other host: Secondary - Standby Ready
   Active time: 0 (sec)
        """
    }

    # If help is requested, print help content and exit the function
    if help_requested:
        print("\n" + "=" * 80)
        print(f"📖 Help for: {failover_details_help['command']}".center(80))
        print("=" * 80)
        print(f"\n{failover_details_help['description']}\n")
        print("Example Output:")
        print(failover_details_help['example_output'])
        return None  # No actual command execution

    # Execute the Failover Details command
    command = "show failover details"
    try:
        output = get_and_parse_cli_output(command)

        if not suppress_output:
            print("\nFailover Details Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)

        return output

    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
