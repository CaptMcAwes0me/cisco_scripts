
from core.utils import get_and_parse_cli_output

def cluster_resource_usage(suppress_output=False):
    """Retrieves and optionally displays the Cluster Resource Usage using 'show cluster resource usage'."""

    command = "show cluster resource usage"

    try:
        output = get_and_parse_cli_output(command)

        if not suppress_output:
            print("\nCluster Resource Usage Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)

        return output

    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
