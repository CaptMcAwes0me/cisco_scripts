# Description: This script retrieves and optionally displays the performance monitoring (Perfmon) statistics using 'show perfmon'.

from core.utils import get_and_parse_cli_output


def perfmon(suppress_output=False, help_requested=False):
    """
    Retrieves and optionally displays the Perfmon statistics using 'show perfmon'.
    If help_requested=True, it prints the help information instead.
    """

    perfmon_help_info = {
        'command': 'show perfmon',
        'description': (
            "The 'show perfmon' command provides real-time statistics for connections, translations (xlates), "
            "authentication events, and protocol-specific operations. It helps in assessing the system's "
            "current and average transaction processing rate."
        ),
        'example_output': """
firepower# show perfmon

PERFMON STATS:                     Current      Average
Xlates                                0/s          0/s
Connections                           0/s          0/s
TCP Conns                             0/s          0/s
UDP Conns                             0/s          0/s
URL Access                            0/s          0/s
URL Server Req                        0/s          0/s
TCP Fixup                             0/s          0/s
TCP Intercept Established Conns       0/s          0/s
TCP Intercept Attempts                0/s          0/s
TCP Embryonic Conns Timeout           0/s          0/s
FTP Fixup                             0/s          0/s
AAA Authen                            0/s          0/s
AAA Author                            0/s          0/s
AAA Account                           0/s          0/s
HTTP Fixup                            0/s          0/s

VALID CONNS RATE in TCP INTERCEPT:    Current      Average
                                       N/A         N/A
        """,
        'notes': (
            "Key fields in the output include:\n"
            "  - **Xlates**: Rate of NAT translations per second.\n"
            "  - **Connections**: Total new connections per second.\n"
            "  - **TCP Conns / UDP Conns**: Breakdown of protocol-based connections.\n"
            "  - **AAA Authen/Author/Account**: Tracks authentication, authorization, and accounting operations.\n"
            "  - **TCP Intercept**: Tracks TCP connection interception for security enforcement.\n"
            "  - **HTTP, FTP, URL Fixup**: Indicates protocol-specific traffic handling.\n"
            "  - **Current vs. Average Rates**: Provides real-time and historical performance comparison."
        ),
        'related_commands': [
            {'command': 'show conn count', 'description': 'Displays the number of active connections.'},
            {'command': 'show xlate count', 'description': 'Shows the number of active NAT translations.'},
            {'command': 'show traffic', 'description': 'Provides real-time network traffic statistics.'},
            {'command': 'show cpu usage', 'description': 'Displays detailed CPU utilization statistics.'},
        ]
    }

    if help_requested:
        print("\n" + "-" * 80)
        print(f"📖 Help for: {perfmon_help_info['command']}".center(80))
        print("-" * 80)
        print(f"\nDescription:\n{perfmon_help_info['description']}\n")
        print("Example Output:")
        print(perfmon_help_info['example_output'])
        print("\nNotes:")
        print(perfmon_help_info['notes'])
        print("\nRelated Commands:")
        for related in perfmon_help_info['related_commands']:
            print(f"  - {related['command']}: {related['description']}")
        return None

    command = "show perfmon"

    try:
        output = get_and_parse_cli_output(command)

        if not suppress_output:
            print("\nPerfmon Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)

        return output

    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
