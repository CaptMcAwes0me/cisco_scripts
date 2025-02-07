def routing_help():
    help_text = """
    === Routing Menu Help ===

    The Routing Menu provides options for troubleshooting and viewing routing information on the system. 
    It includes different routing protocols and global routing details.

    **Menu Options:**
    1) Global Routing - View and troubleshoot system-wide routing settings.
    2) EIGRP - Check EIGRP (Enhanced Interior Gateway Routing Protocol) configuration and neighbor relationships.
    3) OSPF - View OSPF (Open Shortest Path First) routing details, including neighbors and database information.
    4) BGP - Display BGP (Border Gateway Protocol) settings, peer relationships, and advertised routes.
    5) ISIS - Analyze ISIS (Intermediate System to Intermediate System) routing details.
    6) VRF - View Virtual Routing and Forwarding (VRF) configurations.

    **How to Use the Menu:**
    - Enter the corresponding number to access routing details for a specific protocol.
    - Review routing tables and protocol-specific information for troubleshooting.
    - Use 'q' or 'exit' to leave the menu.

    **Additional Notes:**
    - Understanding routing protocols helps identify connectivity issues.
    - Use protocol-specific commands (e.g., 'show route', 'show eigrp neighbors') for deeper insights.
    - Ensure proper neighbor relationships and route advertisements are in place.

    ============================================
    """
    print(help_text)
