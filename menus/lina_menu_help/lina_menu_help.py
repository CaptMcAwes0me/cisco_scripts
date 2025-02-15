def lina_menu_help():
    """Provides guidance on Lina system commands and their practical applications."""

    help_sections = {
        "1. Verifying Lina System Information": [
            "🔹 Use `show version` to display the software and hardware details of the system.",
            "🔹 Example:",
            "   1️⃣ Run: show version",
            "      - Confirm the current software version and system uptime.",
        ],
        "2. Monitoring Network Address Translation (NAT)": [
            "🔹 Use `show running-config nat` to display all configured NAT rules.",
            "🔹 Use `show nat detail` to view active NAT translations with hit counts.",
            "🔹 Use `show xlate` to inspect real-time NAT translation entries.",
            "🔹 Example:",
            "   1️⃣ Run: show nat detail",
            "      - Identify which NAT rules are actively being used.",
            "   2️⃣ Run: show xlate",
            "      - Review dynamic and static NAT entries currently in use.",
        ],
        "3. Inspecting Routing Table and Protocols": [
            "🔹 Use `show route` to display the current routing table.",
            "🔹 Use `show route ospf` to view OSPF-learned routes.",
            "🔹 Use `show bgp summary` to inspect BGP peer status and route counts.",
            "🔹 Example:",
            "   1️⃣ Run: show route",
            "      - Confirm learned routes and their sources.",
            "   2️⃣ Run: show route ospf",
            "      - Check OSPF-advertised routes and network reachability.",
        ],
        "4. Monitoring VPN Tunnel Status": [
            "🔹 Use `show vpn-sessiondb anyconnect` to view active AnyConnect sessions.",
            "🔹 Use `show crypto ipsec sa` to examine active IPSec tunnels.",
            "🔹 Use `show crypto isakmp sa` to check IKE Phase 1 negotiations.",
            "🔹 Example:",
            "   1️⃣ Run: show vpn-sessiondb anyconnect",
            "      - Validate AnyConnect users and tunnel statistics.",
            "   2️⃣ Run: show crypto ipsec sa",
            "      - Review encryption and authentication details for IPSec tunnels.",
        ],
        "5. Checking High Availability (Failover) Status": [
            "🔹 Use `show failover` to check failover role, state, and sync status.",
            "🔹 Use `show failover history` to display failover event logs.",
            "🔹 Example:",
            "   1️⃣ Run: show failover",
            "      - Verify if the device is in Active or Standby state.",
            "   2️⃣ Run: show failover history",
            "      - Review any failover events and their timestamps.",
        ],
        "6. Logging and Monitoring System Events": [
            "🔹 Use `show logging` to display system logs.",
            "🔹 Example:",
            "   1️⃣ Run: show logging",
            "      - Review system events, errors, and warnings.",
        ],
        "7. Inspecting Cluster Status and Performance": [
            "🔹 Use `show cluster info` to review cluster membership and health status.",
            "🔹 Use `show cluster resource usage` to analyze CPU, memory, and connection usage across the cluster.",
            "🔹 Example:",
            "   1️⃣ Run: show cluster info",
            "      - Verify the number of active cluster members and their states.",
            "   2️⃣ Run: show cluster resource usage",
            "      - Monitor resource utilization across all cluster nodes.",
        ],
        "8. Diagnosing Block Memory Utilization": [
            "🔹 Use `show blocks` to inspect memory block allocation.",
            "🔹 Use `show blocks exhaustion history` to review memory exhaustion trends.",
            "🔹 Example:",
            "   1️⃣ Run: show blocks",
            "      - Identify memory blocks in use and available.",
            "   2️⃣ Run: show blocks exhaustion history",
            "      - Check if memory shortages have impacted system performance.",
        ],
    }

    print("\n" + "=" * 80)
    print("📘 Lina System Help: Command Usage and Practical Examples 📘".center(80))
    print("=" * 80)

    for section, lines in help_sections.items():
        print(f"\n🟢 {section}")
        for line in lines:
            print(f"   {line}")

    print("\n" + "=" * 80)
    print("🔍 Tip: Use 'X?' to see help for a specific command (e.g., '2?' for NAT troubleshooting).")
    print("=" * 80)
