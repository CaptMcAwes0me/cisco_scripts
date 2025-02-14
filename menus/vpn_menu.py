from core.utils import display_formatted_menu
from lina.vpn.anyconnect.anyconnect_tunnel_groups.anyconnect_tunnel_groups import anyconnect_tunnel_groups
from lina.vpn.s2s.s2s_tunnel_groups.s2s_tunnel_groups import s2s_tunnel_groups
from menus.vpn_menu_help.vpn_menu_help import vpn_menu_help


def vpn_menu():
    menu_options = {
        "1": ("AnyConnect (Secure Client) - Menu", anyconnect_tunnel_groups),
        "2": ("Site-to-Site VPN - Menu", s2s_tunnel_groups),
        "3": ("VPN Menu Help", vpn_menu_help),
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
                print("\nExiting to previous menu...")
                break
        else:
            print("\n[!] Invalid choice. Please enter a number between 0 and 2.")
