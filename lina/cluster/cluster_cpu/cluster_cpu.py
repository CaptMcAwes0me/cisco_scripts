from core.utils import get_and_parse_cli_output

def cluster_cpu(suppress_output=False, help_requested=False):
    """
    Retrieves and optionally displays the Cluster CPU utilization using 'show cluster cpu'.
    If help_requested=True, it prints command information instead of executing the command.
    """

    cluster_cpu_help = {
        'command': 'show cluster cpu',
        'description': (
            "Displays CPU utilization statistics for the entire cluster and individual units. "
            "Includes 5-second, 1-minute, and 5-minute average CPU usage values. "
            "Useful for diagnosing load balancing issues and CPU bottlenecks."
        ),
        'example_output': """
firepower# show cluster cpu
Usage Summary In Cluster:*********************************************
CPU Utilization for 5 seconds = 99%; 1 minute: 84% 5 minutes: 32%
unit-1-2(LOCAL):******************************************************
CPU Utilization for 5 seconds = 100%; 1 minute: 84% 5 minutes: 32%
unit-1-1:*************************************************************
CPU Utilization for 5 seconds = 100%; 1 minute: 84% 5 minutes: 32%
unit-2-2:*************************************************************
CPU Utilization for 5 seconds = 99%; 1 minute: 85% 5 minutes: 33%
unit-2-1:*************************************************************
CPU Utilization for 5 seconds = 99%; 1 minute: 83% 5 minutes: 31%
        """
    }

    # If help is requested, print help content and exit the function
    if help_requested:
        print("\n" + "=" * 80)
        print(f"📖 Help for: {cluster_cpu_help['command']}".center(80))
        print("=" * 80)
        print(f"\n{cluster_cpu_help['description']}\n")
        print("Example Output:")
        print(cluster_cpu_help['example_output'])
        return None  # No actual command execution

    try:
        # Execute 'show cluster cpu'
        output = get_and_parse_cli_output("show cluster cpu")

        if not suppress_output:
            print("\n🖥️ Cluster CPU Utilization:")
            print("=" * 80)
            print(output)
            print("=" * 80)

        return output

    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
