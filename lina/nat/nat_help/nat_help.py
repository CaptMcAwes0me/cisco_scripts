def nat_help():
    """Displays how different NAT commands relate to each other with practical examples."""

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
            "🔹 Use `show nat proxy-arp` to determine if the ASA is responding to ARP requests for NAT addresses.",
            "🔹 Example:",
            "   1️⃣ Run: show nat proxy-arp (Check Proxy ARP behavior for NAT mappings)",
            "   2️⃣ If issues arise, verify NAT rule configurations and routing settings.",
        ],
    }

    print("\n" + "=" * 80)
    print("📘 NAT Help: Understanding Command Relationships 📘".center(80))
    print("=" * 80)

    for section, lines in help_sections.items():
        print(f"\n🟢 {section}")
        for line in lines:
            print(f"   {line}")

    print("\n" + "=" * 80)
    print("🔍 Tip: Use 'X?' to see help for a specific command (e.g., '2?' for Show NAT Detail).")
    print("=" * 80)
