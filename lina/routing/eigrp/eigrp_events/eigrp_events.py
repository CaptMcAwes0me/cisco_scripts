# Description: This script retrieves and displays EIGRP events using the 'show eigrp events' command.


from core.utils import get_and_parse_cli_output


def eigrp_events():
    """Retrieves and displays EIGRP events using the 'show eigrp events' command."""

    # Command to retrieve EIGRP events
    command = "show eigrp events"

    try:
        # Get and parse the CLI output from the command
        output = get_and_parse_cli_output(command)

        # Display the output
        print("\nEIGRP Events Output:")
        print("-" * 80)
        print(output)
        print("-" * 80)
        return(output)
    except Exception as e:
        print(f"[!] Error: {e}")
