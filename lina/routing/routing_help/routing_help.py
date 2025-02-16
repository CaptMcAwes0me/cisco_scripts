def routing_help():
    """Displays technical details for each routing protocol, including metrics, administrative distance, troubleshooting, and protocol specifics."""

    help_sections = {
        "1. Global Routing Overview": [
            "🔹 Routing is the process of selecting a path for traffic in a network.",
            "🔹 The FTD supports both static and dynamic routing protocols.",
            "🔹 The routing table is built based on the best available paths.",
            "🔹 Administrative Distance (AD) is used to prioritize routes when multiple sources provide the same destination.",
        ],
        "2. EIGRP (Enhanced Interior Gateway Routing Protocol)": [
            "🔹 Type: Dynamic, Distance-Vector Protocol (Cisco Proprietary)",
            "🔹 Administrative Distance: 90 (internal), 170 (external)",
            "🔹 Metric: Uses a composite metric (Bandwidth, Delay, Reliability, Load, MTU).",
            "🔹 Protocol: Uses RTP (Reliable Transport Protocol) over IP protocol 88.",
            "🔹 Troubleshooting:",
            "   - If neighbors are not forming, check: `show eigrp neighbors` and ensure proper authentication if configured.",
            "   - If routes are missing, verify `show eigrp topology` and confirm route filtering is not blocking updates.",
            "   - If convergence is slow, review `show eigrp events` and check for high CPU or memory utilization.",
        ],
        "3. OSPF (Open Shortest Path First)": [
            "🔹 Type: Dynamic, Link-State Protocol (Open Standard)",
            "🔹 Administrative Distance: 110",
            "🔹 Metric: Cost (Based on cumulative interface bandwidth)",
            "🔹 Protocol: Uses IP protocol 89 for communication.",
            "🔹 Areas: Uses hierarchical design with Areas (Backbone: Area 0).",
            "🔹 Troubleshooting:",
            "   - If neighbors are stuck in `INIT` or `EXSTART`, check MTU mismatches (`show ospf interface`).",
            "   - If routes are missing, verify area configuration (`show ospf database`).",
            "   - If convergence is slow, review LSA types and SPF calculations (`show ospf events`).",
        ],
        "4. BGP (Border Gateway Protocol)": [
            "🔹 Type: Dynamic, Path-Vector Protocol (Used for Internet Routing)",
            "🔹 Administrative Distance: 20 (External BGP), 200 (Internal BGP)",
            "🔹 Metric: Uses AS-Path, Weight, Local Preference, MED.",
            "🔹 Protocol: Uses TCP port 179.",
            "🔹 Troubleshooting:",
            "   - If a session is stuck in `Idle` or `Active`, check `show bgp summary` and ensure the neighbor is reachable.",
            "   - If routes are not propagating, verify `show bgp ipv4 unicast` and confirm outbound policies are not filtering updates.",
            "   - If suboptimal routing occurs, inspect `show bgp path` and adjust attributes like local preference and MED.",
        ],
        "5. ISIS (Intermediate System to Intermediate System)": [
            "🔹 Type: Dynamic, Link-State Protocol (Used in ISP Networks)",
            "🔹 Administrative Distance: 115",
            "🔹 Metric: Uses a wide metric based on cost (default = 10).",
            "🔹 Protocol: Uses CLNP (Connectionless Network Protocol), encapsulated in Layer 2.",
            "🔹 Troubleshooting:",
            "   - If adjacency issues occur, ensure interfaces are properly configured with `show clns neighbors`.",
            "   - If routes are missing, verify `show isis database` and confirm LSPs are being exchanged.",
            "   - If path selection is incorrect, check `show isis route` and adjust metrics as necessary.",
        ],
        "6. VRF (Virtual Routing and Forwarding)": [
            "🔹 Type: Used for network segmentation and multi-tenant routing.",
            "🔹 Purpose: Allows multiple routing tables on a single device.",
            "🔹 Common Commands: `show vrf detail`, `show vrf tableid`.",
            "🔹 Troubleshooting:",
            "   - If a route is missing from a VRF, confirm its presence with `show route vrf <name>`.",
            "   - If an interface is not part of a VRF, check `show run interface <intf>` for correct VRF assignment.",
        ],
        "7. Static Routing": [
            "🔹 Type: Manually configured routes, used when no dynamic protocol is needed.",
            "🔹 Administrative Distance: 1 (Higher priority than dynamic routes).",
            "🔹 Example: `route outside 0.0.0.0 0.0.0.0 192.168.1.1` (Sets default gateway).",
        ],
    }

    print("\n" + "=" * 80)
    print("📘 Routing Help: Protocol-Specific Information 📘".center(80))
    print("=" * 80)

    for section, lines in help_sections.items():
        print(f"\n🟢 {section}")
        for line in lines:
            print(f"   {line}")

    print("\n" + "=" * 80)
    print("🔍 Tip: Use 'X?' to see help for a specific command (e.g., '2?' for EIGRP).")
    print("=" * 80)
