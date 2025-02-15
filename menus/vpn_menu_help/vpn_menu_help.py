def vpn_menu_help():
    """Displays detailed help information for VPN-related configurations and commands."""

    help_sections = {
        "1. Understanding VPN Types": [
            "🔹 **AnyConnect (Secure Client VPN)** - Provides remote access VPN functionality for individual users.",
            "🔹 **Site-to-Site (S2S) VPN** - Connects entire networks securely over an encrypted tunnel.",
            "🔹 **IPSec VPN** - Uses IKEv1 or IKEv2 for secure encrypted communication.",
            "🔹 **SSL VPN** - Uses Secure Sockets Layer (SSL) for encrypted web-based VPN access.",
        ],
        "2. Managing AnyConnect VPN": [
            "🔹 Use `show running-config tunnel-group | include type remote-access` to list AnyConnect tunnel groups.",
            "🔹 Use `show vpn-sessiondb anyconnect` to view active AnyConnect sessions.",
            "🔹 Example:",
            "   1️⃣ Run: `show running-config tunnel-group <group_name>` (View AnyConnect tunnel-group settings)",
            "   2️⃣ Run: `show running-config group-policy <policy_name>` (Verify group policy details)",
            "   3️⃣ Run: `show running-config webvpn` (Check SSL VPN configuration settings)",
        ],
        "3. Managing Site-to-Site VPN": [
            "🔹 Use `show running-config tunnel-group | include type ipsec-l2l` to list all Site-to-Site VPN tunnels.",
            "🔹 Use `show crypto ipsec sa` to check IPSec security associations.",
            "🔹 Example:",
            "   1️⃣ Run: `show crypto ikev1 sa` (View active IKEv1 SAs)",
            "   2️⃣ Run: `show crypto ikev2 sa` (View active IKEv2 SAs)",
            "   3️⃣ Run: `show crypto ipsec sa` (Check active IPSec tunnels)",
        ],
        "4. Checking VPN Connection Status": [
            "🔹 Use `show vpn-sessiondb` to view all VPN sessions (AnyConnect, S2S, etc.).",
            "🔹 Use `show crypto session` to display detailed VPN session information.",
            "🔹 Example:",
            "   1️⃣ Run: `show vpn-sessiondb summary` (Get VPN session summary)",
            "   2️⃣ Run: `show crypto session detail` (Detailed crypto session information)",
        ],
        "5. Troubleshooting VPN Issues": [
            "🔹 Use `debug crypto ikev1 10` or `debug crypto ikev2 10` for VPN tunnel establishment issues.",
            "🔹 Use `debug webvpn` for SSL VPN troubleshooting.",
            "🔹 Example:",
            "   1️⃣ Run: `debug crypto ikev1 10` (Check IKEv1 negotiation details)",
            "   2️⃣ Run: `show logging` (Review logs for VPN errors)",
            "   3️⃣ Run: `show asp drop` (Check if VPN traffic is being dropped by the firewall)",
        ],
    }

    print("\n" + "=" * 80)
    print("📘 VPN Help: Understanding VPN Configuration & Troubleshooting 📘".center(80))
    print("=" * 80)

    for section, lines in help_sections.items():
        print(f"\n🟢 {section}")
        for line in lines:
            print(f"   {line}")

    print("\n" + "=" * 80)
    print("🔍 Tip: Use 'X?' to see help for a specific VPN function (e.g., '3?' for Site-to-Site VPN).")
    print("=" * 80)
