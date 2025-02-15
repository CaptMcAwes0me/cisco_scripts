from core.utils import get_and_parse_cli_output


def cluster_xlate_count(suppress_output=False, help_requested=False):
    """
    Retrieves and optionally displays the Cluster Xlate Count using 'show cluster xlate count'.
    If help_requested=True, it prints command information instead of executing the command.
    """

    cluster_xlate_count_help = {
        'command': 'show cluster xlate count',
        'description': (
            "Displays the total number of active translation (xlate) entries across the cluster. "
            "This command is useful for monitoring NAT translations and identifying excessive "
            "or unexpected NAT usage that could impact cluster performance."
        )
    }

    # If help is requested, print help content and exit the function
    if help_requested:
        print("\n" + "=" * 80)
        print(f"📖 Help for: {cluster_xlate_count_help['command']}".center(80))
        print("=" * 80)
        print(f"\n{cluster_xlate_count_help['description']}\n")
        return None  # No actual command execution

    # Execute command to retrieve the cluster xlate count
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
