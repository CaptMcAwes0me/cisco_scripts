from core.utils import get_and_parse_cli_output


def isis_lsp_log(suppress_output=False, help_requested=False):
    """Retrieves and optionally displays the ISIS LSP (Link-State Packet) log using the 'show isis lsp-log' command.
       If help_requested=True, it prints the help information instead.
    """

    isis_lsp_log_help = {
        'command': 'show isis lsp-log',
        'description': (
            "Displays a log of ISIS LSP (Link-State Packet) updates, including LSP origin, sequence number changes, "
            "and aging. This command helps in diagnosing LSP flooding issues and ensuring ISIS database synchronization."
        ),
        'example_output': """
ISIS LSP Log:

Timestamp       LSP ID                  Seq Num   Event
12:30:01.123    1921.6800.1001.00-00     0x000006  Generated new LSP
12:31:15.456    1921.6800.1002.00-00     0x000007  Received new LSP
12:35:20.789    1921.6800.1001.00-00     0x000008  Refreshed LSP
        """
    }

    # If help is requested, print help content and exit the function
    if help_requested:
        print("\n" + "-" * 80)
        print(f"Help for: {isis_lsp_log_help['command']}".center(80))
        print("-" * 80)
        print(f"\n{isis_lsp_log_help['description']}\n")
        print("Example Output:")
        print(isis_lsp_log_help['example_output'])
        return None  # No actual command execution

    # Execute the ISIS LSP Log command
    command = "show isis lsp-log"
    try:
        output = get_and_parse_cli_output(command)
        if not suppress_output:
            print("\nISIS LSP Log Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)
        return output
    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
