def anyconnect_help():
    """Displays how different AnyConnect commands relate to each other with practical examples."""

    help_sections = {
        "1. Verifying AnyConnect Configuration & Tunnel Groups": [
            "🔹 Use `show running-config all tunnel-group <group>` to check the full configuration of an AnyConnect tunnel-group.",
            "🔹 Use `show running-config all group-policy <policy>` to verify group policy settings.",
            "🔹 Example:",
            "   1️⃣ Run: show running-config all tunnel-group <group> (Confirm authentication, address pools, and policies).",
            "   2️⃣ Run: show running-config all group-policy <policy> (Check split tunneling, ACLs, and DNS settings).",
        ],
        "2. Checking AnyConnect Session Details": [
            "🔹 Use `show vpn-sessiondb anyconnect` to view active AnyConnect sessions.",
            "🔹 Use `show vpn-sessiondb anyconnect filter tunnel-group <group>` to narrow results to a specific tunnel-group.",
            "🔹 Example:",
            "   1️⃣ Run: show vpn-sessiondb anyconnect (Check active sessions, assigned IPs, and session time).",
            "   2️⃣ If filtering by group, run: show vpn-sessiondb anyconnect filter tunnel-group <group>.",
        ],
        "3. Analyzing SSL & DTLS Data": [
            "🔹 Use `show ssl information` to check SSL settings, session details, and supported cipher suites.",
            "🔹 Use `show ssl errors` to see any SSL-related errors affecting connectivity.",
            "🔹 Example:",
            "   1️⃣ Run: show ssl information (Verify SSL version, session details, and ciphers in use).",
            "   2️⃣ Run: show ssl errors (Look for handshake failures, invalid certificates, or cipher mismatches).",
        ],
        "4. Investigating Crypto & Certificate Issues": [
            "🔹 Use `show crypto ca trustpoint` to list configured trustpoints for certificate-based authentication.",
            "🔹 Use `show crypto ca certificates` to view installed certificates and their validity.",
            "🔹 Use `show crypto ca crls` to check for revoked certificates.",
            "🔹 Example:",
            "   1️⃣ Run: show crypto ca trustpoint (Confirm which trustpoints are in use).",
            "   2️⃣ Run: show crypto ca certificates (Ensure certificates are valid and not expired).",
            "   3️⃣ Run: show crypto ca crls (Check for any revoked certificates that might block access).",
        ],
        "5. Debugging AnyConnect Performance & Crypto Acceleration": [
            "🔹 Use `show crypto accelerator status` to confirm if hardware crypto acceleration is enabled.",
            "🔹 Use `show crypto accelerator statistics` to analyze encryption/decryption performance.",
            "🔹 Example:",
            "   1️⃣ Run: show crypto accelerator status (Ensure hardware offload is functioning).",
            "   2️⃣ Run: show crypto accelerator statistics (Check for excessive CPU load on encrypted sessions).",
        ],
        "6. Monitoring System-Wide VPN Usage": [
            "🔹 Use `show running-config ip local pool` to see assigned AnyConnect IP address pools.",
            "🔹 Use `show running-config all sysopt | include vpn` to check VPN-specific system optimizations.",
            "🔹 Example:",
            "   1️⃣ Run: show running-config ip local pool (Confirm IP pool size and available addresses).",
            "   2️⃣ Run: show running-config all sysopt | include vpn (Check VPN optimization settings).",
        ],
    }

    print("\n" + "=" * 80)
    print("📘 AnyConnect Help: Understanding Command Relationships 📘".center(80))
    print("=" * 80)

    for section, lines in help_sections.items():
        print(f"\n🟢 {section}")
        for line in lines:
            print(f"   {line}")

    print("\n" + "=" * 80)
    print("🔍 Tip: Use 'X?' to see help for a specific command (e.g., '3?' for SSL Data).")
    print("=" * 80)
