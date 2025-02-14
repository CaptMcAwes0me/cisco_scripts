from core.utils import get_and_parse_cli_output


def snmp_host(suppress_output=False, help_requested=False):
    """Retrieves and optionally displays the SNMP Host using 'show snmp-server host'.
       If help_requested=True, it prints the help information instead.
    """

    snmp_host_help = {
        'command': 'show snmp-server host',
        'description': (
            "This command displays **configured SNMP hosts** that receive traps or queries.\n\n"
            "**Usage Notes & Troubleshooting:**\n"
            "- Ensure that the **SNMP host IP address and community string** match the SNMP manager's configuration.\n"
            "- If SNMP traps are not being received, verify:\n"
            "  1️⃣ `show logging` - Ensure logging is enabled.\n"
            "  2️⃣ `show snmp-server community` - Ensure correct SNMP community.\n"
            "  3️⃣ `capture <name> interface <int> match ip host <SNMP_host>` - Check if SNMP packets are sent.\n"
            "- To add an SNMP host:\n"
            "  `snmp-server host <interface> <ip_address> version <v1|v2c|v3> <community>`"
        ),
        'example_output': """
FTDv# show snmp-server host

Host      : 192.168.1.100
Interface : inside
Version   : v2c
Community : public
Traps     : Enabled
        """
    }

    # If help is requested, print help content and exit the function
    if help_requested:
        print("\n" + "=" * 80)
        print(f"📖 Help for: {snmp_host_help['command']}".center(80))
        print("=" * 80)
        print(f"\n{snmp_host_help['description']}\n")
        print("Example Output:")
        print(snmp_host_help['example_output'])
        return None  # No actual command execution

    command = "show snmp-server host"

    try:
        output = get_and_parse_cli_output(command)

        if not suppress_output:
            print("\nSNMP Host Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)

        return output

    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
