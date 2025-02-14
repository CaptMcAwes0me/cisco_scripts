def snmp_help():
    """Displays SNMP troubleshooting steps and command relationships."""

    help_sections = {
        "1. Verifying SNMP Configuration": [
            "🔹 Use `show run all snmp-server` to confirm SNMP settings, communities, users, and traps.",
            "🔹 If SNMP is not responding, check for interface restrictions or ACLs blocking SNMP queries.",
            "🔹 Example:",
            "   1️⃣ Run: show run all snmp-server (Ensure SNMP is configured correctly)",
            "   2️⃣ If issues persist, check: show snmp-server statistics (Look for SNMP errors)",
        ],
        "2. Checking SNMP Engine ID": [
            "🔹 Use `show snmp-server engineID` to verify the SNMPv3 Engine ID.",
            "🔹 If SNMPv3 authentication fails, ensure the **Engine ID matches** between manager and agent.",
            "🔹 Example:",
            "   1️⃣ Run: show snmp-server engineID (Confirm Engine ID for SNMPv3)",
            "   2️⃣ If mismatched, reconfigure: show run all snmp-server",
        ],
        "3. Managing SNMP Groups & Users": [
            "🔹 Use `show snmp-server group` to verify **SNMP access levels** for different groups.",
            "🔹 Use `show snmp-server user` to confirm **SNMPv3 user authentication and encryption settings**.",
            "🔹 Example:",
            "   1️⃣ Run: show snmp-server group (Check assigned SNMP privileges)",
            "   2️⃣ Run: show snmp-server user (Verify SNMPv3 authentication/encryption settings)",
        ],
        "4. Checking SNMP Hosts & Trap Destinations": [
            "🔹 Use `show snmp-server host` to list configured SNMP servers and trap destinations.",
            "🔹 If SNMP traps are not received, verify SNMP **traps are enabled** and UDP/161 traffic is allowed.",
            "🔹 Example:",
            "   1️⃣ Run: show snmp-server host (Confirm SNMP server IPs)",
            "   2️⃣ If traps are missing, check: show logging (Ensure logging is enabled for SNMP events)",
        ],
        "5. Monitoring SNMP Statistics": [
            "🔹 Use `show snmp-server statistics` to check SNMP request failures, timeouts, and errors.",
            "🔹 If SNMP polling is slow, look for **high request failures** or SNMP process issues.",
            "🔹 Example:",
            "   1️⃣ Run: show snmp-server statistics (Analyze SNMP request counts & errors)",
            "   2️⃣ If failures are high, check: show cpu detailed (Ensure CPU isn't overloaded)",
        ],
    }

    print("\n" + "=" * 80)
    print("📘 SNMP Help: Understanding Command Relationships 📘".center(80))
    print("=" * 80)

    for section, lines in help_sections.items():
        print(f"\n🟢 {section}")
        for line in lines:
            print(f"   {line}")

    print("\n" + "=" * 80)
    print("🔍 Tip: Use 'X?' to see help for a specific command (e.g., '3?' for SNMP Group).")
    print("=" * 80)
