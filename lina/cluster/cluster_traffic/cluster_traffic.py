from core.utils import get_and_parse_cli_output


def cluster_traffic(suppress_output=False, help_requested=False):
    """
    Retrieves and optionally displays the Cluster Traffic using 'show cluster traffic'.
    If help_requested=True, it prints command information instead of executing the command.
    """

    cluster_traffic_help = {
        'command': 'show cluster traffic',
        'description': (
            "Displays real-time and cumulative traffic statistics for the cluster. "
            "This information helps analyze load distribution across cluster nodes, "
            "monitor network throughput, and detect potential bottlenecks."
        ),
    }

    # If help is requested, print help content and exit the function
    if help_requested:
        print("\n" + "=" * 80)
        print(f"📖 Help for: {cluster_traffic_help['command']}".center(80))
        print("=" * 80)
        print(f"\n{cluster_traffic_help['description']}\n")
        return None  # No actual command execution

    try:
        # Execute 'show cluster traffic'
        output = get_and_parse_cli_output("show cluster traffic")

        if not suppress_output:
            print("\n📊 Cluster Traffic Statistics:")
            print("=" * 80)
            print(output)
            print("=" * 80)

        return output

    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
