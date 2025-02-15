from core.utils import get_and_parse_cli_output


def blocks_exhaustion_snapshot(suppress_output=False, help_requested=False):
    """Retrieves and optionally displays the Blocks Exhaustion Snapshot using 'show blocks exhaustion snapshot'."""

    blocks_exhaustion_snapshot_help_info = {
        'command': 'show blocks exhaustion snapshot',
        'description': (
            "Provides a real-time snapshot of memory block exhaustion, showing the most recent occurrences "
            "of memory block depletion. This command is useful for identifying sudden memory usage spikes, "
            "tracking memory fragmentation, and detecting abnormal resource consumption."
        )
    }

    # Handle help request
    if help_requested:
        print("\n" + "=" * 80)
        print(f"Help for: {blocks_exhaustion_snapshot_help_info['command']}".center(80))
        print("=" * 80)
        print(f"\n{blocks_exhaustion_snapshot_help_info['description']}\n")
        return None  # Do not execute the command

    command = "show blocks exhaustion snapshot"

    try:
        output = get_and_parse_cli_output(command)

        if not suppress_output:
            print("\nBlocks Exhaustion Snapshot Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)

        return output

    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
