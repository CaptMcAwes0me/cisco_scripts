def routing_help():
    """Displays how different routing protocols and commands relate to each other with practical examples."""

    help_sections = {
        "1. Viewing Global Routing Information": [
            "🔹 Use `show route all` to view all installed routes from all routing protocols.",
            "🔹 Use `show running-config all route` to verify static and dynamic route configurations.",
            "🔹 Example:",
            "   1️⃣ Run: show route all (Check all routing table entries)",
            "   2️⃣ Run: show running-config all route (Verify configured static and dynamic routes)",
        ],
        "2. Working with EIGRP": [
            "🔹 Use `show eigrp neighbors` to check EIGRP neighbor relationships.",
            "🔹 Use `show eigrp topology` to examine feasible successors and route paths.",
            "🔹 Example:",
            "   1️⃣ Run: show eigrp neighbors (Verify EIGRP adjacencies)",
            "   2️⃣ Run: show eigrp topology (Check alternate paths and feasible successors)",
        ],
        "3. Working with OSPF": [
            "🔹 Use `show ospf neighbor` to confirm OSPF adjacency formation.",
            "🔹 Use `show ospf database` to inspect link-state advertisements (LSAs).",
            "🔹 Example:",
            "   1️⃣ Run: show ospf neighbor (Verify adjacency state for each OSPF router)",
            "   2️⃣ Run: show ospf database (Check LSAs for troubleshooting OSPF issues)",
        ],
        "4. Working with BGP": [
            "🔹 Use `show bgp summary` to see BGP neighbor relationships and route advertisements.",
            "🔹 Use `show bgp neighbors` to inspect detailed peer information and routing policies.",
            "🔹 Example:",
            "   1️⃣ Run: show bgp summary (View overall BGP status and peer states)",
            "   2️⃣ Run: show bgp neighbors (Analyze BGP peer attributes and policies)",
        ],
        "5. Working with ISIS": [
            "🔹 Use `show isis neighbors` to check ISIS adjacency status.",
            "🔹 Use `show isis database` to view ISIS link-state database entries.",
            "🔹 Example:",
            "   1️⃣ Run: show isis neighbors (Verify ISIS neighbor establishment)",
            "   2️⃣ Run: show isis database (Check link-state entries for route propagation issues)",
        ],
        "6. Managing VRFs and Route Isolation": [
            "🔹 Use `show vrf detail` to check VRF configuration and associated interfaces.",
            "🔹 Use `show vrf tableid` to verify internal table IDs assigned to VRFs.",
            "🔹 Example:",
            "   1️⃣ Run: show vrf detail (Review VRF route import/export policies)",
            "   2️⃣ Run: show vrf tableid (Identify VRF-specific route lookup tables)",
        ],
    }

    print("\n" + "=" * 80)
    print("📘 Routing Help: Understanding Command Relationships 📘".center(80))
    print("=" * 80)

    for section, lines in help_sections.items():
        print(f"\n🟢 {section}")
        for line in lines:
            print(f"   {line}")

    print("\n" + "=" * 80)
    print("🔍 Tip: Use 'X?' to see help for a specific command (e.g., '2?' for EIGRP).")
    print("=" * 80)
