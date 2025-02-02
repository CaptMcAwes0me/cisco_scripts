# Description: This script retrieves the NAT proxy-arp table with 'show nat proxy-arp'.

from core.utils import get_and_parse_cli_output


def nat_proxy_arp(suppress_output=False):
    """Retrieves and optionally displays the NAT proxy-arp table with 'show nat proxy-arp'."""

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
