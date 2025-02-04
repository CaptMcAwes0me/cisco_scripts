from core.utils import display_formatted_menu
from lina.logging_and_monitoring.snmp.snmp_config import snmp_config
from lina.logging_and_monitoring.snmp.snmp_engineid import snmp_engineid
from lina.logging_and_monitoring.snmp.snmp_group import snmp_group
from lina.logging_and_monitoring.snmp.snmp_host import snmp_host
from lina.logging_and_monitoring.snmp.snmp_user import snmp_user
from lina.logging_and_monitoring.snmp.snmp_stats import snmp_stats


def snmp_menu():
    menu_options = {
        "1": ("SNMP Config", snmp_config),
        "2": ("SNMP Engine ID", snmp_engineid),
        "3": ("SNMP Group", snmp_group),
        "4": ("SNMP Host", snmp_host),
        "5": ("SNMP User", snmp_user),
        "6": ("SNMP Stats", snmp_stats),
        "0": ("Exit", None),
    }

    while True:
        # Prepare the menu options for display
        options_display = {key: description for key, (description, _) in menu_options.items()}
        display_formatted_menu("SNMP Menu", options_display)

        choice = input("Select an option (0-6): ").strip()

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
            print("\n[!] Invalid choice. Please enter a number between 0 and 6.")
