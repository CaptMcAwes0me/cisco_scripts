import re
from core.utils import get_and_parse_cli_output


def cluster_member_limit(suppress_output=False):
    """Retrieves and optionally displays the Cluster Member Limit using 'show cluster info'."""

    command = "show cluster info"

    try:
        output = get_and_parse_cli_output(command)

        # Use a regex to find the "Cluster Member Limit" value
        match = re.search(r"Cluster Member Limit\s*:\s*(\d+)", output)

        if match:
            cluster_member_limit = match.group(1)
        else:
            cluster_member_limit = "Unknown"

        if not suppress_output:
            print("\nCluster Member Limit Output:")
            print("-" * 80)
            print(f"Cluster Member Limit: {cluster_member_limit}")
            print("-" * 80)
            print(
                "\033[1;33m[NOTE]\033[0m: The Cluster Member Limit should be configured to match the number of cluster"
                " members to ensure stable cluster communication and performance regarding NAT pool exhaustion.\n")

        return cluster_member_limit

    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
