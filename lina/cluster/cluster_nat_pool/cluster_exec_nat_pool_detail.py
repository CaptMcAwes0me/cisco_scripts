from core.utils import get_and_parse_cli_output


def cluster_exec_nat_pool_detail(suppress_output=False, help_requested=False):
    """
    Retrieves and optionally displays detailed NAT pool allocation information across
    all cluster members using 'cluster exec show nat pool detail'.
    If help_requested=True, it prints command information instead of executing the command.
    """

    cluster_exec_nat_pool_detail_help = {
        'command': 'cluster exec show nat pool detail',
        'description': (
            "Executes 'show nat pool detail' on all members of the cluster, providing detailed insights into "
            "NAT pool allocation per unit. This command is essential for diagnosing NAT pool distribution, "
            "troubleshooting dynamic NAT port exhaustion, and verifying allocation efficiency across NAT pools."
        ),
        'example_output': """
> cluster exec show nat pool detail
--------------------------------------------------------------------------------
TCP PAT pool outside_a, address 174.0.1.1
   Range: [1536-2047], Allocated: 56
   Range: [8192-8703], Allocated: 16
UDP PAT pool outside_a, address 174.0.1.1
   Range: [1536-2047], Allocated: 12
   Range: [8192-8703], Allocated: 25
TCP PAT pool outside_b, address 174.0.2.1
   Range: [47104-47615], Allocated: 39
   Range: [62464-62975], Allocated: 9
UDP PAT pool outside_b, address 174.0.2.1
   Range: [47104-47615], Allocated: 35
   Range: [62464-62975], Allocated: 27
--------------------------------------------------------------------------------
        """
    }

    # If help is requested, print help content and exit the function
    if help_requested:
        print("\n" + "=" * 80)
        print(f"📖 Help for: {cluster_exec_nat_pool_detail_help['command']}".center(80))
        print("=" * 80)
        print(f"\n{cluster_exec_nat_pool_detail_help['description']}\n")
        print("Example Output:")
        print(cluster_exec_nat_pool_detail_help['example_output'])
        return None  # No actual command execution

    # Execute command to retrieve detailed NAT pool information for all cluster members
    command = "cluster exec show nat pool detail"

    try:
        output = get_and_parse_cli_output(command)

        if not suppress_output:
            print("\nCluster Exec NAT Pool Detail Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)

        return output

    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
