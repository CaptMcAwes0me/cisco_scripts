def snmp_help():
    """Displays SNMP troubleshooting steps, command relationships, troubleshooting techniques, and common caveats."""

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
        "6. Common SNMP Troubleshooting Commands": [
            "🔹 `debug snmp packet` - Displays real-time SNMP packet flow.",
            "🔹 `show snmp` - Shows basic SNMP configuration and status.",
            "🔹 `ping <snmp-server>` - Ensures reachability to the SNMP server.",
            "🔹 `telnet <snmp-server> 161` - Verifies SNMP UDP/161 is open.",
            "🔹 `capture <name> interface <intf> match ip host <src> host <dst>` - Checks if SNMP requests and responses are flowing.",
            "🔹 `clear snmp-server statistics` - Resets SNMP counters to help track fresh issues.",
        ],
        "7. SNMP Troubleshooting Techniques": [
            "🔹 **Confirm SNMP Access Lists** - Ensure no ACLs are blocking SNMP traffic.",
            "🔹 **Verify SNMP Community Strings** - If using SNMPv2, make sure the correct community string is used.",
            "🔹 **Check SNMPv3 Authentication** - Ensure correct authentication and encryption settings for users.",
            "🔹 **Monitor Polling Performance** - Use `show snmp-server statistics` to track response times.",
            "🔹 **Capture and Analyze SNMP Traffic** - Use packet captures to confirm if SNMP requests are reaching the device.",
            "🔹 **Use Debugging Cautiously** - `debug snmp packet` can be useful but may generate excessive output.",
        ],
        "8. Common SNMP Caveats": [
            "🔹 **SNMP Traps vs Polling** - Ensure the device is configured to send traps, not just respond to polling.",
            "🔹 **SNMPv3 Encryption Mismatches** - If SNMPv3 fails, check if authentication and encryption settings match.",
            "🔹 **Firewalls Blocking SNMP Traffic** - Ensure UDP/161 (SNMP queries) and UDP/162 (SNMP traps) are open.",
            "🔹 **Device CPU Load Issues** - Too many SNMP requests can overload the CPU; monitor using `show cpu detailed`.",
            "🔹 **SNMP Timers & Timeouts** - If polling delays occur, verify timeout settings on both the SNMP agent and manager.",
            "🔹 **OID Compatibility Issues** - Some SNMP managers may require specific OIDs to be enabled for proper polling.",
        ],
    }

    print("\n" + "=" * 80)
    print("📘 SNMP Help: Command Relationships, Troubleshooting, and Caveats 📘".center(80))
    print("=" * 80)

    for section, lines in help_sections.items():
        print(f"\n🟢 {section}")
        for line in lines:
            print(f"   {line}")

    print("\n" + "=" * 80)
    print("🔍 Tip: Use 'X?' to see help for a specific command (e.g., '6?' for SNMP Troubleshooting Commands).")
    print("=" * 80)
