def isis_help():
    """Displays how different ISIS commands relate to each other with practical examples."""

    help_sections = {
        "1. Verifying ISIS Configuration & Process": [
            "🔹 Use `show running-config all router isis` to verify ISIS process settings, NETs, and interfaces.",
            "🔹 Use `show isis topology` to get an overview of ISIS network structure and adjacencies.",
            "🔹 Example:",
            "   1️⃣ Run: show running-config all router isis (Confirm NETs, levels, and interface settings)",
            "   2️⃣ Run: show isis topology (Verify ISIS neighbors, levels, and metric paths)",
        ],
        "2. Checking ISIS Neighbor Adjacencies": [
            "🔹 Use `show isis neighbors` to check if ISIS neighbors have formed adjacencies.",
            "🔹 If an expected neighbor is missing, check interface status using `show isis topology`.",
            "🔹 Example:",
            "   1️⃣ Run: show isis neighbors (Confirm if neighbors are UP or stuck in INIT/DOWN)",
            "   2️⃣ If neighbors are missing, check: show isis topology (Verify ISIS links and interfaces)",
            "   3️⃣ If adjacencies fail, check: show running-config all router isis (Confirm level and authentication)",
        ],
        "3. Investigating ISIS Route Installation": [
            "🔹 Use `show isis rib` to see which ISIS routes are installed in the routing table.",
            "🔹 If an expected route is missing, check `show isis database` to confirm if LSPs exist.",
            "🔹 Example:",
            "   1️⃣ Run: show isis rib (Ensure expected routes are installed in the RIB)",
            "   2️⃣ If a route is missing, check: show isis database (Verify LSP presence and sequence numbers)",
            "   3️⃣ If an LSP exists but isn’t in the RIB, check: show isis spf-log (Look for SPF calculation issues)",
        ],
        "4. Diagnosing ISIS Database Issues": [
            "🔹 Use `show isis database` to review ISIS LSPs, including sequence numbers and hold times.",
            "🔹 Use `show isis lsp-log` to check if LSPs are being frequently updated or purged.",
            "🔹 Example:",
            "   1️⃣ Run: show isis database (Confirm LSPs are present and valid)",
            "   2️⃣ Run: show isis lsp-log (Check for frequent LSP flooding or stale LSPs)",
        ],
        "5. Monitoring ISIS SPF & Convergence": [
            "🔹 Use `show isis spf-log` to review SPF calculations and changes in the network topology.",
            "🔹 Use `show isis traffic` (if applicable) to analyze ISIS message exchange counts.",
            "🔹 Example:",
            "   1️⃣ Run: show isis spf-log (Check for excessive SPF recalculations)",
            "   2️⃣ If SPF recalculations are frequent, check: show isis lsp-log (Look for frequent LSP updates)",
        ],
        "6. Mapping System IDs to Hostnames": [
            "🔹 Use `show isis hostname` to map ISIS system IDs to human-readable hostnames.",
            "🔹 Example:",
            "   1️⃣ Run: show isis hostname (Resolve system IDs to router names for better readability)",
        ],
    }

    print("\n" + "=" * 80)
    print("📘 ISIS Help: Understanding Command Relationships 📘".center(80))
    print("=" * 80)

    for section, lines in help_sections.items():
        print(f"\n🟢 {section}")
        for line in lines:
            print(f"   {line}")

    print("\n" + "=" * 80)
    print("🔍 Tip: Use 'X?' to see help for a specific command (e.g., '4?' for ISIS Database).")
    print("=" * 80)
