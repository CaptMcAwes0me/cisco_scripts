
from core.utils import get_and_parse_cli_output

def cluster_conn_count(suppress_output=False):
    """Retrieves and optionally displays the Cluster Conn Count using 'show cluster conn count'."""

    command = "show cluster conn count"

    try:
        output = get_and_parse_cli_output(command)

        if not suppress_output:
            print("\nCluster Conn Count Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)

        return output

    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
