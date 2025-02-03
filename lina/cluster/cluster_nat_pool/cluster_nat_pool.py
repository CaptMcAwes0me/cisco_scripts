
from core.utils import get_and_parse_cli_output

def cluster_nat_pool(suppress_output=False):
    """Retrieves and optionally displays the Cluster NAT Pool using 'show nat pool cluster'."""

    command = "show nat pool cluster"

    try:
        output = get_and_parse_cli_output(command)

        if not suppress_output:
            print("\nCluster NAT Pool Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)

        return output

    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
