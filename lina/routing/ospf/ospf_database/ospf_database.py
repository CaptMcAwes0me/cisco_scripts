from core.utils import get_and_parse_cli_output


def ospf_database(suppress_output=False, help_requested=False):
    """Retrieves and optionally displays OSPF database using the 'show ospf database' command.
       If help_requested=True, it prints the help information instead.
    """

    ospf_database_help = {
        'command': 'show ospf database',
        'description': (
            "Displays the contents of the OSPF link-state database, including Router LSAs, Network LSAs, "
            "Summary LSAs, and External LSAs. This command helps in troubleshooting OSPF topology issues "
            "and verifying route advertisements."
        ),
        'example_output': """
OSPF Database for Process ID 1, VRF default

Router Link States (Area 0)
Link ID       ADV Router     Age   Seq#       Checksum
192.168.1.1   192.168.1.1    123   0x8000001a  0x00A3
192.168.1.2   192.168.1.2    300   0x8000002c  0xB4D1

Summary Net Link States (Area 0)
Link ID       ADV Router     Age   Seq#       Checksum
10.10.10.0    192.168.1.1    156   0x8000004d  0x1B23
        """
    }

    # If help is requested, print help content and exit the function
    if help_requested:
        print("\n" + "-" * 80)
        print(f"Help for: {ospf_database_help['command']}".center(80))
        print("-" * 80)
        print(f"\n{ospf_database_help['description']}\n")
        print("Example Output:")
        print(ospf_database_help['example_output'])
        return None  # No actual command execution

    # Execute the OSPF Database command
    command = "show ospf database"
    try:
        output = get_and_parse_cli_output(command)
        if not suppress_output:
            print("\nOSPF Database Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)
        return output
    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
