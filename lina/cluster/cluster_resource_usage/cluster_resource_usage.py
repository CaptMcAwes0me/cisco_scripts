from core.utils import get_and_parse_cli_output


def cluster_resource_usage(suppress_output=False, help_requested=False):
    """
    Retrieves and optionally displays the Cluster Resource Usage using 'show cluster resource usage'.
    If help_requested=True, it prints command information instead of executing the command.
    """

    cluster_resource_usage_help = {
        'command': 'show cluster resource usage',
        'description': (
            "Displays resource usage statistics across all cluster members. This command provides "
            "information on memory, SSH client sessions, storage, syslogs, connections, translations (XLATEs), "
            "hosts, MAC addresses, routes, and VPN session limits. This data helps troubleshoot performance "
            "issues and determine if the cluster is approaching any configured limits."
        ),
        'example_output': """
firepower# show cluster resource usage
Usage Summary In Cluster:*********************************************
Resource           Current  Peak  Limit       Denied   Context  
------------------------------------------------------------
memory             0        N/A   unlimited   0        System  
SSH Client         0        N/A   10          0        System  
Storage            0        N/A   unlimited   0        System  
Syslogs [rate]     0        N/A   N/A         0        System  
Conns              52       N/A   500000      0        System  
Xlates             52       N/A   N/A         0        System  
Hosts              38       N/A   N/A         0        System  
Conns [rate]       1        N/A   N/A         0        System  
Inspects [rate]    1        N/A   N/A         0        System  
Mac-addresses      0        N/A   32768       0        System  
Routes             38       N/A   unlimited   0        System  
Other VPN Sessions 0        N/A   500         0        System  
Other VPN Burst    0        N/A   500         0        System  
AnyConnect         0        N/A   500         0        System  
AnyConnect Burst   0        N/A   500         0        System  
IKEv1 in-negotiation 0      N/A   unlimited   0        System  
        """
    }

    # If help is requested, print help content and exit the function
    if help_requested:
        print("\n" + "=" * 80)
        print(f"Help for: {cluster_resource_usage_help['command']}".center(80))
        print("=" * 80)
        print(f"\n{cluster_resource_usage_help['description']}\n")
        print("Example Output:")
        print(cluster_resource_usage_help['example_output'])
        return None  # No actual command execution

    # Execute command to retrieve resource usage data
    command = "show cluster resource usage"

    try:
        output = get_and_parse_cli_output(command)

        if not suppress_output:
            print("\nCluster Resource Usage Output:")
            print("=" * 80)
            print(output)
            print("=" * 80)

        return output

    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
