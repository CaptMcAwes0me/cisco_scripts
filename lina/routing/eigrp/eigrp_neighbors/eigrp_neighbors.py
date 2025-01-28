# Description: This script retrieves and displays EIGRP interfaces.

from core.utils import get_and_parse_cli_output


def eigrp_neighbors():
    """Retrieves and displays EIGRP neighbors."""
    command = "show eigrp neighbors"
    try:
        output = get_and_parse_cli_output(command)
        print("\nEIGRP Neighbors Output:")
        print("-" * 80)
        print(output)
        print("-" * 80)
        return output
    except Exception as e:
        print(f"[!] Error: {e}")
        return ""
