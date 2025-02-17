import re
from collections import Counter
from core.utils import get_and_parse_cli_output


def parse_conn_output(output):
    """
    Parses 'show conn' output into a structured list, handling variations in spacing.
    """
    conn_data = []
    conn_pattern = re.compile(
        r'(?P<proto>\S+)\s+(?P<src_intf>\S+)\s+(?P<src_ip>\S+?):(?P<src_port>\d+)\s+'
        r'(?P<dst_intf>\S+)\s+(?P<dst_ip>\S+?):(?P<dst_port>\d+),\s+'
        r'idle\s+(?P<idle_time>[\d:]+),\s+bytes\s+(?P<bytes>\d+),\s+flags\s+(?P<flags>.+)'
    )

    processing = False  # Flag to start processing when connections appear

    for line in output.split('\n'):
        line = line.strip()

        if not processing:
            if conn_pattern.match(line):
                processing = True  # Start processing actual connection entries
            else:
                continue  # Skip irrelevant lines before connections start

        match = conn_pattern.match(line)
        if match:
            conn_data.append({
                "Proto": match.group("proto"),
                "Src_Intf": match.group("src_intf"),
                "Src_IP": match.group("src_ip"),
                "Src_Port": match.group("src_port"),
                "Dst_Intf": match.group("dst_intf"),
                "Dst_IP": match.group("dst_ip"),
                "Dst_Port": match.group("dst_port"),
                "Idle_Time": match.group("idle_time"),
                "Bytes": int(match.group("bytes")),
                "Flags": match.group("flags").strip()
            })

    return conn_data


def conn_analyzer(help_requested=False):
    """
    Retrieves and optionally displays the connection table using 'show conn detail' or a filtered version.
    If help_requested=True, it prints the help information instead.
    """

    conn_help_info = {
        'command': 'show conn',
        'description': (
            "The 'show conn' command displays detailed information about all active connections through the FTD. "
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

    try:
        command = f"show conn"
        output = get_and_parse_cli_output(command)
        conn_data = parse_conn_output(output)

        print(f"Parsed {len(conn_data)} connections")
        if not conn_data:
            print("No connection data found.")
            return

        # Top-20 IPs with the most connections
        ip_counts = Counter(conn['Src_IP'] for conn in conn_data).most_common(20)
        print("\nTop-20 IPs with Most Connections:")
        print("IP Address".ljust(40) + "Count".rjust(10) + "  Percent")
        print("-" * 60)
        total_conns = len(conn_data)
        for ip, count in ip_counts:
            percent = (count / total_conns) * 100
            print(f"{ip.ljust(40)}{count:>10}  {percent:.3f}%")

        # Top-20 Connections by Bytes Transferred
        print("\nTop-20 Connections by Bytes Transferred:")
        print("Proto".ljust(6) + "Src Intf".ljust(15) + "Src IP".ljust(36) + "Src Port".ljust(10) + "Dst Intf".ljust(
            15) + "Dst IP".ljust(36) + "Dst Port".ljust(10) + "Idle Time".ljust(10) + "Bytes".rjust(12) + "    Flags")
        print("-" * 160)
        for conn in sorted(conn_data, key=lambda x: x['Bytes'], reverse=True)[:20]:
            print(
                f"{conn['Proto'].ljust(6)}{conn['Src_Intf'].ljust(15)}{conn['Src_IP'].ljust(36)}{conn['Src_Port'].ljust(10)}{conn['Dst_Intf'].ljust(15)}{conn['Dst_IP'].ljust(36)}{conn['Dst_Port'].ljust(10)}{conn['Idle_Time'].ljust(10)}{str(conn['Bytes']).rjust(12)}  {conn['Flags']}")

        # Top-20 Connections by Idle Time
        print("\nTop-20 Connections by Idle Time:")
        print("Proto".ljust(6) + "Src Intf".ljust(15) + "Src IP".ljust(36) + "Src Port".ljust(10) + "Dst Intf".ljust(
            15) + "Dst IP".ljust(36) + "Dst Port".ljust(10) + "Idle Time".ljust(10) + "Bytes".rjust(12) + "    Flags")
        print("-" * 160)
        for conn in sorted(conn_data, key=lambda x: x['Idle_Time'], reverse=True)[:20]:
            print(
                f"{conn['Proto'].ljust(6)}{conn['Src_Intf'].ljust(15)}{conn['Src_IP'].ljust(36)}{conn['Src_Port'].ljust(10)}{conn['Dst_Intf'].ljust(15)}{conn['Dst_IP'].ljust(36)}{conn['Dst_Port'].ljust(10)}{conn['Idle_Time'].ljust(10)}{str(conn['Bytes']).rjust(12)}  {conn['Flags']}")

        # Hairpinning (U-turn) connections
        print("\nTop-20 Hairpinning Connections:")
        print("Proto".ljust(6) + "Src Intf".ljust(15) + "Src IP".ljust(36) + "Src Port".ljust(10) + "Dst Intf".ljust(
            15) + "Dst IP".ljust(36) + "Dst Port".ljust(10) + "Idle Time".ljust(10) + "Bytes".rjust(12) + "    Flags")
        print("-" * 160)
        for conn in sorted([c for c in conn_data if c['Src_Intf'] == c['Dst_Intf']], key=lambda x: x['Bytes'],
                           reverse=True)[:20]:
            print(
                f"{conn['Proto'].ljust(6)}{conn['Src_Intf'].ljust(15)}{conn['Src_IP'].ljust(36)}{conn['Src_Port'].ljust(10)}{conn['Dst_Intf'].ljust(15)}{conn['Dst_IP'].ljust(36)}{conn['Dst_Port'].ljust(10)}{conn['Idle_Time'].ljust(10)}{str(conn['Bytes']).rjust(12)}  {conn['Flags']}")

        # Connection counts per interface pair
        interface_pairs = Counter(
            (conn['Src_Intf'], conn['Dst_Intf']) for conn in conn_data
        )
        print("\nConns per Interface Pair")
        print("Interface-pair".ljust(60) + "Count".rjust(10) + "  Percent")
        print("-" * 80)
        for (src_intf, dst_intf), count in interface_pairs.most_common():
            percent = (count / total_conns) * 100
            print(f"{src_intf} <-> {dst_intf}".ljust(60) + f"{count:>10}  {percent:.3f}%")

        # Connection percentage per protocol
        protocol_counts = Counter(conn['Proto'] for conn in conn_data)
        print("\nConnection Percentage per Protocol:")
        print("Protocol".ljust(20) + "Count".rjust(10) + "  Percent")
        print("-" * 50)
        for proto, count in protocol_counts.items():
            percent = (count / total_conns) * 100
            print(f"{proto}".ljust(20) + f"{count:>10}  {percent:.3f}%")

        # Extract Embryonic Connections (SYN but not SYN/ACK, 'aA' flags)
        embryonic_conns = [conn for conn in conn_data if 'a' in conn['Flags'] or 'A' in conn['Flags']]
        print(f"\nTotal Embryonic Connections: {len(embryonic_conns)}")

        # Top-10 TCP Embryonic Destination Port Statistics
        top_embryonic_dst = Counter(conn['Dst_Port'] for conn in embryonic_conns).most_common(10)
        print("\nTop-10 TCP Embryonic Destination Ports:")
        print("DST Port".ljust(10) + "Count".rjust(10))
        print("-" * 25)
        for port, count in top_embryonic_dst:
            print(f"{port.ljust(10)}{count:>10}")

        # Top-10 TCP Embryonic Source Port Statistics
        top_embryonic_src = Counter(conn['Src_Port'] for conn in embryonic_conns).most_common(10)
        print("\nTop-10 TCP Embryonic Source Ports:")
        print("Src Port".ljust(10) + "Count".rjust(10))
        print("-" * 25)
        for port, count in top_embryonic_src:
            print(f"{port.ljust(10)}{count:>10}")

    except Exception as e:
        print(f"Error occurred: {e}")


def conn_detail_dump(suppress_output=False, help_requested=False):
    """Retrieves and optionally displays the conn using 'show conn detail'."""

    conn_help_info = {
        'command': 'show conn detail',
        'description': (
            "The 'show conn detail' command displays detailed information about all active connections through the FTDgarrett-branch/lina/routing/global_routing/global_routing_help/global_routing_help.py. "
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
