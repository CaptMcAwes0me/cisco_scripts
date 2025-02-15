# Description: This script contains the Cluster menu and its associated functions.

from core.utils import display_formatted_menu
from lina.cluster.cluster_running_config.cluster_running_config import cluster_running_config
from lina.cluster.cluster_member_limit.cluster_member_limit import cluster_member_limit
from lina.cluster.cluster_nat_pool.cluster_nat_pool import cluster_nat_pool
from lina.cluster.cluster_nat_pool.cluster_exec_nat_pool_detail import cluster_exec_nat_pool_detail
from lina.cluster.cluster_resource_usage.cluster_resource_usage import cluster_resource_usage
from lina.cluster.cluster_mtu.cluster_mtu import cluster_mtu
from lina.cluster.cluster_conn_count.cluster_conn_count import cluster_conn_count
from lina.cluster.cluster_xlate_count.cluster_xlate_count import cluster_xlate_count
from lina.cluster.cluster_traffic.cluster_traffic import cluster_traffic
from lina.cluster.cluster_cpu.cluster_cpu import cluster_cpu
from lina.cluster.cluster_help.cluster_help import cluster_help


def cluster_menu():
    """Displays a menu for cluster-related tasks.
       Supports 'X?' functionality to display help for each menu option.
    """

    menu_options = {
        "1": ("Cluster Running Configuration", cluster_running_config),
        "2": ("Cluster Member Limit", cluster_member_limit),
        "3": ("Cluster NAT Pool", cluster_nat_pool),
        "4": ("Cluster NAT Pool (Cluster Exec)", cluster_exec_nat_pool_detail),
        "5": ("Cluster Resource Usage", cluster_resource_usage),
        "6": ("Cluster MTU", cluster_mtu),
        "7": ("Cluster Conn Count", cluster_conn_count),
        "8": ("Cluster Xlate Count", cluster_xlate_count),
        "9": ("Cluster Traffic", cluster_traffic),
        "10": ("Cluster CPU", cluster_cpu),
        "11": ("Cluster Help", cluster_help),
        "0": ("Exit", None),
    }

    while True:
        # Prepare menu display
        options_display = {key: description for key, (description, _) in menu_options.items()}
        display_formatted_menu("Cluster Menu", options_display)

        choice = input("Select an option (0-11) or enter '?' for help (e.g., '3?'): ").strip()

        # Handle 'X?' help functionality
        if choice.endswith("?"):
            base_choice = choice[:-1]  # Remove "?" from input
            if base_choice in menu_options:
                description, function = menu_options[base_choice]

                # Special case: `cluster_help` runs directly
                if function == cluster_help:
                    function()
                elif function:
                    print("\n" + "=" * 80)
                    print(f"📖 Help for: {description}".center(80))
                    print("=" * 80)
                    function(help_requested=True)  # Call function in help mode
                else:
                    print("\n[!] Help not available for this option.")
            else:
                print("\n[!] Invalid choice. Please enter a valid number followed by '?' (e.g., '2?').")

        elif choice in menu_options:
            description, function = menu_options[choice]
            if function:
                print("\n" + "-" * 80)
                print(f"Accessing {description}...".center(80))
                print("-" * 80)
                function()  # Normal function execution
            else:
                print("\nExiting to previous menu...")
                break

        else:
            print("\n[!] Invalid choice. Please enter a number between 0 and 11.")
