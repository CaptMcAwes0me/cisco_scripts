# Description: This script contains the Cluster menu and its associated functions.

from core.utils import display_formatted_menu
from lina.cluster.cluster_running_config.cluster_running_config import cluster_running_config
from lina.cluster.cluster_member_limit.cluster_member_limit import cluster_member_limit
from lina.cluster.cluster_nat_pool.cluster_nat_pool import cluster_nat_pool
from lina.cluster.cluster_resource_usage.cluster_resource_usage import cluster_resource_usage
from lina.cluster.cluster_mtu.cluster_mtu import cluster_mtu
from lina.cluster.cluster_conn_count.cluster_conn_count import cluster_conn_count
from lina.cluster.cluster_xlate_count.cluster_xlate_count import cluster_xlate_count
from lina.cluster.cluster_traffic.cluster_traffic import cluster_traffic
from lina.cluster.cluster_cpu.cluster_cpu import cluster_cpu
from lina.cluster.cluster_help.cluster_help import cluster_help


def cluster_menu():
    menu_options = {
        "1": ("Cluster Running Configuration", cluster_running_config),
        "2": ("Cluster Member Limit", cluster_member_limit),
        "3": ("Cluster NAT Pool", cluster_nat_pool),
        "4": ("Cluster Resource Usage", cluster_resource_usage),
        "5": ("Cluster MTU", cluster_mtu),
        "6": ("Cluster Conn Count", cluster_conn_count),
        "7": ("Cluster Xlate Count", cluster_xlate_count),
        "8": ("Cluster Traffic", cluster_traffic),
        "9": ("Cluster CPU", cluster_cpu),
        "10": ("Cluster Help", cluster_help),
        "0": ("Exit", None),
    }

    while True:
        # Prepare the menu options for display
        options_display = {key: description for key, (description, _) in menu_options.items()}
        display_formatted_menu("Cluster Menu", options_display)

        choice = input("Select an option (0-10): ").strip()

        if choice in menu_options:
            description, function = menu_options[choice]
            if function:  # If a function is assigned
                print("\n" + "-" * 80)
                print(f"Accessing {description}...".center(80))
                print("-" * 80)
                function()
            else:  # Exit condition
                print("\nExiting to previous menu...")
                break
        else:
            print("\n[!] Invalid choice. Please enter a number between 0 and 10.")
