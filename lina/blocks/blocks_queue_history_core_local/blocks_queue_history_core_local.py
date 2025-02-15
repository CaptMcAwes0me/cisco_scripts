from core.utils import get_and_parse_cli_output


def blocks_queue_history_core_local(suppress_output=False, help_requested=False):
    """Retrieves and optionally displays the Blocks Queue History Core Local using 'show blocks history core-local'."""

    blocks_queue_history_core_local_help_info = {
        'command': 'show blocks queue history core-local',
        'description': (
            "Displays the history of memory block allocations and deallocations for the local core. "
            "This command is useful for monitoring memory block usage trends, identifying resource leaks, "
            "and troubleshooting memory allocation failures."
        )
    }

    # Handle help request
    if help_requested:
        print("\n" + "=" * 80)
        print(f"Help for: {blocks_queue_history_core_local_help_info['command']}".center(80))
        print("=" * 80)
        print(f"\n{blocks_queue_history_core_local_help_info['description']}\n")
        return None  # Do not execute the command

    command = "show blocks queue history core-local"

    try:
        output = get_and_parse_cli_output(command)

        if not suppress_output:
            print("\nBlocks Queue History Core Local Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)

        return output

    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
