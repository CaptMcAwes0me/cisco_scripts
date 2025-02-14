# Description: This script retrieves and optionally displays the connection table using 'show conn detail' or a filtered version.

from core.utils import get_and_parse_cli_output


def conn_detail(suppress_output=False, help_requested=False):
    """
    Retrieves and optionally displays the connection table using 'show conn detail' or a filtered version.
    If help_requested=True, it prints the help information instead.
    """


    conn_help_info = {
        'command': 'show conn detail',
        'description': (
            "The 'show conn detail' command displays detailed information about all active connections through the ASA. "
            "This includes protocol types, source and destination IP addresses and ports, idle times, data transfer statistics, "
            "and connection flags that indicate the state and characteristics of each connection."
        ),
        'example_output': """
TCP outside 192.168.3.5:80 dmz 172.16.103.221:57646, idle 0:00:29, bytes 2176, flags UIO
TCP outside 10.23.232.217:443 inside 192.168.1.3:52427, idle 0:01:02, bytes 4504, flags UIO
        """,
        'notes': (
            "Each line represents an active connection with the following details:\n"
            "  - **Protocol**: The protocol in use (e.g., TCP, UDP).\n"
            "  - **Source Interface and IP:Port**: The originating interface and IP address with the port number.\n"
            "  - **Destination Interface and IP:Port**: The destination interface and IP address with the port number.\n"
            "  - **Idle Time**: Duration since the last packet was exchanged.\n"
            "  - **Bytes**: Total number of bytes transferred over the connection.\n"
            "  - **Flags**: Indicators of the connection's state and attributes."
        ),
        'related_commands': [
            {'command': 'show conn', 'description': 'Displays a summary of active connections.'},
            {'command': 'show conn count', 'description': 'Shows the number of active connections.'},
            {'command': 'clear conn', 'description': 'Terminates active connections.'},
            {'command': 'show local-host', 'description': 'Displays information about local hosts.'},
            {'command': 'show xlate', 'description': 'Shows the NAT translation table.'},
        ]
    }

    if help_requested:
        print("\n" + "-" * 80)
        print(f"📖 Help for: {conn_help_info['command']}".center(80))
        print("-" * 80)
        print(f"\nDescription:\n{conn_help_info['description']}\n")
        print("Example Output:")
        print(conn_help_info['example_output'])
        print("\nNotes:")
        print(conn_help_info['notes'])
        print("\nRelated Commands:")
        for related in conn_help_info['related_commands']:
            print(f"  - {related['command']}: {related['description']}")
        return None

    # Prompt user for an IP address to filter
    ip_filter = input("Enter an IP address to filter by (or press enter to show all): ").strip()

    # Modify the command based on user input
    command = f"show conn address {ip_filter}" if ip_filter else "show conn detail"

    try:
        output = get_and_parse_cli_output(command)

        if not suppress_output:
            print("\nConnection Detail Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)

        return output

    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message


def conn_detail_dump(suppress_output=False, help_requested=False):
    """Retrieves and optionally displays the conn using 'show conn detail'."""

    conn_help_info = {
        'command': 'show conn detail',
        'description': (
            "The 'show conn detail' command displays detailed information about all active connections through the ASA. "
            "This includes protocol types, source and destination IP addresses and ports, idle times, data transfer statistics, "
            "and connection flags that indicate the state and characteristics of each connection."
        ),
        'example_output': """
TCP outside 192.168.3.5:80 dmz 172.16.103.221:57646, idle 0:00:29, bytes 2176, flags UIO
TCP outside 10.23.232.217:443 inside 192.168.1.3:52427, idle 0:01:02, bytes 4504, flags UIO
        """,
        'notes': (
            "Each line represents an active connection with the following details:\n"
            "  - **Protocol**: The protocol in use (e.g., TCP, UDP).\n"
            "  - **Source Interface and IP:Port**: The originating interface and IP address with the port number.\n"
            "  - **Destination Interface and IP:Port**: The destination interface and IP address with the port number.\n"
            "  - **Idle Time**: Duration since the last packet was exchanged.\n"
            "  - **Bytes**: Total number of bytes transferred over the connection.\n"
            "  - **Flags**: Indicators of the connection's state and attributes."
        ),
        'related_commands': [
            {'command': 'show conn', 'description': 'Displays a summary of active connections.'},
            {'command': 'show conn count', 'description': 'Shows the number of active connections.'},
            {'command': 'clear conn', 'description': 'Terminates active connections.'},
            {'command': 'show local-host', 'description': 'Displays information about local hosts.'},
            {'command': 'show xlate', 'description': 'Shows the NAT translation table.'},
        ]
    }

    if help_requested:
        print("\n" + "-" * 80)
        print(f"📖 Help for: {conn_help_info['command']}".center(80))
        print("-" * 80)
        print(f"\nDescription:\n{conn_help_info['description']}\n")
        print("Example Output:")
        print(conn_help_info['example_output'])
        print("\nNotes:")
        print(conn_help_info['notes'])
        print("\nRelated Commands:")
        for related in conn_help_info['related_commands']:
            print(f"  - {related['command']}: {related['description']}")
        return None

    command = "show conn detail"

    try:
        output = get_and_parse_cli_output(command)

        if not suppress_output:
            print("\nConn Detail Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)

        return output

    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
