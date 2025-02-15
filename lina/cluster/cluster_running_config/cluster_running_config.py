from core.utils import get_and_parse_cli_output


def cluster_running_config(suppress_output=False, help_requested=False):
    """Retrieves and optionally displays the Cluster Running Config using 'show run all cluster'.
       If help_requested=True, it prints command information instead.
    """

    cluster_running_config_help = {
        'command': 'show running-config cluster',
        'description': (
            "Displays the full cluster configuration, including cluster group settings, "
            "priority, cluster-interface configurations, health-check parameters, and "
            "rejoin settings. This command helps validate cluster setup and confirm synchronization."
        ),
        'example_output': """
firepower# show running-config cluster 
cluster group ftd_cluster1
 key *****
 local-unit unit-1-1
 cluster-interface Port-channel48.204 ip 10.173.1.1 255.255.0.0
 priority 9
 health-check holdtime 3
 health-check data-interface auto-rejoin 3 5 2
 health-check cluster-interface auto-rejoin unlimited 5 1
 health-check system auto-rejoin 3 5 2
 health-check monitor-interface debounce-time 500
 site-id 1
 no unit join-acceleration
 enable
"""
    }

    # If help is requested, print help content and exit the function
    if help_requested:
        print("\n" + "=" * 80)
        print(f"📖 Help for: {cluster_running_config_help['command']}".center(80))
        print("=" * 80)
        print(f"\n{cluster_running_config_help['description']}\n")
        print("Example Output:")
        print(cluster_running_config_help['example_output'])
        return None  # No actual command execution

    # Execute the Cluster Running Configuration command
    command = "show run all cluster"
    try:
        output = get_and_parse_cli_output(command)
        if not suppress_output:
            print("\nCluster Running Config Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)
        return output
    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
