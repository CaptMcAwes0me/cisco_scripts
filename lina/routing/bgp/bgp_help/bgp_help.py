def bgp_help():
    """Displays how different BGP commands relate to each other with practical examples."""

    help_sections = {
        "1. BGP Summary & Neighbor Relationships": [
            "🔹 Use `show bgp summary` to get an overview of BGP peers, AS numbers, and prefixes received.",
            "🔹 If a neighbor is missing, check `show bgp neighbors` to see session state.",
            "🔹 Example:",
            "   1️⃣ Run: show bgp summary",
            "   2️⃣ If a neighbor is in IDLE state, check: show bgp neighbors",
            "   3️⃣ Ensure it is correctly configured in: show running-config all router bgp",
        ],
        "2. Checking Advertised and Received Routes": [
            "🔹 Use `show bgp neighbor <neighbor> advertised-routes` to see what prefixes are being sent.",
            "🔹 Use `show bgp ipv4 unicast` to check received routes.",
            "🔹 Example:",
            "   1️⃣ Run: show bgp ipv4 unicast  (to see what routes are learned)",
            "   2️⃣ Run: show bgp neighbor 203.0.113.2 advertised-routes (to check what was sent)",
        ],
        "3. CIDR & Path Selection": [
            "🔹 Use `show bgp cidr-only` to view summarized routes.",
            "🔹 Use `show bgp paths` to examine available paths to a destination.",
            "🔹 Example:",
            "   1️⃣ Run: show bgp cidr-only (to check summarized routes)",
            "   2️⃣ Run: show bgp paths (to compare different AS path options for the same prefix)",
        ],
        "4. Troubleshooting Prefix Installation in RIB": [
            "🔹 If a route is not appearing in the routing table, check `show bgp rib-failure`.",
            "🔹 If a prefix is missing from BGP advertisements, check `show bgp pending-prefixes`.",
            "🔹 Example:",
            "   1️⃣ Run: show bgp ipv4 unicast (to confirm the route is present in BGP)",
            "   2️⃣ If missing from routing table, run: show bgp rib-failure",
            "   3️⃣ If pending for advertisement, run: show bgp pending-prefixes",
        ],
        "5. Optimizing BGP Updates & Policy Verification": [
            "🔹 Use `show bgp update-group` to understand how BGP updates are sent to neighbors.",
            "🔹 If an expected route is missing, ensure prefix lists and policies are correct.",
            "🔹 Example:",
            "   1️⃣ Run: show bgp update-group (to see how updates are grouped)",
            "   2️⃣ Verify prefix filtering with: show bgp prefix-list",
        ]
    }

    print("\n" + "=" * 80)
    print("📘 BGP Help: Understanding Command Relationships 📘".center(80))
    print("=" * 80)

    for section, lines in help_sections.items():
        print(f"\n🟢 {section}")
        for line in lines:
            print(f"   {line}")

    print("\n" + "=" * 80)
    print("🔍 Tip: Use 'X?' to see help for a specific command (e.g., '2?' for BGP Summary).")
    print("=" * 80)
