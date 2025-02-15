def failover_help():
    """Displays failover troubleshooting steps, command relationships, troubleshooting techniques, and common caveats."""

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
        "6. Common Failover Troubleshooting Commands": [
            "🔹 `debug fover <option>` - View real-time failover event logs and messages.",
            "🔹 `show failover history` - Displays past failover events and reasons.",
            "🔹 `show interface <failover-link>` - Ensures the failover interface is operational.",
            "🔹 `ping <peer-ip>` - Verifies that the standby unit is reachable via the failover link.",
        ],
        "7. Failover Troubleshooting Techniques": [
            "🔹 **Check Failover Interface Status** - Ensure failover links are up using `show failover interface`.",
            "🔹 **Monitor Failover Health** - Use `show failover` and `show failover details` for sync and health status.",
            "🔹 **Review Past Failovers** - Use `show failover history` to analyze previous failover events.",
            "🔹 **Test Manual Failover** - Run `failover active` on the standby unit to verify failover behavior.",
            "🔹 **Check Licensing and Feature Mismatch** - Ensure both units have identical licenses and feature sets.",
        ],
        "8. Common Failover Caveats": [
            "🔹 **Failover Interface Must Be Reachable** - If the failover interface is down, failover will not occur.",
            "🔹 **Configuration Sync Issues** - If changes aren’t syncing, use `debug fover sync`.",
            "🔹 **IP/MAC Address Spoofing** - The active/standby MAC address and IP address 'float' between units.",
            "🔹 **Software & Hardware Mismatches** - Both devices must have the same software and hardware capabilities.",
            "🔹 **Failover Communication Protocol** - Failover uses IP Protocol 105 for communication between units.",
        ],
    }

    print("\n" + "=" * 80)
    print("📘 Failover Help: Command Relationships, Troubleshooting, and Caveats 📘".center(80))
    print("=" * 80)

    for section, lines in help_sections.items():
        print(f"\n🟢 {section}")
        for line in lines:
            print(f"   {line}")

    print("\n" + "=" * 80)
    print("🔍 Tip: Use 'X?' to see help for a specific command (e.g., '6?' for Failover Troubleshooting Commands).")
    print("=" * 80)
