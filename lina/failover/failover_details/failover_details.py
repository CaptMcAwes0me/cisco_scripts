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
		Active time: 19114 (sec)
		slot 0: FTD hw/sw rev (/9.18(4)47) status (Up Sys)
		  Interface outside (192.168.0.1): Normal (Waiting)
		  Interface inside (192.168.1.1): Normal (Waiting)
		  Interface diagnostic (0.0.0.0): Normal (Waiting)
		slot 1: snort rev (1.0)  status (up)
		snort poll success:18962 miss:0
		slot 2: diskstatus rev (1.0)  status (up)

		disk poll success:18962 miss:0
	Other host: Secondary - App Sync
		Active time: 0 (sec)
		  Interface outside (0.0.0.0): Unknown (Waiting)
		  Interface inside (0.0.0.0): Unknown (Waiting)
		  Interface diagnostic (0.0.0.0): Unknown (Waiting)
		slot 1: snort rev (1.0)  status (up)
		peer snort poll success:18962 miss:0
		slot 2: diskstatus rev (1.0)  status (up)

		peer disk poll success:18962 miss:0
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
