from core.utils import get_and_parse_cli_output


def cluster_exec_nat_pool(suppress_output=False, help_requested=False):
    """
    Retrieves and optionally displays detailed NAT pool allocation information across
    all cluster members using 'cluster exec show nat pool'.
    If help_requested=True, it prints command information instead of executing the command.
    """

    cluster_exec_nat_pool_help = {
        'command': 'cluster exec show nat pool',
        'description': (
            "Executes 'show nat pool' on all members of the cluster, providing insights into "
            "NAT pool allocation per unit. This command is essential for diagnosing NAT pool distribution, "
            "troubleshooting dynamic NAT port exhaustion, and verifying allocation efficiency across NAT pools."
        ),
        'example_output': """
> cluster exec show nat pool
--------------------------------------------------------------------------------
ICMP PAT pool dynamic-pat, address 172.16.2.200, range 1-65535, allocated 2
TCP PAT pool dynamic-pat, address 172.16.2.200, range 1-1024, allocated 0
TCP PAT pool dynamic-pat, address 172.16.2.200, range 1024-65535, allocated 2
UDP PAT pool dynamic-pat, address 172.16.2.200, range 1-1024, allocated 0
UDP PAT pool dynamic-pat, address 172.16.2.200, range 1024-65535, allocated 2
--------------------------------------------------------------------------------
        """
    }

    # If help is requested, print help content and exit the function
    if help_requested:
        print("\n" + "=" * 80)
        print(f"📖 Help for: {cluster_exec_nat_pool_help['command']}".center(80))
        print("=" * 80)
        print(f"\n{cluster_exec_nat_pool_help['description']}\n")
        print("Example Output:")
        print(cluster_exec_nat_pool_help['example_output'])
        return None  # No actual command execution

    # Execute command to retrieve NAT pool information for all cluster members
    command = "cluster exec show nat pool"

    try:
        output = get_and_parse_cli_output(command)

        if not suppress_output:
            print("\nCluster Exec NAT Pool Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)

        return output

    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
