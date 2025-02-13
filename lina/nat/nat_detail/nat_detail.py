from core.utils import get_and_parse_cli_output

def nat_detail(suppress_output=False, help_requested=False):
    """Retrieves and optionally displays the NAT Detail Table using 'show nat detail'.
       If help_requested=True, it prints the help information instead.
    """

    nat_detail_help = {
        'command': 'show nat detail',
        'description': (
            "Displays the NAT policy table with detailed information, including hit counts for each rule. "
            "The 'translate_hits' counter indicates the number of new connections matching the NAT rule in the forward direction, "
            "while the 'untranslate_hits' counter shows matches in the reverse direction. "
            "This command is useful for understanding which NAT entries are actively used and for troubleshooting NAT configurations."
        ),
        'example_output': """
Manual NAT Policies (Section 1)
1 (any) to (any) source dynamic S S' destination static D' D
    translate_hits = 0, untranslate_hits = 0
    Source - Real: 1.1.1.2/32, Mapped: 2.2.2.3/32
    Destination - Real: 10.10.10.0/24, Mapped: 20.20.20.0/24

Auto NAT Policies (Section 2)
1 (inside) to (outside) source dynamic A 2.2.2.2
    translate_hits = 0, untranslate_hits = 0
    Source - Real: 1.1.1.1/32, Mapped: 2.2.2.2/32

Manual NAT Policies (Section 3)
1 (any) to (any) source dynamic C C' destination static B' B service R R'
    translate_hits = 0, untranslate_hits = 0
    Source - Real: 11.11.11.10-11.11.11.11, Mapped: 192.168.10.10/32
    Destination - Real: 192.168.1.0/24, Mapped: 10.75.1.0/24
    Service - Real: tcp source eq 10 destination eq ftp-data, Mapped: tcp source eq 100 destination eq 200
        """
    }

    # If help is requested, print help content and exit the function
    if help_requested:
        print("\n" + "-" * 80)
        print(f"Help for: {nat_detail_help['command']}".center(80))
        print("-" * 80)
        print(f"\n{nat_detail_help['description']}\n")
        print("Example Output:")
        print(nat_detail_help['example_output'])
        return None  # No actual command execution

    # Execute the NAT Detail command
    command = "show nat detail"
    try:
        output = get_and_parse_cli_output(command)
        if not suppress_output:
            print("\nNAT Detail Table Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)
        return output
    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
