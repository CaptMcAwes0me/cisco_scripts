from core.utils import get_and_parse_cli_output


def logging_buffered_output(suppress_output=False, help_requested=False):
    """Retrieves and optionally displays the Logging Buffered Output using 'show log'.
       If help_requested=True, it prints the help information instead.
    """

    logging_buffered_output_help = {
        'command': 'show log',
        'description': (
            "This command displays log messages stored in the **buffered logging memory** on the device.\n\n"
            "**Usage Notes & Troubleshooting:**\n"
            "- Logs stored in the buffer are **not persistent** (cleared after a reboot).\n"
            "- If no logs appear, verify that **buffered logging** is enabled (`show running-config logging`).\n"
            "- Use `logging buffered <level>` to configure logging for specific severity levels.\n"
            "- Check `logging buffer-size <size>` to adjust the memory allocated for buffering logs.\n"
            "- If you need to clear the logs, use `clear logging buffer`."
        ),
        'example_output': """
FTDv# show log

Feb 14 15:05:18 2025: %ASA-4-106023: Deny udp src outside:14.38.117.1/443 dst inside:192.168.1.10/53124
Feb 14 15:05:19 2025: %ASA-6-302015: Built outbound TCP connection 12345678 for outside:14.38.117.10/443 to inside:192.168.1.20/53125
Feb 14 15:05:20 2025: %ASA-3-402117: IPSEC: Received an ESP packet (SPI=0x1234ABCD) from 14.38.117.30 to 192.168.2.1, but no associated SA was found
Feb 14 15:05:21 2025: %ASA-7-609001: Built inbound ICMP connection for fover:1.1.1.2
        """
    }

    # If help is requested, print help content and exit the function
    if help_requested:
        print("\n" + "=" * 80)
        print(f"📖 Help for: {logging_buffered_output_help['command']}".center(80))
        print("=" * 80)
        print(f"\n{logging_buffered_output_help['description']}\n")
        print("Example Output:")
        print(logging_buffered_output_help['example_output'])
        return None  # No actual command execution

    command = "show log"

    try:
        output = get_and_parse_cli_output(command)

        if not suppress_output:
            print("\nLogging Buffered Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)

        return output

    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
