def global_routing_help():
    help_text = """
    Lina "Global Routing" Commands Help
    ===================================

    1. **show running-config all route**  
       - Displays the complete running configuration related to routing.  
       - This command provides a full view of the routing-related configuration, such as static routes, route maps, and routing protocol configurations.

    2. **show running-config all router**  
       - Displays the running configuration for all routing protocols (e.g., EIGRP, OSPF, BGP).  
       - Useful for reviewing the global router settings, including the configuration of individual routing protocols.

    3. **show route all**  
       - Displays all routes in the routing table.  
       - Provides a comprehensive view of the routes known to the router, regardless of their source (static, dynamic, etc.), allowing administrators to verify routing table contents.

    4. **show asp table routing all**  
       - Displays the routing table of the Adaptive Security Path (ASP).  
       - Helps administrators view the state of the routing paths within the ASP, including both secure and non-secure routes, and can be used to diagnose routing-related issues in a secure environment.

    How These Commands Relate
    =========================

    - The **show running-config all route** and **show running-config all router** commands provide details on the router's overall configuration, including routing settings and protocols.

    - The **show route all** command helps view all routes in the routing table, enabling a broad understanding of how traffic will be forwarded.

    - The **show asp table routing all** command is particularly useful for viewing the routing state in an adaptive security environment, which can differ from the standard routing table due to security features.

    Together, these commands allow administrators to configure, view, and troubleshoot routing configurations and routing table states across different routing protocols and security paths.
    """
    print(help_text)
