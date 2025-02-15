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
Failover LAN Interface: fover GigabitEthernet0/7 (up)
Reconnect timeout 0:00:00
Unit Poll frequency 1 seconds, holdtime 15 seconds
Interface Poll frequency 5 seconds, holdtime 25 seconds
Interface Policy 1
Monitored Interfaces 3 of 1285 maximum
MAC Address Move Notification Interval not set
failover replication http
Version: Ours 9.18(4)47, Mate 9.18(4)47
Serial Number: Ours SN, Mate SN
Last Failover at: 14:15:10 UTC Feb 14 2025
	This host: Primary - Active
		Active time: 19314 (sec)
		slot 0: FTD hw/sw rev (/9.18(4)47) status (Up Sys)
		  Interface outside (192.168.0.1): Normal (Waiting)
		  Interface inside (192.168.1.1): Normal (Waiting)
		  Interface diagnostic (0.0.0.0): Normal (Waiting)
		slot 1: snort rev (1.0)  status (up)
		slot 2: diskstatus rev (1.0)  status (up)
	Other host: Secondary - Failed
		Active time: 0 (sec)
		  Interface outside (0.0.0.0): Unknown (Waiting)
		  Interface inside (0.0.0.0): Unknown (Waiting)
		  Interface diagnostic (0.0.0.0): Unknown (Waiting)
		slot 1: snort rev (1.0)  status (up)
		slot 2: diskstatus rev (1.0)  status (up)
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
