from core.utils import display_formatted_menu
from menus.syslog_menu import syslog_menu
from menus.snmp_menu import snmp_menu
from lina.logging_and_monitoring.logging_and_monitoring_help import logging_and_monitoring_help  # Import help function


def logging_and_monitoring_menu():
    """Displays a menu for logging and monitoring-related tasks.
       Supports 'X?' functionality to display help for each menu option.
    """

    menu_options = {
        "1": ("Syslog - Menu", syslog_menu),
        "2": ("SNMP - Menu", snmp_menu),
        "3": ("Logging & Monitoring Help", logging_and_monitoring_help),
        "0": ("Exit", None),
    }

    while True:
        # Prepare the menu options for display
        options_display = {key: description for key, (description, _) in menu_options.items()}
        display_formatted_menu("Logging & Monitoring Menu", options_display)

        choice = input("Select an option (0-3) or enter '?' for help (e.g., '1?'): ").strip()

        # Handle 'X?' help functionality
        if choice.endswith("?"):
            base_choice = choice[:-1]  # Remove "?" from input
            if base_choice in menu_options:
                description, function = menu_options[base_choice]

                # Special case: `logging_and_monitoring_help` runs directly
                if function == logging_and_monitoring_help:
                    function()
                elif function:
                    print("\n" + "=" * 80)
                    print(f"📖 Help for: {description}".center(80))
                    print("=" * 80)
                    function(help_requested=True)  # Call function in help mode
                else:
                    print("\n[!] Help not available for this option.")
            else:
                print("\n[!] Invalid choice. Please enter a valid number followed by '?' (e.g., '1?').")

        elif choice in menu_options:
            description, function = menu_options[choice]
            if function:
                print("\n" + "-" * 80)
                print(f"Accessing {description}...".center(80))
                print("-" * 80)
                function()  # Normal function execution
            else:
                print("\nExiting to previous menu...")
                break

        else:
            print("\n[!] Invalid choice. Please enter a number between 0 and 3.")
