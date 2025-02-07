from core.utils import display_formatted_menu
from menus.syslog_menu import syslog_menu
from menus.snmp_menu import snmp_menu


def logging_and_monitoring_menu():
    menu_options = {
        "1": ("Syslog Menu", syslog_menu),
        "2": ("SNMP Menu", snmp_menu),
        "0": ("Exit", None),
    }

    while True:
        # Prepare the menu options for display
        options_display = {key: description for key, (description, _) in menu_options.items()}
        display_formatted_menu("System Menu", options_display)

        choice = input("Select an option (0-2): ").strip()

        if choice in menu_options:
            description, function = menu_options[choice]
            if function:  # If a function is assigned
                print("\n" + "-" * 80)
                print(f"Accessing {description}...".center(80))
                print("-" * 80)
                function()
            else:  # Exit condition
                print("\nExiting to previous menu...")
                break
        else:
            print("\n[!] Invalid choice. Please enter a number between 0 and 2.")
