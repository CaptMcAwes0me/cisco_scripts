def cluster_help():
    """Displays guidance on troubleshooting and managing clustering in Cisco Firepower devices."""

    help_sections = {
        "1. Verifying Cluster Configuration": [
            "🔹 Use `Cluster Running Configuration` to verify cluster-specific settings, "
            "including cluster group settings, health checks, and priorities.",
            "🔹 Example:",
            "   1️⃣ Run: show run all cluster (Review cluster-specific configurations)",
            "   2️⃣ Check for correct cluster-interface configuration and unit priorities."
        ],
        "2. Checking Cluster Member Limits": [
            "🔹 Use `Cluster Member Limit` to review the configured limit for cluster members.",
            "🔹 Verify that the limit matches the intended number of cluster members to prevent NAT pool exhaustion.",
            "🔹 Example:",
            "   1️⃣ Run: show cluster info (Verify Cluster Member Limit)",
            "   2️⃣ Ensure that the number of active members does not exceed the limit."
        ],
        "3. Diagnosing NAT Pool Issues": [
            "🔹 Use `Cluster NAT Pool` to view NAT pool configuration for the cluster.",
            "🔹 Example:",
            "   1️⃣ Run: show nat pool cluster (Inspect NAT pool details)",
            "   2️⃣ Check for available IP addresses in the NAT pool."
        ],
        "4. Analyzing Cluster Resource Usage": [
            "🔹 Use `Cluster Resource Usage` to view usage statistics for memory, storage, connections, and VPN sessions.",
            "🔹 Example:",
            "   1️⃣ Run: show cluster resource usage (Review current usage for CPU, memory, and other resources)",
            "   2️⃣ Monitor for any resource bottlenecks."
        ],
        "5. Monitoring Cluster Traffic and CPU": [
            "🔹 Use `Cluster Traffic` to monitor the distribution of traffic among cluster members.",
            "🔹 Use `Cluster CPU` to view CPU utilization for the cluster and individual units.",
            "🔹 Example:",
            "   1️⃣ Run: show cluster traffic (Check for imbalanced traffic distribution)",
            "   2️⃣ Run: show cluster cpu (Monitor CPU usage for high utilization)"
        ],
        "6. Investigating Connection Issues": [
            "🔹 Use `Cluster Conn Count` to check the number of connections distributed among cluster members.",
            "🔹 Use `Cluster Xlate Count` to view the translation count for each member.",
            "🔹 Example:",
            "   1️⃣ Run: show cluster conn count (Inspect connection distribution)",
            "   2️⃣ Run: show cluster xlate count (Check translation counts for each unit)"
        ],
    }

    print("\n" + "=" * 80)
    print("📘 Cluster Help: Troubleshooting and Managing Clustering 📘".center(80))
    print("=" * 80)

    for section, lines in help_sections.items():
        print(f"\n🟢 {section}")
        for line in lines:
            print(f"   {line}")

    print("\n" + "=" * 80)
    print("🔍 Tip: Use 'X?' to see help for a specific command (e.g., '3?' for Cluster NAT Pool).")
    print("=" * 80)
