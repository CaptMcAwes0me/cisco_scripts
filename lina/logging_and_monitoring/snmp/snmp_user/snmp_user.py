from core.utils import get_and_parse_cli_output


def snmp_user(suppress_output=False, help_requested=False):
    """Retrieves and optionally displays the SNMP User using 'show snmp-server user'.
       If help_requested=True, it prints the help information instead.
    """

    snmp_user_help = {
        'command': 'show snmp-server user',
        'description': (
            "This command displays SNMPv3 users and their authentication/privacy settings.\n\n"
            "**Usage Notes & Troubleshooting:**\n"
            "- If **SNMPv3 authentication fails**, check:\n"
            "  1️⃣ `show snmp-server user` - Ensure the user exists.\n"
            "  2️⃣ `show run all snmp-server` - Verify authentication settings.\n"
            "  3️⃣ `show snmp-server statistics` - Look for failed authentication attempts.\n"
            "- If **SNMPv3 encryption is not working**, verify:\n"
            "  ✔ `show snmp-server user` - Ensure **AES/DES encryption** is configured.\n"
            "  ✔ `show snmp-server group` - Confirm privacy settings for the group."
        ),
        'example_output': """
FTDv# show snmp-server user

User              Auth   Priv   Acc Group   EngineID
----------------------------------------------------
admin_user        MD5    AES128 ReadOnly    8000000903000027E5D59A
monitor_user      SHA     AES    ReadWrite   8000000903000027E5D59B
        """
    }

    # If help is requested, print help content and exit the function
    if help_requested:
        print("\n" + "=" * 80)
        print(f"📖 Help for: {snmp_user_help['command']}".center(80))
        print("=" * 80)
        print(f"\n{snmp_user_help['description']}\n")
        print("Example Output:")
        print(snmp_user_help['example_output'])
        return None  # No actual command execution

    command = "show snmp-server user"

    try:
        output = get_and_parse_cli_output(command)

        if not suppress_output:
            print("\nSNMP User Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)

        return output

    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
