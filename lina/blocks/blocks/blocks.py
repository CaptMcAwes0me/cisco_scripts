from core.utils import get_and_parse_cli_output

def blocks(suppress_output=False, help_requested=False):
    """Retrieves and optionally displays memory block allocation statistics using 'show blocks'."""

    blocks_help_info = {
        'command': 'show blocks',
        'description': (
            "Displays memory block allocation details, including block sizes, free and used counts, "
            "and memory fragmentation. This command is useful for diagnosing memory exhaustion issues "
            "that can impact system performance."
        ),
        'example_output': """
firepower# show blocks
   SIZE    MAX    LOW    CNT
      4   4200   4195   4200
    256   4200   4120   4190
    1550   600   550    598
    8192   100    50     90
"""
    }

    # Handle help request
    if help_requested:
        print("\n" + "=" * 80)
        print(f"Help for: {blocks_help_info['command']}".center(80))
        print("=" * 80)
        print(f"\n{blocks_help_info['description']}\n")
        print("Example Output:")
        print(blocks_help_info['example_output'])
        return None  # Do not execute the command

    command = "show blocks"

    try:
        output = get_and_parse_cli_output(command)

        if not suppress_output:
            print("\nBlocks Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)

        return output

    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
