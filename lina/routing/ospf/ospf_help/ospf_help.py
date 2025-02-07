def ospf_help():
    help_text = """
    Lina "OSPF" Commands Help
    =========================

    1. **show running-config all router ospf**  
       - Displays the complete running configuration for OSPF (Open Shortest Path First).  
       - This command shows the OSPF-specific configuration on the router, including router IDs, area configurations, and network advertisements.

    2. **show ospf all**  
       - Displays all OSPF-related information on the router.  
       - This command provides a comprehensive view of OSPF details such as routing information, neighbors, and interface configurations.

    3. **show ospf border-routers**  
       - Displays the OSPF border routers.  
       - Useful for identifying OSPF routers that are configured as border routers between different OSPF areas or between OSPF and other routing protocols.

    4. **show ospf database**  
       - Displays the OSPF link-state database.  
       - This database contains all the link-state advertisements (LSAs) in OSPF, which describe the network topology and are used for calculating the best path.

    5. **show ospf events**  
       - Displays the OSPF event log.  
       - This log provides detailed information about OSPF events such as state changes, neighbor transitions, and OSPF process behavior.

    6. **show ospf interface**  
       - Displays OSPF-specific information about the router's interfaces.  
       - This command shows details about OSPF-enabled interfaces, including their state, IP addresses, and the OSPF settings applied to them.

    7. **show ospf neighbor**  
       - Displays information about OSPF neighbors.  
       - Shows the status of OSPF neighbor relationships, including the neighbor's IP address, interface, and the state of the OSPF adjacency.

    8. **show ospf nsf**  
       - Displays information about OSPF Non-Stop Forwarding (NSF) status.  
       - NSF helps OSPF maintain routing without interruption during a router failure, and this command provides the current status of NSF on the router.

    9. **show ospf rib**  
       - Displays the OSPF Routing Information Base (RIB).  
       - This command shows the routes learned through OSPF, helping administrators verify the routes and check OSPF's decision-making process.

    10. **show ospf statistics**  
        - Displays OSPF statistics.  
        - Provides information about OSPF process statistics, including the number of LSAs processed, OSPF packets sent and received, and other OSPF-related counters.

    11. **show ospf traffic**  
        - Displays OSPF traffic details.  
        - Helps analyze the OSPF traffic, including the volume of OSPF packets sent and received, allowing for troubleshooting of OSPF-related performance issues.

    How These Commands Relate
    =========================

    - The **show running-config all router ospf** command provides a high-level overview of the OSPF configuration on the router.

    - The **show ospf all**, **show ospf database**, and **show ospf rib** commands provide insight into the router's OSPF routing information, including databases and routes.

    - The **show ospf interface**, **show ospf neighbor**, and **show ospf border-routers** commands provide details about the OSPF-enabled interfaces and the status of OSPF relationships with other routers.

    - The **show ospf events** and **show ospf statistics** commands help monitor OSPF behavior and performance, while the **show ospf nsf** command provides details about the Non-Stop Forwarding functionality for OSPF.

    - The **show ospf traffic** command helps with troubleshooting performance issues related to OSPF traffic and packet exchanges.
    """
    print(help_text)
