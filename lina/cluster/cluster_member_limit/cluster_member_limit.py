import re
from core.utils import get_and_parse_cli_output

def cluster_member_limit(suppress_output=False, help_requested=False):
    """Retrieves and optionally displays the Cluster Member Limit using 'show cluster info'.
       If help_requested=True, it prints command information instead.
    """

    cluster_member_limit_help = {
        'command': 'show cluster info',
        'description': (
            "Displays the current cluster member limit, which defines the maximum number of "
            "devices allowed in a cluster. This setting ensures proper resource distribution and "
            "prevents issues such as NAT pool exhaustion in a clustered firewall deployment."
        ),
        'example_output': """
> show cluster info
Cluster asa_cluster1: On
     Interface mode: spanned
 Cluster Member Limit : 16
     This is "unit-1-1" in state MASTER
         ID        : 0
         Site ID   : 1
         Version   : 9.17(1)
         Serial No.: SN
         CCL IP    : 10.10.10.1
         CCL MAC   : dead.dead.dead
         Module    : FPR4K-SM-24
        """
    }

    # If help is requested, print help content and exit the function
    if help_requested:
        print("\n" + "=" * 80)
        print(f"Help for: {cluster_member_limit_help['command']}".center(80))
        print("=" * 80)
        print(f"\n{cluster_member_limit_help['description']}\n")
        print("Example Output:")
        print(cluster_member_limit_help['example_output'])
        return None  # No actual command execution

    # Execute the Cluster Info command
    command = "show cluster info"
    try:
        output = get_and_parse_cli_output(command)

        # Use regex to find the "Cluster Member Limit" value
        match = re.search(r"Cluster Member Limit\s*:\s*(\d+)", output)
        cluster_member_limit = match.group(1) if match else "Unknown"

        if not suppress_output:
            print("\nCluster Member Limit Output:")
            print("-" * 80)
            print(f"Cluster Member Limit: {cluster_member_limit}")
            print("-" * 80)
            print(
                "⚠️ The Cluster Member Limit should be configured to match the number of cluster "
                "members to ensure stable cluster communication and performance regarding NAT pool exhaustion. ⚠️ \n")

        return cluster_member_limit

    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
