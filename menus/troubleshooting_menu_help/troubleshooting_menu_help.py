def troubleshooting_menu_help():
    """Provides an overview of the troubleshooting menu and its available options."""

    help_sections = {
        "Troubleshooting Menu Overview": [
            "🔹 **Device Information** - Displays system details, hardware inventory, and configuration settings.",
            "🔹 **Firepower Troubleshooting** - Diagnoses issues related to policies, FMC registration, and traffic flow.",
            "🔹 **Lina Troubleshooting** - Focuses on ASA-based troubleshooting for NAT, ACLs, and packet analysis.",
            "🔹 **Troubleshooting Menu Help** - Provides guidance on available troubleshooting tools and their use cases.",
            "🔹 Example:",
            "   1️⃣ Select `Device Information` to retrieve software version, hardware details, and configuration.",
            "   2️⃣ Choose `Firepower Troubleshooting` for deeper analysis of Firepower policy enforcement and connectivity.",
            "   3️⃣ Navigate to `Lina Troubleshooting` to inspect packet flow, NAT translations, and ACL behavior.",
        ],
    }

    print("\n" + "=" * 80)
    print("📘 Troubleshooting Menu Help 📘".center(80))
    print("=" * 80)

    for section, lines in help_sections.items():
        print(f"\n🟢 {section}")
        for line in lines:
            print(f"   {line}")

    print("\n" + "=" * 80)
    print("🔍 Tip: Use 'X?' to see help for a specific option (e.g., '2?' for Firepower Troubleshooting).")
    print("=" * 80)
