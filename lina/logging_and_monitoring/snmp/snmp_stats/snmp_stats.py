from core.utils import get_and_parse_cli_output


def snmp_stats(suppress_output=False, help_requested=False):
    """Retrieves and optionally displays the SNMP Statistics using 'show snmp-server statistics'.
       If help_requested=True, it prints the help information instead.
    """

    snmp_stats_help = {
        'command': 'show snmp-server statistics',
        'description': (
            "This command displays SNMP statistics, including **packet counts, errors, and response times**.\n\n"
            "**Usage Notes & Troubleshooting:**\n"
            "- If **SNMP requests fail**, check:\n"
            "  1️⃣ `show snmp-server community` - Ensure the correct SNMP community string.\n"
            "  2️⃣ `show snmp-server host` - Verify SNMP host settings.\n"
            "  3️⃣ `show snmp-server statistics` - Look for **high error counts or dropped packets**.\n"
            "- If **SNMP traps are missing**, verify:\n"
            "  ✔ `show logging` - Ensure logging is enabled for SNMP.\n"
            "  ✔ `capture <name> interface <int> match ip host <SNMP_manager>` - Ensure packets are sent."
        ),
        'example_output': """
FTDv# show snmp-server statistics

SNMP packets input      : 250
SNMP packets output     : 245
SNMP packets dropped    : 5
SNMP Get-requests       : 100
SNMP Get-next requests  : 50
SNMP Set-requests       : 20
SNMP Response sent      : 245
SNMP Bad community name : 2
SNMP Bad community use  : 1
        """
    }

    # If help is requested, print help content and exit the function
    if help_requested:
        print("\n" + "=" * 80)
        print(f"📖 Help for: {snmp_stats_help['command']}".center(80))
        print("=" * 80)
        print(f"\n{snmp_stats_help['description']}\n")
        print("Example Output:")
        print(snmp_stats_help['example_output'])
        return None  # No actual command execution

    command = "show snmp-server statistics"

    try:
        output = get_and_parse_cli_output(command)

        if not suppress_output:
            print("\nSNMP Statistics Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)

        return output

    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
