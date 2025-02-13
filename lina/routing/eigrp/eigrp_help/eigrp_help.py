def eigrp_help():
    """Displays how different EIGRP commands relate to each other with practical examples."""

    help_sections = {
        "1. Checking EIGRP Configuration & Neighbor Relationships": [
            "🔹 Use `show run all router eigrp` to verify the active EIGRP configuration.",
            "🔹 Use `show eigrp neighbors` to check adjacency status with neighbors.",
            "🔹 Example:",
            "   1️⃣ Run: show run all router eigrp (Verify correct AS number and network statements)",
            "   2️⃣ Run: show eigrp neighbors (Ensure neighbors are forming correctly)",
            "   3️⃣ If a neighbor is missing, check: show eigrp interfaces (Confirm interfaces are enabled for EIGRP)",
        ],
        "2. Analyzing the EIGRP Topology & Feasible Successors": [
            "🔹 Use `show eigrp topology` to view all learned routes and feasible successors.",
            "🔹 Example:",
            "   1️⃣ Run: show eigrp topology (Verify feasible successor paths for redundancy)",
            "   2️⃣ Check the successor’s next hop and feasibility condition.",
        ],
        "3. Diagnosing Routing Issues in EIGRP": [
            "🔹 Use `show route all eigrp` to check the routes installed in the routing table.",
            "🔹 If a route is missing, check the topology table: `show eigrp topology`.",
            "🔹 Example:",
            "   1️⃣ Run: show route all eigrp (Ensure the expected routes are present)",
            "   2️⃣ If missing, check: show eigrp topology (Confirm if the route exists in EIGRP)",
            "   3️⃣ If the route is in topology but not in the RIB, verify: show eigrp rib-failure",
        ],
        "4. Monitoring EIGRP Traffic & Events": [
            "🔹 Use `show eigrp traffic` to analyze packet exchanges such as Hello, Update, and Queries.",
            "🔹 Use `show eigrp events` to check recent significant changes in the EIGRP process.",
            "🔹 Example:",
            "   1️⃣ Run: show eigrp traffic (Check for excessive Query or Update messages)",
            "   2️⃣ Run: show eigrp events (Identify recent topology changes and neighbor issues)",
        ],
        "5. Verifying EIGRP Interface Participation": [
            "🔹 Use `show eigrp interfaces` to check which interfaces are running EIGRP.",
            "🔹 Example:",
            "   1️⃣ Run: show eigrp interfaces (Ensure the correct interfaces are enabled)",
            "   2️⃣ If an interface is missing, verify: show run all router eigrp (Check network statements)",
        ]
    }

    print("\n" + "=" * 80)
    print("📘 EIGRP Help: Understanding Command Relationships 📘".center(80))
    print("=" * 80)

    for section, lines in help_sections.items():
        print(f"\n🟢 {section}")
        for line in lines:
            print(f"   {line}")

    print("\n" + "=" * 80)
    print("🔍 Tip: Use 'X?' to see help for a specific command (e.g., '4?' for EIGRP Neighbors).")
    print("=" * 80)
