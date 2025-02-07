def vpn_menu_help():
    help_text = """
    === VPN Menu Help ===

    The VPN Menu provides options for troubleshooting and viewing VPN configurations, including 
    AnyConnect (Secure Client) and Site-to-Site VPNs.

    **Menu Options:**
    1) AnyConnect (Secure Client) Menu - View and troubleshoot remote access VPN settings, 
       including user sessions, authentication, and encryption details.
    2) Site-to-Site VPN Menu - Analyze configurations and status of IPsec tunnels, peer connections, 
       and encryption policies.

    **How to Use the Menu:**
    - Enter the corresponding number to access VPN details.
    - Review active sessions, tunnel states, and authentication settings.

    **Additional Notes:**
    - Ensure VPN configurations match expected settings to prevent connectivity issues.
    - Check for certificate validity, encryption mismatches, and authentication failures.
    - Use `show crypto ikev2 sa`, `show vpn-sessiondb`, and other related commands for further analysis.

    ============================================
    """
    print(help_text)
