from core.utils import get_and_parse_cli_output


def blocks_exhaustion_history(suppress_output=False, help_requested=False):
    """Retrieves and optionally displays the Blocks Exhaustion History using 'show blocks exhaustion history'."""

    blocks_exhaustion_history_help_info = {
        'command': 'show blocks exhaustion history',
        'description': (
            "Displays a history of memory block exhaustion events, including timestamps and block sizes "
            "that ran out of memory. This command is useful for diagnosing memory allocation issues and "
            "identifying patterns of memory depletion that may indicate a resource leak."
        )
    }

    # Handle help request
    if help_requested:
        print("\n" + "=" * 80)
        print(f"Help for: {blocks_exhaustion_history_help_info['command']}".center(80))
        print("=" * 80)
        print(f"\n{blocks_exhaustion_history_help_info['description']}\n")
        return None  # Do not execute the command

    command = "show blocks exhaustion history"

    try:
        output = get_and_parse_cli_output(command)

        if not suppress_output:
            print("\nBlocks Exhaustion History Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)

        return output

    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
