from core.utils import get_and_parse_cli_output


def snmp_engineid(suppress_output=False, help_requested=False):
    """Retrieves and optionally displays the SNMP Engine ID using 'show snmp-server engineID'.
       If help_requested=True, it prints the help information instead.
    """

    snmp_engineid_help = {
        'command': 'show snmp-server engineID',
        'description': (
            "This command displays the **SNMP Engine ID**, a unique identifier for SNMPv3 communication.\n\n"
            "**Usage Notes & Troubleshooting:**\n"
            "- The Engine ID is **automatically generated** but can be **manually set** if needed.\n"
            "- If SNMPv3 authentication fails, ensure that the **Engine ID matches** on both ends.\n"
            "- Use `show snmp user` to verify SNMPv3 users.\n"
            "- If SNMP traps are not received, confirm the **Engine ID consistency** across SNMP managers."
        ),
        'example_output': """
FTDv# show snmp-server engineID

Local EngineID: 80000009030000249D8A8C00
        """
    }

    # If help is requested, print help content and exit the function
    if help_requested:
        print("\n" + "=" * 80)
        print(f"📖 Help for: {snmp_engineid_help['command']}".center(80))
        print("=" * 80)
        print(f"\n{snmp_engineid_help['description']}\n")
        print("Example Output:")
        print(snmp_engineid_help['example_output'])
        return None  # No actual command execution

    command = "show snmp-server engineID"

    try:
        output = get_and_parse_cli_output(command)

        if not suppress_output:
            print("\nSNMP EngineID Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)

        return output

    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
