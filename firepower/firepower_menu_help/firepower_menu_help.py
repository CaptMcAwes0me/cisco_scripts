def firepower_menu_help():
    help_text = """
    === Firepower Troubleshooting Help ===

    The Firepower Menu provides diagnostic tools to troubleshoot common issues within a Firepower device.

    **Menu Options:**
    1) Device Information - View system version, hardware specifications, and uptime details.
    2) Registration Troubleshooting - Check device registration status and troubleshoot connectivity.
    3) Database Troubleshooting - Analyze Firepower database integrity and performance.
    4) Disk Usage Troubleshooting - Monitor disk space usage and identify storage-related issues.
    5) System CPU Troubleshooting (FTD Only) - Analyze CPU usage and process performance (Firepower Threat Defense only).
    0) Exit - Return to the previous menu.

    **Usage Tips:**
    - Use Device Information to gather system details before troubleshooting.
    - Registration Troubleshooting helps diagnose communication issues between Firepower and its management system.
    - Database and Disk Usage tools help ensure proper system functionality.
    - CPU Troubleshooting is essential for performance monitoring, especially on FTD devices.

    ============================================
    """
    print(help_text)

