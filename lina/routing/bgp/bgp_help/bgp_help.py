def bgp_help():
    help_text = """
    Lina "BGP" Commands Help
    =======================

    1. **show running-config all router bgp**  
       - Displays the complete running configuration for BGP (Border Gateway Protocol).  
       - Useful for reviewing the full BGP configuration, including router BGP settings, neighbor relationships, and network advertisements.

    2. **show bgp summary**  
       - Displays a summary of BGP status and statistics.  
       - Provides an overview of the BGP process, showing the number of established neighbors, the number of prefixes learned, and other essential BGP performance indicators.

    3. **show bgp neighbors**  
       - Displays information about BGP neighbors.  
       - Shows details of BGP peering, including the status of connections, AS numbers, and the number of routes learned from each neighbor.

    4. **show bgp ipv4 unicast**  
       - Displays the BGP IPv4 Unicast routing table.  
       - Provides information about IPv4 routes advertised by the BGP process, useful for verifying which routes are being exchanged with peers.

    5. **show bgp cidr-only**  
       - Displays only CIDR-formatted (Classless Inter-Domain Routing) prefixes.  
       - Helps isolate the CIDR blocks in the BGP routing table for easier analysis of IP address usage.

    6. **show bgp paths**  
       - Displays the paths that BGP has learned.  
       - Shows the available BGP paths, including route attributes like AS path, next hop, and local preference, helping to analyze route selection.

    7. **show bgp pending-prefixes**  
       - Displays the list of prefixes that are pending BGP update.  
       - Helps track prefixes that are in the process of being advertised or withdrawn by BGP, useful for monitoring BGP convergence.

    8. **show bgp rib-failure**  
       - Displays information about BGP route installation failures.  
       - Provides details on why certain routes could not be installed into the BGP Routing Information Base (RIB), which can assist in troubleshooting BGP route issues.

    9. **show bgp neighbor <neighbor> advertised-routes**  
       - Displays the routes advertised by a specific BGP neighbor.  
       - Useful for verifying which routes a particular neighbor is advertising to your system and checking for routing inconsistencies or issues.

    10. **show bgp update-group**  
        - Displays information about BGP update groups.  
        - Shows details regarding how BGP update messages are grouped and exchanged, helping in understanding the performance and behavior of BGP updates.

    How These Commands Relate
    =========================

    - The **show running-config all router bgp** command provides the complete BGP configuration, while the other commands provide insights into the operational status, route advertisements, and BGP path information.

    - The **show bgp summary**, **show bgp neighbors**, and **show bgp ipv4 unicast** commands give an overview of the BGP process, neighbor status, and routing table.

    - The **show bgp cidr-only**, **show bgp paths**, and **show bgp rib-failure** commands are focused on analyzing BGP path selection, prefix advertisement, and any issues with route installation.

    - The **show bgp pending-prefixes** and **show bgp neighbor <neighbor> advertised-routes** commands are useful for tracking specific routes being processed and exchanged with BGP neighbors.

    - The **show bgp update-group** command helps understand BGP update group behavior, which is important for optimizing BGP message exchange and ensuring efficient route propagation.
    """
    print(help_text)
