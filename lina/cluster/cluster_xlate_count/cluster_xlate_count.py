
from core.utils import get_and_parse_cli_output

def cluster_xlate_count(suppress_output=False):
    """Retrieves and optionally displays the Cluster Xlate Count using 'show cluster xlate count'."""

    command = "show cluster xlate count"

    try:
        output = get_and_parse_cli_output(command)

        if not suppress_output:
            print("\nCluster Xlate Count Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)

        return output

    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
