from core.utils import get_and_parse_cli_output

def nat_pool(suppress_output=False, help_requested=False):
    """
    Retrieves and optionally displays the NAT pool using 'show nat pool'.
    If help_requested=True, it prints the help information instead.
    """

    nat_pool_help = {
        'command': 'show nat pool',
        'description': (
            "Displays the current NAT port address translation (PAT) pools, including the protocol, interface, "
            "mapped IP address, port ranges, and the number of allocated ports. This command is useful for monitoring "
            "the utilization of NAT resources and ensuring that there are sufficient ports available for translation."
        ),
        'example_output': """
TCP inside, address 10.76.11.25, range 1-511, allocated 0
TCP inside, address 10.76.11.25, range 512-1023, allocated 0
TCP inside, address 10.76.11.25, range 1024-65535, allocated 1
        """
    }

    # If help is requested, print help content and exit the function
    if help_requested:
        print("\n" + "-" * 80)
        print(f"Help for: {nat_pool_help['command']}".center(80))
        print("-" * 80)
        print(f"\n{nat_pool_help['description']}\n")
        print("Example Output:")
        print(nat_pool_help['example_output'])
        return None  # No actual command execution

    # Execute the NAT Pool command
    try:
        output = get_and_parse_cli_output(command)
        if not suppress_output:
            print("\nNAT Pool Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)
        return output
    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
