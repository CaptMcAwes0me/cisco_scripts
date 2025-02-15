from core.utils import get_and_parse_cli_output


def logging_queue(suppress_output=False, help_requested=False):
    """Retrieves and optionally displays the Logging Queue using 'show logging queue'.
       If help_requested=True, it prints the help information instead.
    """

    logging_queue_help = {
        'command': 'show logging queue',
        'description': (
            "This command displays the current logging queue details, showing how many messages are waiting to be "
            "processed, the maximum queue size, and any potential message drops.\n\n"
            "**Usage Notes & Troubleshooting:**\n"
            "- If log messages are not appearing in real-time, check if the queue is full.\n"
            "- A high 'dropped' count indicates the system is unable to process logs quickly enough.\n"
            "- If messages are backing up, consider adjusting the logging buffer size (`logging buffer-size`).\n"
            "- Verify that `logging queue` has an appropriate size set for the environment.\n"
            "- If logs are being sent to an external syslog server (`logging host`), ensure there are no network issues."
        ),
        'example_output': """
FTDv# show logging queue
Queue Limit: 512
Total Messages Queued: 0
Total Messages Dropped: 0
        """
    }

    # If help is requested, print help content and exit the function
    if help_requested:
        print("\n" + "=" * 80)
        print(f"📖 Help for: {logging_queue_help['command']}".center(80))
        print("=" * 80)
        print(f"\n{logging_queue_help['description']}\n")
        print("Example Output:")
        print(logging_queue_help['example_output'])
        return None  # No actual command execution

    command = "show logging queue"

    try:
        output = get_and_parse_cli_output(command)

        if not suppress_output:
            print("\nLogging Queue Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)

        return output

    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
