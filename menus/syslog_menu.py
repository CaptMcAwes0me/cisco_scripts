from core.utils import display_formatted_menu
from lina.logging_and_monitoring.syslog.logging_config.logging_config import logging_config
from lina.logging_and_monitoring.syslog.logging_queue.logging_queue import logging_queue
from lina.logging_and_monitoring.syslog.logging_message.logging_message import logging_message
from lina.logging_and_monitoring.syslog.logging_manager_detail.logging_manager_detail import logging_manager_detail
from lina.logging_and_monitoring.syslog.logging_dynamic_rate_limit.logging_dynamic_rate_limit import logging_dynamic_rate_limit
from lina.logging_and_monitoring.syslog.logging_unified_client.logging_unified_client import logging_unified_client
from lina.logging_and_monitoring.syslog.logging_unified_client_stats.logging_unified_client_stats import logging_unified_client_stats
from lina.logging_and_monitoring.syslog.logging_buffered_output.logging_buffered_output import logging_buffered_output
from lina.logging_and_monitoring.syslog.syslog_help.syslog_help import syslog_help


def syslog_menu(help_requested=False):
    """Displays a menu for syslog-related tasks.
       Supports 'X?' functionality to display help for each menu option.
    """

    syslog_menu_help_info = {
        'command': 'Syslog Menu',
        'description': (
            "The Syslog Menu provides options for configuring, monitoring, and troubleshooting "
            "syslog messages. This menu includes controls for log buffers, dynamic rate limiting, "
            "queue management, and unified logging clients. These commands help diagnose log "
            "delivery failures, performance bottlenecks, and excessive message drops."
        ),
        'troubleshooting_steps': [
            "🔹 **Step 1: Verify Logging Configuration**",
            "   - Run `Logging Config` to ensure logging is enabled and levels are correctly set.",
            "   - Check the logging destination (buffered, console, or remote server).",
            "🔹 **Step 2: Monitor Message Processing**",
            "   - Use `Logging Queue` to inspect log queue size and dropped messages.",
            "   - If logs are being dropped, consider increasing queue limits or adjusting logging rates.",
            "🔹 **Step 3: Check Log Filtering and Dynamic Rate Limits**",
            "   - Run `Logging Dynamic Rate Limit` to ensure rate limits are not filtering out critical logs.",
            "   - If logs are missing, review logging filters and severity settings.",
            "🔹 **Step 4: Debug Logging Client Communication**",
            "   - Use `Logging Unified Client` and `Logging Unified Client Stats` to verify remote logging connectivity.",
            "   - Ensure the syslog server is reachable and accepting messages.",
            "🔹 **Step 5: Examine Buffered Output**",
            "   - Run `Logging Buffered Output` to check if logs are accumulating in the buffer.",
            "   - If logs are stuck in the buffer, increase the buffer size or enable periodic flushing."
        ],
        'example_output': """
================================================================================
                                   Syslog Menu
================================================================================
1) Logging Config
2) Logging Queue
3) Logging Message
4) Logging Manager Detail
5) Logging Dynamic Rate Limit
6) Logging Unified Client
7) Logging Unified Client Stats
8) Logging Buffered Output
9) Logging Help
0) Exit
================================================================================
        """
    }

    if help_requested:
        print("\n" + "=" * 80)
        print(f"📖 Help for: {syslog_menu_help_info['command']}".center(80))
        print("=" * 80)
        print(f"\n{syslog_menu_help_info['description']}\n")
        print("Troubleshooting Steps:")
        for step in syslog_menu_help_info['troubleshooting_steps']:
            print(f"   {step}")
        print("\nExample Output:")
        print(syslog_menu_help_info['example_output'])
        return None

    menu_options = {
        "1": ("Logging Config", logging_config),
        "2": ("Logging Queue", logging_queue),
        "3": ("Logging Message", logging_message),
        "4": ("Logging Manager Detail", logging_manager_detail),
        "5": ("Logging Dynamic Rate Limit", logging_dynamic_rate_limit),
        "6": ("Logging Unified Client", logging_unified_client),
        "7": ("Logging Unified Client Stats", logging_unified_client_stats),
        "8": ("Logging Buffered Output", logging_buffered_output),
        "9": ("Logging Help", syslog_help),
        "0": ("Exit", None),
    }

    while True:
        # Prepare menu display
        options_display = {key: description for key, (description, _) in menu_options.items()}
        display_formatted_menu("Syslog Menu", options_display)

        choice = input("Select an option (0-9) or enter '?' for help (e.g., '3?'): ").strip()

        # Handle 'X?' help functionality
        if choice.endswith("?"):
            base_choice = choice[:-1]  # Remove "?" from input
            if base_choice in menu_options:
                description, function = menu_options[base_choice]

                # Special case: `syslog_help` runs directly
                if function == syslog_help:
                    function()
                elif function:
                    print("\n" + "=" * 80)
                    print(f"📖 Help for: {description}".center(80))
                    print("=" * 80)
                    function(help_requested=True)  # Call function in help mode
                else:
                    print("\n[!] Help not available for this option.")
            else:
                print("\n[!] Invalid choice. Please enter a valid number followed by '?' (e.g., '2?').")

        elif choice in menu_options:
            description, function = menu_options[choice]
            if function:
                print("\n" + "-" * 80)
                print(f"Accessing {description}...".center(80))
                print("-" * 80)
                function()  # Normal function execution
            else:
                print("\nReturning to the previous menu...")
                break

        else:
            print("\n[!] Invalid choice. Please enter a number between 0 and 9.")
