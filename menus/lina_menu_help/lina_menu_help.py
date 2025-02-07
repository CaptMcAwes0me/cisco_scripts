def lina_menu_help():
    help_text = """
    === Lina Troubleshooting Help ===

    The Lina Menu provides network and system troubleshooting tools for devices running the Lina process.

    **Menu Options:**
    1) Device Information - Retrieve details about system software, hardware, and uptime.
    2) NAT (Network Address Translation) - View and troubleshoot NAT policies and translations.
    3) Connectivity and Traffic - Check ARP, active connections, and network traffic statistics.
    4) Routing - Analyze routing configurations including OSPF, BGP, EIGRP, and VRFs.
    5) VPN - Inspect VPN status, tunnels, and encryption parameters.
    6) High Availability (HA) / Failover - Check failover state, redundancy, and synchronization settings.
    7) Logging and Monitoring - View system logs and monitor security events.
    8) Clustering - Diagnose cluster-related issues, including resource usage and configuration.
    9) Blocks - Monitor and troubleshoot system memory block allocation and exhaustion.
    0) Exit - Return to the previous menu.

    **Troubleshooting Notes:**
    - Use Device Information to get an overview before deeper troubleshooting.
    - Connectivity and Traffic help diagnose network-level issues.
    - Routing and VPN sections provide insight into configuration and operational issues.
    - HA/Failover ensures high availability and redundancy functionality.
    - Logging and Monitoring assist in security event tracking and system behavior analysis.

    ============================================
    """
    print(help_text)

