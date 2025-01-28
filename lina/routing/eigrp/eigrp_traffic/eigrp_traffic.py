# Description: This script retrieves and displays EIGRP traffic.

from core.utils import get_and_parse_cli_output


def eigrp_traffic():
    """Retrieves and displays EIGRP traffic."""
    command = "show eigrp traffic"
    try:
        output = get_and_parse_cli_output(command)
        print("\nEIGRP Traffic Output:")
        print("-" * 80)
        print(output)
        print("-" * 80)
        return output
    except Exception as e:
        print(f"[!] Error: {e}")
        return ""
