def ospf_help():
    """Displays how different OSPF commands relate to each other with practical examples."""

    help_sections = {
        "1. Verifying OSPF Configuration & Process": [
            "🔹 Use `show run all router ospf` to verify OSPF process settings, areas, and interfaces.",
            "🔹 Use `show ospf all` to get a high-level summary of OSPF, including areas, SPF runs, and LSAs.",
            "🔹 Example:",
            "   1️⃣ Run: show run all router ospf (Confirm process ID, network statements, and area assignments)",
            "   2️⃣ Run: show ospf all (Verify general OSPF health, neighbor count, and LSAs)",
        ],
        "2. Checking OSPF Neighbor Adjacencies": [
            "🔹 Use `show ospf neighbor` to check if neighbors have formed adjacencies.",
            "🔹 If an expected neighbor is missing, check interface status using `show ospf interface`.",
            "🔹 Example:",
            "   1️⃣ Run: show ospf neighbor (Confirm if neighbors are FULL or stuck in INIT/TWO-WAY)",
            "   2️⃣ If neighbors are missing, check: show ospf interface (Verify interface OSPF state)",
            "   3️⃣ If the interface is down, check: show run all router ospf (Confirm network statements)",
        ],
        "3. Investigating OSPF Route Installation": [
            "🔹 Use `show ospf rib` to see which OSPF routes are installed in the routing table.",
            "🔹 If an expected route is missing, check `show ospf database` to confirm if LSAs exist.",
            "🔹 Example:",
            "   1️⃣ Run: show ospf rib (Ensure expected routes are installed in the RIB)",
            "   2️⃣ If a route is missing, check: show ospf database (Verify LSA presence)",
            "   3️⃣ If the LSA exists but isn’t in the RIB, check: show ospf statistics (Look for SPF issues)",
        ],
        "4. Diagnosing OSPF Database Issues": [
            "🔹 Use `show ospf database` to review all LSAs, including Router, Network, and External LSAs.",
            "🔹 Use `show ospf border-routers` to check for ABRs/ASBRs handling inter-area/external routes.",
            "🔹 Example:",
            "   1️⃣ Run: show ospf database (Confirm LSAs are present and valid)",
            "   2️⃣ Run: show ospf border-routers (Check ABRs/ASBRs distributing routes)",
        ],
        "5. Monitoring OSPF SPF & Traffic": [
            "🔹 Use `show ospf statistics` to review SPF calculations, LSA updates, and neighbor changes.",
            "🔹 Use `show ospf traffic` to analyze packet exchange counts (Hello, LSU, LSR, LSAck).",
            "🔹 Example:",
            "   1️⃣ Run: show ospf statistics (Check for excessive SPF recalculations)",
            "   2️⃣ If SPF recalculations are frequent, check: show ospf traffic (Look for LSA flooding)",
        ],
        "6. Ensuring OSPF NSF (Non-Stop Forwarding) Functionality": [
            "🔹 Use `show ospf nsf` to confirm if NSF is enabled and whether it’s operating correctly.",
            "🔹 Example:",
            "   1️⃣ Run: show ospf nsf (Verify NSF capability and last recovery status)",
        ],
    }

    print("\n" + "=" * 80)
    print("📘 OSPF Help: Understanding Command Relationships 📘".center(80))
    print("=" * 80)

    for section, lines in help_sections.items():
        print(f"\n🟢 {section}")
        for line in lines:
            print(f"   {line}")

    print("\n" + "=" * 80)
    print("🔍 Tip: Use 'X?' to see help for a specific command (e.g., '4?' for OSPF Database).")
    print("=" * 80)
