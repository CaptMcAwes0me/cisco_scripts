from core.utils import get_and_parse_cli_output


def blocks_queue_history_detail(suppress_output=False, help_requested=False):
    """Retrieves and optionally displays the Blocks Queue History Detail using 'show blocks queue history detail'."""

    blocks_queue_history_detail_help_info = {
        'command': 'show blocks queue history detail',
        'description': (
            "Displays a detailed history of memory block allocations and deallocations across queue types. "
            "This command helps diagnose memory allocation patterns, track block exhaustion events, and "
            "analyze resource consumption per queue type."
        ),
        'example_output': """
History buffer memory usage: 3744 bytes (default)
History analysis time limit: 100 msec
Each Summary for User and Queue_type is followed by its top 5 individual queues
Blocks shown below are used blocks

Analysis elapsed time: 726 usec
Snapshot created at 00:22:26 UTC Feb 1 2025
Block Size: 256
  Blk_cnt Last_Op Queue_Type             Id/Interface User         Context
       85 alloc   <alloc_pc 0x000000aaad051b0c> <na>         <na>         
0x00000055001c8be8: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  |  ................
0x00000055001c8bf8: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  |  ................
0x00000055001c8c08: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  |  ................
0x00000055001c8c18: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  |  ................
0x00000055001c8c28: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  |  ................
        """
    }

    # Handle help request
    if help_requested:
        print("\n" + "=" * 80)
        print(f"Help for: {blocks_queue_history_detail_help_info['command']}".center(80))
        print("=" * 80)
        print(f"\n{blocks_queue_history_detail_help_info['description']}\n")
        print("Example Output:")
        print(blocks_queue_history_detail_help_info['example_output'])
        return None  # Do not execute the command

    command = "show blocks queue history detail"

    try:
        output = get_and_parse_cli_output(command)

        if not suppress_output:
            print("\nBlocks Queue History Detail Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)

        return output

    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
