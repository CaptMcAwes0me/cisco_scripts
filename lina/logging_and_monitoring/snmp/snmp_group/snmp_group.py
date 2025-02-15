from core.utils import get_and_parse_cli_output


def snmp_group(suppress_output=False, help_requested=False):
    """Retrieves and optionally displays the SNMP Group using 'show snmp-server group'.
       If help_requested=True, it prints the help information instead.
    """

    snmp_group_help = {
        'command': 'show snmp-server group',
        'description': (
            "This command displays **SNMP groups** configured on the FTD.\n\n"
            "**Usage Notes & Troubleshooting:**\n"
            "- SNMP groups define **access control and security models** (v1, v2c, v3).\n"
            "- If SNMP access fails, check that the **correct group and security level** are assigned.\n"
            "- Use `show snmp-server user` to verify which users belong to which SNMP groups.\n"
            "- If SNMPv3 is used, confirm that the **authentication and encryption settings match**.\n"
            "- To modify an SNMP group, use:\n"
            "  `snmp-server group <group_name> v3 priv` (for SNMPv3 with encryption)."
        ),
        'example_output': """
FTDv# show snmp-server group

Group name: AdminGroup   Security model: v3   Auth: MD5   Priv: AES128
Group name: ReadOnly     Security model: v2c  Read View: all
        """
    }

    # If help is requested, print help content and exit the function
    if help_requested:
        print("\n" + "=" * 80)
        print(f"📖 Help for: {snmp_group_help['command']}".center(80))
        print("=" * 80)
        print(f"\n{snmp_group_help['description']}\n")
        print("Example Output:")
        print(snmp_group_help['example_output'])
        return None  # No actual command execution

    command = "show snmp-server group"

    try:
        output = get_and_parse_cli_output(command)

        if not suppress_output:
            print("\nSNMP Group Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)

        return output

    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
