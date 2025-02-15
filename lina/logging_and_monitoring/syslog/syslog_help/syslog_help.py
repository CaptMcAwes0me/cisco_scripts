def syslog_help():
    """Displays Syslog troubleshooting steps, command relationships, troubleshooting techniques, and common caveats."""

    help_sections = {
        "1. Verifying Syslog Configuration": [
            "🔹 Use `show running-config all logging` to check **Syslog settings, logging levels, and destinations**.",
            "🔹 If Syslog messages are missing, ensure **logging is enabled** and the correct **logging level** is set.",
            "🔹 Example:",
            "   1️⃣ Run: show running-config all logging (Verify Syslog settings)",
            "   2️⃣ Run: show logging queue (Check if messages are being queued properly)",
        ],
        "2. Checking Syslog Message Delivery": [
            "🔹 Use `show logging message` to verify if a **specific message ID** is configured for logging.",
            "🔹 If certain logs are missing, ensure they are **not being filtered** out using 'no logging message <ID>'.",
            "🔹 Example:",
            "   1️⃣ Run: show logging message (Confirm logging settings for specific messages)",
            "   2️⃣ Run: show logging buffered output (Check if logs are recorded in the buffer)",
        ],
        "3. Troubleshooting Syslog Queues": [
            "🔹 Use `show logging queue` to check if Syslog messages are being **dropped or delayed**.",
            "🔹 If the queue is too large, consider **increasing the queue size** or **reducing logging verbosity**.",
            "🔹 Example:",
            "   1️⃣ Run: show logging queue (Check message backlog and queue size)",
            "   2️⃣ If queue is full, adjust: show running-config all logging (Modify logging settings)",
        ],
        "4. Monitoring Syslog Manager & Dynamic Rate Limits": [
            "🔹 Use `show logging manager detail` to view the **current Syslog manager settings**.",
            "🔹 Use `show logging dynamic-rate-limit` to confirm whether **rate limiting is affecting logs**.",
            "🔹 Example:",
            "   1️⃣ Run: show logging manager detail (Check Syslog manager status)",
            "   2️⃣ Run: show logging dynamic-rate-limit (Verify if logs are being throttled)",
        ],
        "5. Checking Unified Syslog Clients": [
            "🔹 Use `show logging unified-client` to verify **which processes are registered to receive logs**.",
            "🔹 Use `show logging unified-client statistics` to check for **registration failures or message drops**.",
            "🔹 Example:",
            "   1️⃣ Run: show logging unified-client (Confirm which clients are receiving logs)",
            "   2️⃣ Run: show logging unified-client statistics (Check for errors in Syslog client registration)",
        ],
        "6. Reviewing Buffered & External Logging": [
            "🔹 Use `show log` to check logs stored in the **buffer**.",
            "🔹 If logs are not appearing externally, check **destination IPs** using `show running-config all logging`.",
            "🔹 Example:",
            "   1️⃣ Run: show log (Review locally buffered logs)",
            "   2️⃣ Run: show running-config all logging (Ensure external log destinations are correct)",
        ],
        "7. Common Syslog Troubleshooting Commands": [
            "🔹 `debug logging` - View real-time logging debug output.",
            "🔹 `ping <syslog-server>` - Ensure connectivity to remote Syslog servers.",
            "🔹 `ping tcp <syslog-server> 514` (if TCP) - Check if Syslog port is reachable from the device.",
            "🔹 `capture <name> interface <intf> match ip host <src> host <dst>` - Verify if Syslog messages are sent to the correct destination.",
        ],
        "8. Syslog Troubleshooting Techniques": [
            "🔹 **Confirm Syslog Levels** - Ensure logging level is set high enough to capture relevant messages.",
            "🔹 **Check for Message Filtering** - Some messages might be explicitly disabled using 'no logging message <ID>'.",
            "🔹 **Verify Connectivity to Remote Syslog Servers** - Use `ping` to confirm L3 reachability.",
            "🔹 **Check If Messages Are Being Dropped** - Use `show logging queue` to see if messages are stuck.",
            "🔹 **Use Packet Captures** - If logs are missing, verify Syslog packets are leaving the device.",
        ],
        "9. Common Syslog Caveats": [
            "🔹 **Syslog Rate Limiting** - Too many logs can trigger rate-limiting. Check `show logging dynamic-rate-limit`.",
            "🔹 **Buffer Overflows** - If logging buffer is too small, old logs may be lost. Increase the buffer if necessary.",
            "🔹 **UDP vs TCP Logging** - UDP-based Syslog can lose messages during network congestion; consider using TCP logging.",
            "🔹 **TCP Logging** - Ensure 'logging permit-hostdown' is enabled to prevent TCP connections from being dropped.",
            "🔹 **Time Synchronization Issues** - Ensure the device has accurate NTP settings to prevent timestamp mismatches.",
            "🔹 **Firewall Blocking Syslog Traffic** - If logs are missing, ensure no ACLs are blocking UDP/514 traffic.",
            "🔹 **Syslog Message Parsing Issues** - If logs appear scrambled, verify encoding and ensure the Syslog server is properly configured.",
        ],
    }

    print("\n" + "=" * 80)
    print("📘 Syslog Help: Command Relationships, Troubleshooting, and Caveats 📘".center(80))
    print("=" * 80)

    for section, lines in help_sections.items():
        print(f"\n🟢 {section}")
        for line in lines:
            print(f"   {line}")

    print("\n" + "=" * 80)
    print("🔍 Tip: Use 'X?' to see help for a specific command (e.g., '7?' for Syslog Troubleshooting Commands).")
    print("=" * 80)
