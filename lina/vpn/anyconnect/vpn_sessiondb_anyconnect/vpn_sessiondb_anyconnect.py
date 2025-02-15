from core.utils import get_and_parse_cli_output


def vpn_sessiondb_anyconnect(tunnel_group, help_requested=False):
    """
    Retrieves and displays AnyConnect VPN session database information
    for the specified tunnel-group.
    If help_requested=True, prints the help information instead.
    """

    vpn_sessiondb_anyconnect_help = {
        'command': 'show vpn-sessiondb anyconnect filter tunnel-group <group>',
        'description': (
            "Displays active AnyConnect VPN session details for the specified tunnel group. "
            "Provides session status, authentication information, encryption details, and assigned IPs."
        ),
        'example_output': """
Session Type: AnyConnect
 Username     : user1
 Assigned IP  : 192.168.10.5
 Protocol     : SSL-TLSv1.2
 Tunnel Group : AC-TunnelGroup
 Login Time   : 00:05:23
        """
    }

    if help_requested:
        print("\n" + "-" * 80)
        print(f"Help for: {vpn_sessiondb_anyconnect_help['command']}".center(80))
        print("-" * 80)
        print(f"\n{vpn_sessiondb_anyconnect_help['description']}\n")
        print("Example Output:")
        print(vpn_sessiondb_anyconnect_help['example_output'])
        return None  # No actual execution

    try:
        print("=" * 80)
        print(f"VPN-Sessiondb Information for {tunnel_group}".center(80))
        print("=" * 80)
        command = f"show vpn-sessiondb anyconnect filter tunnel-group {tunnel_group}"
        output = get_and_parse_cli_output(command)
        print(output)
        print("=" * 80 + "\n")
        return output

    except Exception as e:
        error_message = f"[!] Error: {e}"
        print(error_message)
        return error_message


def vpn_sessiondb_anyconnect_dump(suppress_output=False, help_requested=False):
    """
    Retrieves and optionally displays the full AnyConnect VPN session database.
    If help_requested=True, prints the help information instead.
    """

    vpn_sessiondb_anyconnect_dump_help = {
        'command': 'show vpn-sessiondb anyconnect',
        'description': (
            "Displays a full list of active AnyConnect VPN sessions, including user details, assigned IPs, "
            "tunnel group associations, encryption protocols, and login times."
        ),
        'example_output': """
Session Type: AnyConnect
 Username     : user2
 Assigned IP  : 192.168.10.12
 Protocol     : SSL-TLSv1.3
 Tunnel Group : RemoteUsers
 Login Time   : 02:15:44
        """
    }

    if help_requested:
        print("\n" + "-" * 80)
        print(f"Help for: {vpn_sessiondb_anyconnect_dump_help['command']}".center(80))
        print("-" * 80)
        print(f"\n{vpn_sessiondb_anyconnect_dump_help['description']}\n")
        print("Example Output:")
        print(vpn_sessiondb_anyconnect_dump_help['example_output'])
        return None  # No actual execution

    command = "show vpn-sessiondb anyconnect"

    try:
        output = get_and_parse_cli_output(command)

        if not suppress_output:
            print(f"\n{command} Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)

        return output

    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
