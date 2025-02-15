from core.utils import get_and_parse_cli_output
import re


def cluster_nat_pool(suppress_output=False, help_requested=False):
    """
    Retrieves and optionally displays the Cluster NAT Pool using 'show nat pool cluster summary'
    followed by 'show nat pool cluster'.
    If help_requested=True, it prints command information instead of executing commands.
    """

    cluster_nat_pool_help = {
        'command': 'show nat pool cluster summary & show nat pool cluster',
        'description': (
            "Displays a summary of NAT pool usage in the cluster, followed by the allocation of "
            "Port Address Translation (PAT) pools. These commands help in troubleshooting NAT resource "
            "distribution, ensuring balanced load and efficient IP address management among cluster members."
        ),
        'example_output': """
> show nat pool cluster summary
port-blocks count display order: total, unit-A, unit-B, unit-C, unit-D
IP outside_a:src_map_a, 174.0.1.20 (128 - 32/32/32/32)
IP outside_a:src_map_a, 174.0.1.21 (128 - 36/32/32/28)
IP outside_b:src_map_b, 174.0.1.22 (128 - 31/32/32/33)

> show nat pool cluster
IP outside_a:src_map_a 174.0.1.20
               [1536 – 2047], owner A, backup B
               [8192 – 8703], owner A, backup B
               [4089 – 4600], owner B, backup A
               [11243 – 11754], owner B, backup A
IP outside_a:src_map_a 174.0.1.21
               [1536 – 2047], owner A, backup B
               [8192 – 8703], owner A, backup B
               [4089 – 4600], owner B, backup A
               [11243 – 11754], owner B, backup A
        """
    }

    # If help is requested, print help content and exit the function
    if help_requested:
        print("\n" + "=" * 80)
        print(f"📖 Help for: {cluster_nat_pool_help['command']}".center(80))
        print("=" * 80)
        print(f"\n{cluster_nat_pool_help['description']}\n")
        print("Example Output:")
        print(cluster_nat_pool_help['example_output'])
        return None  # No actual command execution

    # Execute NAT Pool Summary command first
    command_summary = "show nat pool cluster summary"
    command_detail = "show nat pool cluster"

    try:
        summary_output = get_and_parse_cli_output(command_summary)
        detail_output = get_and_parse_cli_output(command_detail)

        if not suppress_output:
            print("\nCluster NAT Pool Summary Output:")
            print("-" * 80)

            # Parse and format the summary output
            parsed_summary = []
            lines = summary_output.splitlines()
            for line in lines:
                match = re.match(r"IP\s+(\S+),\s+(\d+\.\d+\.\d+\.\d+)\s+\((\d+\s+\-\s+[\d/]+)\)", line)
                if match:
                    interface, ip, block_info = match.groups()
                    parsed_summary.append(f"🔹 Interface: {interface}, IP: {ip}, Port Blocks: {block_info}")

            if parsed_summary:
                print("\n".join(parsed_summary))
            else:
                print(summary_output)  # Fallback to raw output if parsing fails

            print("-" * 80)

            print("\nCluster NAT Pool Detailed Output:")
            print("-" * 80)
            print(detail_output)
            print("-" * 80)

        return summary_output, detail_output

    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
