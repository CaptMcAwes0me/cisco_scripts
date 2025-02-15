def global_routing_help():
    """Displays how different Global Routing commands relate to each other with practical examples."""

    help_sections = {
        "1. Verifying Routing Configuration": [
            "🔹 Use `show running-config all route` to verify static routes and dynamic protocol configurations.",
            "🔹 Use `show running-config all router` to confirm routing protocol settings (OSPF, BGP, EIGRP, ISIS).",
            "🔹 Example:",
            "   1️⃣ Run: show running-config all route (Check for static routes and redistribution settings)",
            "   2️⃣ Run: show running-config all router (Confirm OSPF, BGP, or EIGRP configurations)",
        ],
        "2. Viewing the Routing Table": [
            "🔹 Use `show route all` to display all installed routes from different protocols (OSPF, BGP, EIGRP, etc.).",
            "🔹 If an expected route is missing, check `show asp table routing all` for hidden internal routes.",
            "🔹 Example:",
            "   1️⃣ Run: show route all (Verify if the route is installed and active)",
            "   2️⃣ If missing, check: show asp table routing all (Confirm ASP processing of the route)",
        ],
        "3. Diagnosing Route Processing (ASP Table)": [
            "🔹 Use `show asp table routing all` to review how the FTD processes routes internally.",
            "🔹 This table contains identity routes, policy-based routes, and VPN-related routes.",
            "🔹 If a route appears in `show asp table routing all` but not in `show route all`, it may be a VPN or special policy route.",
            "🔹 Example:",
            "   1️⃣ Run: show asp table routing all (Check if a route is internally processed)",
            "   2️⃣ If the route is missing from `show route all`, check if it's tied to VPNs or NAT rules.",
        ],
        "4. Troubleshooting Missing Routes": [
            "🔹 If a route is expected but missing from `show route all`, follow these steps:",
            "   1️⃣ Run: show running-config all route (Ensure the route is configured)",
            "   2️⃣ Run: show asp table routing all (Confirm the route is recognized internally)",
            "   3️⃣ If dynamic, check: show running-config all router (Verify protocol settings)",
        ],
    }

    print("\n" + "=" * 80)
    print("📘 Global Routing Help: Understanding Command Relationships 📘".center(80))
    print("=" * 80)

    for section, lines in help_sections.items():
        print(f"\n🟢 {section}")
        for line in lines:
            print(f"   {line}")

    print("\n" + "=" * 80)
    print("🔍 Tip: Use 'X?' to see help for a specific command (e.g., '3?' for Show Route All).")
    print("=" * 80)
