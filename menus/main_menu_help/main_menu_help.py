def main_menu_help():
    """Provides an overview of the FP Troubleshooting Helper (FPTH) main menu and its available options."""

    help_sections = {
        "FPTH Menu Overview": [
            "🔹 **Troubleshooting Menu** - Accesses tools for diagnosing issues on Firepower and Lina.",
            "🔹 **Show Tech - Menu** - Gathers detailed system information and logs.",
            "🔹 **FPTH Menu Help** - Provides an overview of FPTH functionality and available options.",
            "🔹 Example:",
            "   1️⃣ Select `Troubleshooting Menu` to analyze Firepower configurations, traffic flow, and errors.",
            "   2️⃣ Choose `Show Tech - Menu` to generate system dumps for further diagnostics.",
            "   3️⃣ Use `FPTH Menu Help` to understand each section’s role and troubleshooting capabilities.",
        ],
    }

    print("\n" + "=" * 80)
    print("📘 FP Troubleshooting Helper (FPTH) Menu Help 📘".center(80))
    print("=" * 80)

    for section, lines in help_sections.items():
        print(f"\n🟢 {section}")
        for line in lines:
            print(f"   {line}")

    print("\n" + "=" * 80)
    print("🔍 Tip: Use 'X?' to see help for a specific option (e.g., '1?' for Troubleshooting Menu).")
    print("=" * 80)
