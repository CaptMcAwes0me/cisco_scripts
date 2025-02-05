from core.utils import display_formatted_menu
from menus.anyconnect_menu import anyconnect_menu
from menus.s2s_menu import s2s_menu


def vpn_menu():
    menu_options = {
        "1": ("AnyConnect (Secure Client) Menu", anyconnect_menu),
        "2": ("Site-to-Site VPN Menu", s2s_menu),
        "0": ("Exit", None),
    }

    while True:
        # Prepare the menu options for display
        options_display = {key: description for key, (description, _) in menu_options.items()}
        display_formatted_menu("VPN Menu", options_display)

        choice = input("Select an option (0-2): ").strip()

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
            print("\n[!] Invalid choice. Please enter a number between 0 and 2.")
