def cluster_help():
    """Displays guidance on troubleshooting and managing clustering in Cisco Firepower devices,
       including common commands, troubleshooting techniques, and caveats."""

    help_sections = {
        "1. Verifying Cluster Configuration": [
            "🔹 Use `show run all cluster` to verify cluster-specific settings, including cluster group settings, health checks, and priorities.",
            "🔹 Example:",
            "   1️⃣ Run: show run all cluster (Review cluster-specific configurations)",
            "   2️⃣ Check for correct cluster-interface configuration and unit priorities.",
        ],
        "2. Checking Cluster Member Limits": [
            "🔹 Use `show cluster info` to review the configured limit for cluster members.",
            "🔹 Verify that the limit matches the intended number of cluster members to prevent NAT pool exhaustion.",
            "🔹 Example:",
            "   1️⃣ Run: show cluster info (Verify Cluster Member Limit)",
            "   2️⃣ Ensure that the number of active members does not exceed the limit.",
        ],
        "3. Diagnosing NAT Pool Issues": [
            "🔹 Use `show nat pool cluster` to view NAT pool configuration for the cluster.",
            "🔹 Example:",
            "   1️⃣ Run: show nat pool cluster (Inspect NAT pool details)",
            "   2️⃣ Check for available IP addresses in the NAT pool.",
        ],
        "4. Analyzing Cluster Resource Usage": [
            "🔹 Use `show cluster resource usage` to view usage statistics for memory, storage, connections, and VPN sessions.",
            "🔹 Example:",
            "   1️⃣ Run: show cluster resource usage (Review current usage for CPU, memory, and other resources)",
            "   2️⃣ Monitor for any resource bottlenecks.",
        ],
        "5. Monitoring Cluster Traffic and CPU": [
            "🔹 Use `show cluster traffic` to monitor the distribution of traffic among cluster members.",
            "🔹 Use `show cluster cpu` to view CPU utilization for the cluster and individual units.",
            "🔹 Example:",
            "   1️⃣ Run: show cluster traffic (Check for imbalanced traffic distribution)",
            "   2️⃣ Run: show cluster cpu (Monitor CPU usage for high utilization)",
        ],
        "6. Investigating Connection Issues": [
            "🔹 Use `show cluster conn count` to check the number of connections distributed among cluster members.",
            "🔹 Use `show cluster xlate count` to view the translation count for each member.",
            "🔹 Example:",
            "   1️⃣ Run: show cluster conn count (Inspect connection distribution)",
            "   2️⃣ Run: show cluster xlate count (Check translation counts for each unit)",
        ],
        "7. Common Clustering Troubleshooting Commands": [
            "🔹 `debug cluster` - Enables debugging for cluster operations.",
            "🔹 `show cluster history` - Displays past cluster events and failover logs.",
            "🔹 `show cluster Info` - Provides a summary of cluster state and individual unit roles.",
            "🔹 `show cluster interface-mode` - Checks the mode of the interfaces (Spanned vs Individual). .",
            "🔹 `capture <name> interface <intf> match ip host <src> host <dst>` - Captures traffic to debug clustering issues.",
            "🔹 `ping <peer-ip>` - Tests reachability between cluster members.",
        ],
        "8. Clustering Troubleshooting Techniques": [
            "🔹 **Check Cluster Health Status** - Use `show cluster info` to ensure all members are in a healthy state.",
            "🔹 **Investigate Cluster Failovers** - Use `show cluster history` to analyze recent failover events.",
            "🔹 **Verify Even Traffic Distribution** - Run `show cluster info loadbalance` to identify load imbalance issues.",
            "🔹 **Confirm Connection Failover Behavior** - Test failover by shutting down an interface and monitoring traffic continuity.",
            "🔹 **Ensure NAT Pool Availability** - Check for pool exhaustion using `show nat pool cluster` and 'show nat pool'.",
        ],
        "9. Common Clustering Caveats": [
            "🔹 **Cluster Control Link (CCL) Must Be Reliable** - If the CCL fails, clustering will break down.",
            "🔹 **Cluster Interface MTU** - Cluster interface MTU should be configured >100 bytes larger than Data interfaces.",
            "🔹 **Uneven Load Balancing** - If traffic isn’t distributed correctly, check NAT allocation, centralized features.adjacent switches.",
            "🔹 **Hardware and Software Version Mismatches** - All members must run the same hardware platform and software version.",
            "🔹 **Member-Limit Default 16** - If left default, 1 / ( X + 1 ), where X equals cluster members PAT ports will be unused.",
            "🔹 **NAT Pool Exhaustion** - If too many xlates exist, the cluster may run out of ports.",
        ],
    }

    print("\n" + "=" * 80)
    print("📘 Cluster Help: Troubleshooting, Commands, and Caveats 📘".center(80))
    print("=" * 80)

    for section, lines in help_sections.items():
        print(f"\n🟢 {section}")
        for line in lines:
            print(f"   {line}")

    print("\n" + "=" * 80)
    print("🔍 Tip: Use 'X?' to see help for a specific command (e.g., '7?' for Clustering Troubleshooting Commands).")
    print("=" * 80)
