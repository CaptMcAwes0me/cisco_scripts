import os
from datetime import datetime
from lina.cluster.cluster_running_config.cluster_running_config import cluster_running_config
from lina.cluster.cluster_member_limit.cluster_member_limit import cluster_member_limit
from lina.cluster.cluster_nat_pool.cluster_nat_pool import cluster_nat_pool
from lina.cluster.cluster_resource_usage.cluster_resource_usage import cluster_resource_usage
from lina.cluster.cluster_mtu.cluster_mtu import cluster_mtu
from lina.cluster.cluster_conn_count.cluster_conn_count import cluster_conn_count
from lina.cluster.cluster_xlate_count.cluster_xlate_count import cluster_xlate_count
from lina.cluster.cluster_traffic.cluster_traffic import cluster_traffic
from lina.cluster.cluster_cpu.cluster_cpu import cluster_cpu
from lina.cluster.cluster_nat_pool.cluster_exec_nat_pool import cluster_exec_nat_pool_detail


def dump_all_cluster_data():
    """Gathers output from all Cluster commands and writes them to a log file under /var/log/fp_troubleshooting_data."""

    # Define the directory path
    troubleshooting_dir = "/var/log/fp_troubleshooting_data"

    # Check if the directory exists, if not, create it
    if not os.path.exists(troubleshooting_dir):
        try:
            os.makedirs(troubleshooting_dir)
            print(f"[+] Created directory: {troubleshooting_dir}")
        except Exception as e:
            print(f"[!] Error creating directory: {e}")
            return

    # Generate timestamp for the log file
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = os.path.join(troubleshooting_dir, f"{timestamp}_cluster_dump.log")

    try:
        # Gather outputs
        data_to_dump = [
            ("Cluster Running Config", cluster_running_config(suppress_output=True)),
            ("Cluster Member Limit", cluster_member_limit(suppress_output=True)),
            ("Cluster NAT Pool", cluster_nat_pool(suppress_output=True)),
            ("Cluster NAT Pool Detail (Cluster Exec)", cluster_exec_nat_pool_detail(suppress_output=True)),
            ("Cluster Resource Usage", cluster_resource_usage(suppress_output=True)),
            ("Cluster MTU", cluster_mtu(suppress_output=True)),
            ("Cluster Conn Count", cluster_conn_count(suppress_output=True)),
            ("Cluster Xlate Count", cluster_xlate_count(suppress_output=True)),
            ("Cluster Traffic", cluster_traffic(suppress_output=True)),
            ("Cluster CPU", cluster_cpu(suppress_output=True))
        ]

        # Write all outputs to the log file
        with open(log_file, "w") as f:
            for title, output in data_to_dump:
                f.write(f"{'=' * 80}\n")
                f.write(f"{title}\n")
                f.write(f"{'-' * 80}\n")
                f.write(f"{output}\n")
                f.write(f"{'=' * 80}\n\n")

        print(f"\n[+] All Cluster data written to: {log_file}")

    except Exception as e:
        print(f"[!] Error writing Cluster data to file: {e}")
