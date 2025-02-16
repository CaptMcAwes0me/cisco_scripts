def nat_help():
    """Displays how different NAT commands relate to each other with practical examples,
       troubleshooting techniques, and common NAT caveats."""

    help_sections = {
        "1. Viewing NAT Configuration": [
            "🔹 Use `show running-config all nat` to verify all NAT rules, including object NAT and manual NAT.",
            "🔹 Use `show nat detail` to see detailed NAT rules and their translation hit counts.",
            "🔹 Example:",
            "   1️⃣ Run: show running-config all nat (Check NAT configuration)",
            "   2️⃣ Run: show nat detail (Confirm NAT rules and hit statistics)",
        ],
        "2. Checking NAT Translations (XLATE)": [
            "🔹 Use `show xlate count` to check the total number of active NAT translations.",
            "🔹 Use `show xlate detail` to inspect individual NAT translations, including source/destination addresses and idle time.",
            "🔹 Example:",
            "   1️⃣ Run: show xlate count (See total number of active NAT translations)",
            "   2️⃣ Run: show xlate detail (Review detailed NAT translations for troubleshooting)",
        ],
        "3. Monitoring NAT Pools": [
            "🔹 Use `show nat pool` to see NAT pools, including available and allocated addresses.",
            "🔹 This is useful for determining whether NAT exhaustion is occurring.",
            "🔹 Example:",
            "   1️⃣ Run: show nat pool (Check NAT pool availability and utilization)",
        ],
        "4. Verifying Proxy ARP": [
            "🔹 Use `show nat proxy-arp` to determine if the FTD is responding to ARP requests for NAT addresses.",
            "🔹 Example:",
            "   1️⃣ Run: show nat proxy-arp (Check Proxy ARP behavior for NAT mappings)",
            "   2️⃣ If issues arise, verify NAT rule configurations and routing settings.",
        ],
        "5. Common NAT Troubleshooting Commands": [
            "🔹 `show conn` - Verify active connections and NAT translations.",
            "🔹 `debug nat` - View real-time NAT debugging output.",
            "🔹 `capture <name> interface <intf> match ip host <src> host <dst>` - Verify if traffic is hitting NAT rules.",
            "🔹 `packet-tracer input <intf> <protocol> <src> <dst> <port>` - Simulate traffic through NAT to identify translation behavior.",
            "🔹 `clear xlate` - Reset NAT translations (use with caution in production environments).",
        ],
        "6. NAT Troubleshooting Techniques": [
            "🔹 **Confirm NAT Rule Order** - Use `show nat detail` to check if rules are in the correct sequence (Auto NAT before Manual NAT).",
            "🔹 **Check if NAT is being applied** - Run `packet-tracer` and inspect NAT sections.",
            "🔹 **Monitor Connection State** - Use `show conn` to ensure translations are properly maintained.",
            "🔹 **Check Routing Issues** - Ensure correct next-hop routing for NAT-translated addresses.",
            "🔹 **Use Debugging Carefully** - `debug nat` can help but may be resource-intensive.",
        ],
        "7. Common NAT Caveats": [
            "🔹 **Twice NAT vs Auto NAT** - Manual NAT (Twice NAT) takes precedence over Auto NAT.",
            "🔹 **Overlapping NAT Rules** - Ensure specific NAT rules are above general ones to avoid incorrect translations.",
            "🔹 **Proxy ARP Issues** - If Proxy ARP is disabled, static NAT mappings may not work unless proper routing is in place.",
            "🔹 **NAT Exemption Conflicts** - Ensure traffic that shouldn't be NATed is explicitly exempted (`no nat-control`).",
            "🔹 **Asymmetric NAT** - If return traffic isn't NATed properly, check for missing rules on inbound interfaces.",
        ],
    }

    print("\n" + "=" * 80)
    print("📘 NAT Help: Understanding Command Relationships, Troubleshooting, and Caveats 📘".center(80))
    print("=" * 80)

    for section, lines in help_sections.items():
        print(f"\n🟢 {section}")
        for line in lines:
            print(f"   {line}")

    print("\n" + "=" * 80)
    print("🔍 Tip: Use 'X?' to see help for a specific command (e.g., '5?' for Common NAT Troubleshooting Commands).")
    print("=" * 80)
