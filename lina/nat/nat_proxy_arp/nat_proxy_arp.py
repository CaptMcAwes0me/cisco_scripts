from core.utils import get_and_parse_cli_output

def nat_proxy_arp(suppress_output=False, help_requested=False):
    """
    Retrieves and optionally displays the NAT proxy ARP table using 'show nat proxy-arp'.
    If help_requested=True, it prints the help information instead.
    """

    nat_proxy_arp_help = {
        'command': 'show nat proxy-arp',
        'description': (
            "Displays the NAT proxy ARP table, showing runtime representations of NAT proxy ARP entries. "
            "This command is useful for verifying which NAT rules have proxy ARP enabled and ensuring that "
            "the device is responding to ARP requests on behalf of the specified IP addresses. Proper proxy ARP "
            "configuration is crucial for the correct routing of packets in NAT scenarios."
        ),
        'example_output': """
Nat Proxy-arp Table
id=0x00007f5558bbbfc0, ip/id=10.10.1.134, mask=255.255.255.255 ifc=test2
    config:(inside) to (test2) source dynamic inside_v6 outside_v4_pat destination static inside_v6_nat any
id=0x00007f5558bbbfc0, ip/id=10.10.1.135, mask=255.255.255.255 ifc=test2
    config:(inside) to (test2) source dynamic inside_v6 outside_v4_pat destination static inside_v6_nat any
id=0x00007f55595ad2c0, ip/id=10.86.118.2, mask=255.255.255.255 ifc=inside
    config:(inside) to (test2) source dynamic inside_v6 interface dns
id=0x00007f5559424e80, ip/id=10.100.10.1, mask=255.255.255.255 ifc=NP Identity Ifc
    config:(any) to (any) source dynamic src_network pat-pool mapped-pat-pool
id=0x00007f5559424e80, ip/id=10.100.10.2, mask=255.255.255.255 ifc=NP Identity Ifc
    config:(any) to (any) source dynamic src_network pat-pool mapped-pat-pool
        """
    }

    # If help is requested, print help content and exit the function
    if help_requested:
        print("\n" + "-" * 80)
        print(f"Help for: {nat_proxy_arp_help['command']}".center(80))
        print("-" * 80)
        print(f"\n{nat_proxy_arp_help['description']}\n")
        print("Example Output:")
        print(nat_proxy_arp_help['example_output'])
        return None  # No actual command execution

    # Execute the NAT Proxy ARP command
    command = "show nat proxy-arp"
    try:
        output = get_and_parse_cli_output(command)
        if not suppress_output:
            print("\nNAT Proxy-ARP Table Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)
        return output
    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
