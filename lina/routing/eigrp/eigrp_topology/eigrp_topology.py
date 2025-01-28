# Description: This script retrieves and displays EIGRP topology.

from core.utils import get_and_parse_cli_output


def eigrp_topology():
    """Retrieves and displays EIGRP topology."""
    command = "show eigrp topology"
    try:
        output = get_and_parse_cli_output(command)
        print("\nEIGRP Topology Output:")
        print("-" * 80)
        print(output)
        print("-" * 80)
        return output
    except Exception as e:
        print(f"[!] Error: {e}")
        return ""

