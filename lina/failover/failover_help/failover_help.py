def failover_help():
    """Displays how different failover commands relate to each other with practical examples."""

    help_sections = {
        "1. Viewing Failover Configuration & Status": [
            "🔹 Use `show failover` to verify the overall failover state and role of each unit.",
            "🔹 Use `show failover running-config` to display the currently configured failover settings.",
            "🔹 Example:",
            "   1️⃣ Run: show failover (Check Active/Standby status, link state, and sync status)",
            "   2️⃣ Run: show run all failover (Verify failover-related configuration)",
        ],
        "2. Checking Failover Synchronization": [
            "🔹 Use `show failover config-sync status` to confirm if configuration sync is successful.",
            "🔹 If a sync issue is detected, check `show failover app-sync stats` for application sync details.",
            "🔹 Example:",
            "   1️⃣ Run: show failover config-sync status (Ensure successful config sync)",
            "   2️⃣ If issues exist, run: show failover app-sync stats (View application sync failures)",
        ],
        "3. Troubleshooting Failover State & Link Issues": [
            "🔹 Use `show failover state` to examine the role of each device and recent failure reasons.",
            "🔹 If failover communication is failing, check `show failover interface` for interface status.",
            "🔹 Example:",
            "   1️⃣ Run: show failover state (Verify active/standby roles and failure history)",
            "   2️⃣ Run: show failover interface (Ensure failover interfaces are up and passing traffic)",
        ],
        "4. Analyzing Failover Failures & Communication": [
            "🔹 Use `show failover details` to get a breakdown of failover link communication and timers.",
            "🔹 If the secondary device is not taking over, check `show failover descriptor` for role info.",
            "🔹 Example:",
            "   1️⃣ Run: show failover details (Examine detailed failover statistics and communication status)",
            "   2️⃣ Run: show failover descriptor (Check if failover role assignment is correct)",
        ],
        "5. Monitoring Failover Performance": [
            "🔹 Use `show failover app-sync stats` to verify synchronization rates for applications.",
            "🔹 Use `show failover config-sync status` to ensure config sync is working correctly.",
            "🔹 Example:",
            "   1️⃣ Run: show failover app-sync stats (Ensure application state sync is healthy)",
            "   2️⃣ Run: show failover config-sync status (Verify config sync with peer device)",
        ],
    }

    print("\n" + "=" * 80)
    print("📘 Failover Help: Understanding Command Relationships 📘".center(80))
    print("=" * 80)

    for section, lines in help_sections.items():
        print(f"\n🟢 {section}")
        for line in lines:
            print(f"   {line}")

    print("\n" + "=" * 80)
    print("🔍 Tip: Use 'X?' to see help for a specific command (e.g., '4?' for Failover Details).")
    print("=" * 80)
