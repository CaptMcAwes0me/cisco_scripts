# Description: This script contains the Logging and Monitoring Dump menu.

from lina.logging_and_monitoring.syslog.dump_all_syslog_data import dump_all_syslog_data
from lina.logging_and_monitoring.snmp.dump_all_snmp_data import dump_all_snmp_data
from core.utils import display_formatted_menu


def logging_and_monitoring_dump_menu():
    menu_options = {
        "1": ("Dump All Syslog Data", dump_all_syslog_data),
        "2": ("Dump All SNMP Data", dump_all_snmp_data),
        "0": ("Exit", None),
    }

    while True:
        # Prepare the menu options for display
        options_display = {key: description for key, (description, _) in menu_options.items()}
        display_formatted_menu("Logging and Monitoring Dump Menu", options_display)

        choice = input("Select an option (0-2): ").strip()

        if choice in menu_options:
            description, function = menu_options[choice]
            if function:  # If a function is assigned
                print("\n" + "-" * 80)
                print(f"Accessing {description}...".center(80))
                print("-" * 80)
                function()  # Call the corresponding function
            else:  # Exit condition
                print("\nExiting the script. Goodbye!")
                break
        else:
            print("\n[!] Invalid choice. Please enter a number between 0 and 2.")
