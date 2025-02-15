from core.utils import get_and_parse_cli_output

def blocks_old_dump(suppress_output=False, help_requested=False):
    """Retrieves and optionally displays the Blocks Old Dump using 'show blocks old dump'."""

    blocks_old_dump_help_info = {
        'command': 'show blocks old dump',
        'description': (
            "Displays a detailed dump of the oldest allocated memory blocks in the system. "
            "Useful for diagnosing memory fragmentation, analyzing memory block retention, "
            "and tracking allocation lifetimes to detect potential leaks."
        )
    }

    # Handle help request
    if help_requested:
        print("\n" + "=" * 80)
        print(f"Help for: {blocks_old_dump_help_info['command']}".center(80))
        print("=" * 80)
        print(f"\n{blocks_old_dump_help_info['description']}\n")
        return None  # Do not execute the command

    command = "show blocks old dump"

    try:
        output = get_and_parse_cli_output(command)

        if not suppress_output:
            print("\nBlocks Old Dump Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)

        return output

    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
