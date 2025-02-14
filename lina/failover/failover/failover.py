from core.utils import get_and_parse_cli_output


def failover(suppress_output=False, help_requested=False):
    """Retrieves and optionally displays the Failover status using 'show failover'.
       If help_requested=True, it prints the help information instead.
    """

    failover_help = {
        'command': 'show failover',
        'description': (
            "Displays detailed failover status, including unit roles (Primary/Secondary), active/standby state, "
            "failover mode (LAN-based, Stateful), statistics, sync status, and interface monitoring results. "
            "This command helps diagnose HA synchronization issues, state transitions, and interface failures."
        ),
        'example_output': """
FTDv# show failover

Failover On
Failover unit Primary
Failover LAN Interface: failover GigabitEthernet0/2 (up)
Unit Poll frequency 1 seconds, holdtime 15 seconds
Interface Poll frequency 5 seconds, holdtime 25 seconds
Interface Policy 1
Monitored Interfaces 3 of 3 total, 1 failed
   Outside (192.168.1.1): Normal
   Inside (192.168.2.1): Normal
   DMZ (192.168.3.1): FAILED (Waiting)
This host: Primary - Active
   Active time: 14 (sec)
   slot 0: ASA5516 up, mate ASA5516 up
   Stateful Failover Logical Update Statistics
      Link: failover GigabitEthernet0/2 (up)
      Stateful Obj xmit xerr rcv rerr
         TCP 1000 0 1000 0
         UDP 500 0 500 0
         ICMP 50 0 50 0
Other host: Secondary - Standby Ready
   Active time: 0 (sec)
    """
    }

    # If help is requested, print help content and exit the function
    if help_requested:
        print("\n" + "=" * 80)
        print(f"📖 Help for: {failover_help['command']}".center(80))
        print("=" * 80)
        print(f"\n{failover_help['description']}\n")
        print("Example Output:")
        print(failover_help['example_output'])
        return None  # No actual command execution

    # Execute the Failover command
    command = "show failover"
    try:
        output = get_and_parse_cli_output(command)

        if not suppress_output:
            print("\nFailover Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)

        return output

    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
