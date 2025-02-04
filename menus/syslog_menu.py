from core.utils import display_formatted_menu
from lina.logging_and_monitoring.syslog.logging_config import logging_config
from lina.logging_and_monitoring.syslog.logging_queue import logging_queue
from lina.logging_and_monitoring.syslog.logging_message import logging_message
from lina.logging_and_monitoring.syslog.logging_manager_detail import logging_manager_detail
from lina.logging_and_monitoring.syslog.logging_dynamic_rate_limit import logging_dynamic_rate_limit
from lina.logging_and_monitoring.syslog.logging_unified_client import logging_unified_client
from lina.logging_and_monitoring.syslog.logging_unified_client_stats import logging_unified_client_stats
from lina.logging_and_monitoring.syslog.logging_buffered_output import logging_buffered_output


def syslog_menu():
    menu_options = {
        "1": ("Logging Config", logging_config),
        "2": ("Logging Queue", logging_queue),
        "3": ("Logging Message", logging_message),
        "4": ("Logging Manager Detail", logging_manager_detail),
        "5": ("Logging Dynamic Rate Limit", logging_dynamic_rate_limit),
        "6": ("Logging Unified Client", logging_unified_client),
        "7": ("Logging Unified Client Stats", logging_unified_client_stats),
        "8": ("Logging Buffered Output", logging_buffered_output),
        "0": ("Exit", None),
    }

    while True:
        # Prepare the menu options for display
        options_display = {key: description for key, (description, _) in menu_options.items()}
        display_formatted_menu("Syslog Menu", options_display)

        choice = input("Select an option (0-8): ").strip()

        if choice in menu_options:
            description, function = menu_options[choice]
            if function:  # If a function is assigned
                print("\n" + "-" * 80)
                print(f"Accessing {description}...".center(80))
                print("-" * 80)
                function()
            else:  # Exit condition
                print("\nExiting the script. Goodbye!")
                break
        else:
            print("\n[!] Invalid choice. Please enter a number between 0 and 8.")
