from core.utils import get_and_parse_cli_output


def snmp_config(suppress_output=False, help_requested=False):
    """Retrieves and optionally displays the SNMP Running Configuration using 'show run all snmp-server'.
       If help_requested=True, it prints the help information instead.
    """

    snmp_config_help = {
        'command': 'show run all snmp-server',
        'description': (
            "This command displays the current **SNMP configuration** on the ASA.\n\n"
            "**Usage Notes & Troubleshooting:**\n"
            "- SNMP is used for **remote monitoring and management** of ASA devices.\n"
            "- If SNMP is not working, ensure **SNMP communities, users, and traps are configured**.\n"
            "- Use `show snmp engineID` to verify the SNMP Engine ID.\n"
            "- Use `show snmp stats` to check for SNMP message processing errors.\n"
            "- Ensure the **firewall allows SNMP traffic** (UDP 161 for queries, UDP 162 for traps)."
        ),
        'example_output': """
FTDv# show run all snmp-server

snmp-server enable
snmp-server host inside 192.168.1.100 community MyCommunity
snmp-server user SNMPUser v3 auth sha MyAuthPass priv aes 128 MyPrivPass
snmp-server group SNMPv3Group v3 priv read ViewAll
snmp-server location DataCenter-Rack4
snmp-server contact admin@example.com
snmp-server enable traps snmp authentication linkup linkdown
        """
    }

    # If help is requested, print help content and exit the function
    if help_requested:
        print("\n" + "=" * 80)
        print(f"📖 Help for: {snmp_config_help['command']}".center(80))
        print("=" * 80)
        print(f"\n{snmp_config_help['description']}\n")
        print("Example Output:")
        print(snmp_config_help['example_output'])
        return None  # No actual command execution

    command = "show run all snmp-server"

    try:
        output = get_and_parse_cli_output(command)

        if not suppress_output:
            print("\nSNMP Running Configuration Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)

        return output

    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
