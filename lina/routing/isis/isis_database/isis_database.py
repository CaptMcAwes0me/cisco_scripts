from core.utils import get_and_parse_cli_output


def isis_database(suppress_output=False, help_requested=False):
    """Retrieves and optionally displays the ISIS database using the 'show isis database' command.
       If help_requested=True, it prints the help information instead.
    """

    isis_database_help = {
        'command': 'show isis database',
        'description': (
            "Displays the Intermediate System to Intermediate System (ISIS) link-state database, "
            "including LSPs (Link-State Packets) for Level-1 and Level-2 routing. This command helps "
            "verify ISIS topology consistency and troubleshoot missing or incorrect LSPs."
        ),
        'example_output': """
ISIS Database for Level-2

LSP ID                 Seq Num  Checksum  Holdtime
1921.6800.1001.00-00   0x000004  0xA1B2    1200
1921.6800.1002.00-00   0x000005  0xB3C4    1100
        """
    }

    # If help is requested, print help content and exit the function
    if help_requested:
        print("\n" + "-" * 80)
        print(f"Help for: {isis_database_help['command']}".center(80))
        print("-" * 80)
        print(f"\n{isis_database_help['description']}\n")
        print("Example Output:")
        print(isis_database_help['example_output'])
        return None  # No actual command execution

    # Execute the ISIS Database command
    command = "show isis database"
    try:
        output = get_and_parse_cli_output(command)
        if not suppress_output:
            print("\nISIS Database Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)
        return output
    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
