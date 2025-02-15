from core.utils import get_and_parse_cli_output

def failover_state(suppress_output=False, help_requested=False):
    """Retrieves and optionally displays the Failover State using 'show failover state'.
       If help_requested=True, it prints the help information instead.
    """

    failover_state_help = {
        'command': 'show failover state',
        'description': (
            "Displays the current failover state of the firewall, including its role (Primary/Secondary), "
            "whether it is Active or Standby, the last failure reason, and the failover communication state. "
            "This command helps verify high availability (HA) status and detect failover-related issues."
        ),
        'example_output': """
FTDv# show failover state

               State          Last Failure Reason      Date/Time
This host  -   Primary
               Active         None
Other host -   Secondary
               Standby Ready  Comm Failure             17:31:43 UTC Feb 14 2025

====Configuration State===
	Sync Skipped
====Communication State===
	Mac set
        """
    }

    # If help is requested, print help content and exit the function
    if help_requested:
        print("\n" + "=" * 80)
        print(f"📖 Help for: {failover_state_help['command']}".center(80))
        print("=" * 80)
        print(f"\n{failover_state_help['description']}\n")
        print("Example Output:")
        print(failover_state_help['example_output'])
        return None  # No actual command execution

    # Execute the Failover State command
    command = "show failover state"
    try:
        output = get_and_parse_cli_output(command)

        if not suppress_output:
            print("\nFailover State Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)

        return output

    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
