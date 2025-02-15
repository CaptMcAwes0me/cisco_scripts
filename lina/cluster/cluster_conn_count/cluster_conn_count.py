from core.utils import get_and_parse_cli_output

def cluster_conn_count(suppress_output=False, help_requested=False):
    """
    Retrieves and optionally displays the Cluster Connection Count and Distribution.
    Uses 'show cluster info conn-distribution' and 'show cluster conn count'.
    If help_requested=True, it prints command information instead of executing the command.
    """

    cluster_conn_count_help = {
        'commands': ['show cluster info conn-distribution', 'show cluster conn count'],
        'description': (
            "Displays the total number of active connections within the cluster and their distribution across "
            "cluster members. This helps in analyzing connection load balancing and troubleshooting uneven traffic "
            "distribution issues."
        ),
        'example_output': """
firepower/master# show cluster info conn-distribution 
Unit            Total Conns (/sec)    Reg Conns (/sec)   Dir Conns (/sec)    Fwd Conns (/sec)
RTP-FW2             5                   2                   3                   0                   
RTP-FW1             5                   4                   1                   0                   

firepower# show cluster conn count
Total connections: 625
        """
    }

    # If help is requested, print help content and exit the function
    if help_requested:
        print("\n" + "=" * 80)
        print(f"Help for: {', '.join(cluster_conn_count_help['commands'])}".center(80))
        print("=" * 80)
        print(f"\n{cluster_conn_count_help['description']}\n")
        print("Example Output:")
        print(cluster_conn_count_help['example_output'])
        return None  # No actual command execution

    try:
        # Execute 'show cluster info conn-distribution'
        conn_distribution_output = get_and_parse_cli_output("show cluster info conn-distribution")

        # Execute 'show cluster conn count'
        conn_count_output = get_and_parse_cli_output("show cluster conn count")

        if not suppress_output:
            print("\nCluster Connection Distribution:")
            print("=" * 80)
            print(conn_distribution_output)
            print("=" * 80)

            print("\nCluster Connection Count:")
            print("=" * 80)
            print(conn_count_output)
            print("=" * 80)

        return conn_distribution_output, conn_count_output

    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
