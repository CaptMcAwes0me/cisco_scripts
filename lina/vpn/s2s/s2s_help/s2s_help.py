def s2s_help():
    """Provides guidance on Site-to-Site VPN commands and their practical applications."""

    help_sections = {
        "1. Verifying Site-to-Site VPN Configuration": [
            "🔹 Use `show run crypto map` to display the crypto map configurations, including peer IPs and access lists.",
            "🔹 Use `show run tunnel-group` to view tunnel group configurations, including authentication methods.",
            "🔹 Example:",
            "   1️⃣ Run: show run crypto map",
            "      - Confirm the correct peer IP addresses and access lists are applied.",
            "   2️⃣ Run: show run tunnel-group",
            "      - Verify the tunnel group settings, such as IPsec attributes and pre-shared keys.",
        ],
        "2. Monitoring VPN Tunnel Status": [
            "🔹 Use `show vpn-sessiondb l2l` to view active LAN-to-LAN VPN sessions.",
            "🔹 Use `show crypto isakmp sa` to check the status of IKE Phase 1 Security Associations.",
            "🔹 Use `show crypto ipsec sa` to examine the status of IPsec Phase 2 Security Associations.",
            "🔹 Example:",
            "   1️⃣ Run: show vpn-sessiondb l2l",
            "      - Confirm the presence of active VPN sessions and their details.",
            "   2️⃣ Run: show crypto isakmp sa",
            "      - Check for 'MM_ACTIVE' state indicating successful Phase 1 negotiation.",
            "   3️⃣ Run: show crypto ipsec sa",
            "      - Verify the encryption and decryption statistics for the IPsec tunnel.",
        ],
        "3. Troubleshooting VPN Connectivity Issues": [
            "🔹 Use `debug crypto isakmp 7` to enable detailed debugging for IKE Phase 1.",
            "🔹 Use `debug crypto ipsec 7` to enable detailed debugging for IPsec Phase 2.",
            "🔹 Use `show logging` to review system logs for VPN-related messages.",
            "🔹 Example:",
            "   1️⃣ Enable debugging:",
            "      - debug crypto isakmp 7",
            "      - debug crypto ipsec 7",
            "   2️⃣ Initiate traffic to bring up the VPN tunnel.",
            "   3️⃣ Run: show logging",
            "      - Analyze logs for errors or messages indicating negotiation failures.",
            "   4️⃣ Disable debugging after analysis:",
            "      - no debug all",
        ],
        "4. Validating VPN Traffic Flow": [
            "🔹 Use `packet-tracer input [interface] [protocol] [source IP] [destination IP]` to simulate traffic and identify at which stage it might be failing.",
            "🔹 Example:",
            "   1️⃣ Run: packet-tracer input inside tcp 192.168.1.10 80 192.168.2.10 80",
            "      - Simulate a TCP connection from the inside network to a remote host through the VPN.",
            "      - Analyze the output to determine if the packet is correctly encrypted and forwarded.",
        ],
        "5. Reviewing VPN Configuration Details": [
            "🔹 Use `more system:running-config` to view the complete running configuration, including encrypted keys.",
            "🔹 Example:",
            "   1️⃣ Run: more system:running-config",
            "      - Review the full configuration for any discrepancies or misconfigurations.",
            "      - Pay special attention to crypto maps, tunnel groups, and NAT settings.",
        ],
    }

    print("\n" + "=" * 80)
    print("📘 Site-to-Site VPN Help: Command Usage and Practical Examples 📘".center(80))
    print("=" * 80)

    for section, lines in help_sections.items():
        print(f"\n🟢 {section}")
        for line in lines:
            print(f"   {line}")

    print("\n" + "=" * 80)
    print("🔍 Tip: Use 'X?' to see help for a specific command (e.g., '2?' for Monitoring VPN Tunnel Status).")
    print("=" * 80)
