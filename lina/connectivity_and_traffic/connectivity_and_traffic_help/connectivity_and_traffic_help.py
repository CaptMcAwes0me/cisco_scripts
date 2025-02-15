# Description: This script provides help documentation for Connectivity and Traffic commands.

def connectivity_and_traffic_help():
    """Displays how different Connectivity and Traffic commands relate to each other with practical examples."""

    help_sections = {
        "1. Viewing ARP Table Entries": [
            "🔹 Use `show arp` to display the ARP table, including resolved IP-to-MAC mappings.",
            "🔹 Use `show arp | include <IP>` to filter by a specific IP address.",
            "🔹 Example:",
            "   1️⃣ Run: show arp (View all ARP table entries)",
            "   2️⃣ Run: show arp | include 192.168.1.1 (Check for a specific IP entry)",
        ],
        "2. Checking Active Connections": [
            "🔹 Use `show conn detail` to display active connections, including NAT translations and session timers.",
            "🔹 Use `show conn address <IP>` to filter connections by a specific IP address.",
            "🔹 Example:",
            "   1️⃣ Run: show conn detail (Check all active connections)",
            "   2️⃣ Run: show conn address 10.0.0.1 (Find connections for a specific host)",
        ],
        "3. Monitoring SLA Configuration & State": [
            "🔹 Use `show sla monitor configuration` to view SLA tracking policies and settings.",
            "🔹 Use `show sla monitor operational-state` to check if SLAs are up/down.",
            "🔹 Example:",
            "   1️⃣ Run: show sla monitor configuration (Verify SLA tracking settings)",
            "   2️⃣ Run: show sla monitor operational-state (Check real-time SLA status)",
        ],
        "4. Analyzing Firewall Traffic": [
            "🔹 Use `show traffic` to monitor traffic statistics, including packets per second and bandwidth usage.",
            "🔹 Example:",
            "   1️⃣ Run: show traffic (View global traffic statistics)",
        ],
        "5. Viewing Performance Monitoring Statistics": [
            "🔹 Use `show perfmon` to display real-time firewall performance metrics.",
            "🔹 Example:",
            "   1️⃣ Run: show perfmon (Check firewall session rates, packet rates, and CPU load)",
        ],
        "6. Examining Service Policy & QoS": [
            "🔹 Use `show service-policy` to review applied policies and their traffic handling statistics.",
            "🔹 Use `show service-policy interface` to check QoS enforcement per interface.",
            "🔹 Example:",
            "   1️⃣ Run: show service-policy (View policy statistics globally)",
            "   2️⃣ Run: show service-policy interface GigabitEthernet0/1 (Check policy for a specific interface)",
        ],
    }

    print("\n" + "=" * 80)
    print("📘 Connectivity and Traffic Help: Understanding Command Relationships 📘".center(80))
    print("=" * 80)

    for section, lines in help_sections.items():
        print(f"\n🟢 {section}")
        for line in lines:
            print(f"   {line}")

    print("\n" + "=" * 80)
    print("🔍 Tip: Use 'X?' to see help for a specific command (e.g., '4?' for Traffic Monitoring).")
    print("=" * 80)
