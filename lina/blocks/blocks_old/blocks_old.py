from core.utils import get_and_parse_cli_output


def blocks_old(suppress_output=False, help_requested=False):
    """Retrieves and optionally displays the Blocks Old using 'show blocks old'."""

    blocks_old_help_info = {
        'command': 'show blocks old',
        'description': (
            "Displays a snapshot of the oldest allocated memory blocks in the system. "
            "This command helps in identifying memory fragmentation and diagnosing potential "
            "memory leaks by tracking which blocks have been held for an extended period."
        )
    }

    # Handle help request
    if help_requested:
        print("\n" + "=" * 80)
        print(f"Help for: {blocks_old_help_info['command']}".center(80))
        print("=" * 80)
        print(f"\n{blocks_old_help_info['description']}\n")
        return None  # Do not execute the command

    command = "show blocks old"

    try:
        output = get_and_parse_cli_output(command)

        if not suppress_output:
            print("\nBlocks Old Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)

        return output

    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
