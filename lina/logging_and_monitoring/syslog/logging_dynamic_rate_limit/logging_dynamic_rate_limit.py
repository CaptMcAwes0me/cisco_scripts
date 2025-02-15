from core.utils import get_and_parse_cli_output


def logging_dynamic_rate_limit(suppress_output=False, help_requested=False):
    """Retrieves and optionally displays the Logging Dynamic-rate-limit using 'show logging dynamic-rate-limit'.
       If help_requested=True, it prints the help information instead.
    """

    logging_dynamic_rate_limit_help = {
        'command': 'show logging dynamic-rate-limit',
        'description': (
            "This command displays the current rate-limiting settings for syslog messages to prevent excessive logging.\n\n"
            "**Usage Notes & Troubleshooting:**\n"
            "- Use this command to verify if syslog messages are being rate-limited.\n"
            "- If critical logs are missing, check if dynamic rate-limiting is restricting message flow.\n"
            "- Use `logging rate-limit <number>` to adjust the maximum number of messages per second.\n"
            "- If logs are still being dropped, review system load and CPU utilization using `show process cpu-usage`."
        ),
        'example_output': """
FTDv# show logging dynamic-rate-limit
Dynamic Rate Limiting: enabled
Message rate limit: 100 messages per second
Current dropped messages: 2450
        """
    }

    # If help is requested, print help content and exit the function
    if help_requested:
        print("\n" + "=" * 80)
        print(f"📖 Help for: {logging_dynamic_rate_limit_help['command']}".center(80))
        print("=" * 80)
        print(f"\n{logging_dynamic_rate_limit_help['description']}\n")
        print("Example Output:")
        print(logging_dynamic_rate_limit_help['example_output'])
        return None  # No actual command execution

    command = "show logging dynamic-rate-limit"

    try:
        output = get_and_parse_cli_output(command)

        if not suppress_output:
            print("\nLogging Dynamic-rate-limit Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)

        return output

    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
