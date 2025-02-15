from core.utils import get_and_parse_cli_output


def failover_descriptor(suppress_output=False, help_requested=False):
    """Retrieves and optionally displays failover descriptor information using 'show failover descriptor'.
       If help_requested=True, it prints the help information instead.
    """

    failover_descriptor_help = {
        'command': 'show failover descriptor',
        'description': (
            "Displays detailed information about the failover descriptors, including the local unit's descriptor, "
            "peer descriptor, and stateful failover descriptor. This command is useful for verifying the sync state "
            "between failover units."
        ),
        'example_output': """
FTDv# show failover descriptor

Failover Descriptor Information:
   Local Descriptor:  FTDv-Primary (Up)
   Peer Descriptor:   FTDv-Secondary (Up)
   Stateful Failover Descriptor: Active
        """
    }

    # If help is requested, print help content and exit the function
    if help_requested:
        print("\n" + "=" * 80)
        print(f"📖 Help for: {failover_descriptor_help['command']}".center(80))
        print("=" * 80)
        print(f"\n{failover_descriptor_help['description']}\n")
        print("Example Output:")
        print(failover_descriptor_help['example_output'])
        return None  # No actual command execution

    # Execute the Failover Descriptor command
    command = "show failover descriptor"
    try:
        output = get_and_parse_cli_output(command)

        if not suppress_output:
            print("\nFailover Descriptor Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)

        return output

    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
