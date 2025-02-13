def vrf_help():
    """Displays how different VRF commands relate to each other with practical examples."""

    help_sections = {
        "1. Viewing VRF Configuration": [
            "🔹 Use `show running-config all vrf` to verify VRF definitions, Route Distinguishers (RD), and Route Targets (RT).",
            "🔹 Use `show vrf` to check active VRFs and their associated interfaces.",
            "🔹 Example:",
            "   1️⃣ Run: show running-config all vrf (Check VRF configurations)",
            "   2️⃣ Run: show vrf (Confirm active VRFs and assigned interfaces)",
        ],
        "2. Checking VRF Route Processing": [
            "🔹 Use `show vrf detail` to view advanced VRF properties, including import/export RTs and assigned address families.",
            "🔹 Use `show vrf tableid` to verify the internal table ID assigned to each VRF.",
            "🔹 Example:",
            "   1️⃣ Run: show vrf detail (Review VRF import/export policies and associated interfaces)",
            "   2️⃣ Run: show vrf tableid (Identify VRF table mappings for routing lookup verification)",
        ],
        "3. Monitoring VRF Traffic": [
            "🔹 Use `show vrf counters` to monitor traffic per VRF, including packet and byte statistics.",
            "🔹 This is useful for diagnosing VRF-level congestion, forwarding issues, and policy routing effectiveness.",
            "🔹 Example:",
            "   1️⃣ Run: show vrf counters (Check per-VRF traffic flow statistics)",
        ],
        "4. Troubleshooting VRF Lock Issues": [
            "🔹 Use `show vrf lock` to check if any VRFs are locked, preventing updates to routing tables.",
            "🔹 Example:",
            "   1️⃣ Run: show vrf lock (Identify locked VRFs that may prevent routing updates)",
            "   2️⃣ Investigate if static routes or BGP processes require unlocking.",
        ],
    }

    print("\n" + "=" * 80)
    print("📘 VRF Help: Understanding Command Relationships 📘".center(80))
    print("=" * 80)

    for section, lines in help_sections.items():
        print(f"\n🟢 {section}")
        for line in lines:
            print(f"   {line}")

    print("\n" + "=" * 80)
    print("🔍 Tip: Use 'X?' to see help for a specific command (e.g., '2?' for Show VRF).")
    print("=" * 80)
