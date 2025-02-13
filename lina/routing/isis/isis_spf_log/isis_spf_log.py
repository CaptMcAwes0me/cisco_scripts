from core.utils import get_and_parse_cli_output


def isis_spf_log(suppress_output=False, help_requested=False):
    """Retrieves and optionally displays the ISIS SPF log using the 'show isis spf-log' command.
       If help_requested=True, it prints the help information instead.
    """

    isis_spf_log_help = {
        'command': 'show isis spf-log',
        'description': (
            "Displays the ISIS Shortest Path First (SPF) log, showing SPF recalculations and changes in the network topology. "
            "This command is useful for identifying frequent topology changes, which may indicate instability or network flaps."
        ),
        'example_output': """
ISIS SPF Log:

Timestamp       Event Type       Node ID        Details
12:30:01.123    SPF Calculation  1921.6800.1001 Route Change Detected
12:35:15.456    SPF Calculation  1921.6800.1002 New LSP Processed
12:40:20.789    SPF Calculation  1921.6800.1001 Converged
        """
    }

    # If help is requested, print help content and exit the function
    if help_requested:
        print("\n" + "-" * 80)
        print(f"Help for: {isis_spf_log_help['command']}".center(80))
        print("-" * 80)
        print(f"\n{isis_spf_log_help['description']}\n")
        print("Example Output:")
        print(isis_spf_log_help['example_output'])
        return None  # No actual command execution

    # Execute the ISIS SPF Log command
    command = "show isis spf-log"
    try:
        output = get_and_parse_cli_output(command)
        if not suppress_output:
            print("\nISIS SPF Log Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)
        return output
    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
