from core.utils import display_formatted_menu
from lina.vpn.anyconnect.anyconnect_tunnel_groups.anyconnect_tunnel_groups import anyconnect_tunnel_groups
from lina.vpn.s2s.s2s_tunnel_groups.s2s_tunnel_groups import s2s_tunnel_groups
from menus.vpn_menu_help.vpn_menu_help import vpn_menu_help


def vpn_menu():
    """
    Displays the VPN menu with options for AnyConnect and Site-to-Site VPNs.
    Allows '?' suffix for inline help on any option.
    """
    menu_options = {
        "1": ("AnyConnect (Secure Client) Menu", anyconnect_tunnel_groups),
        "2": ("Site-to-Site VPN Menu", s2s_tunnel_groups),
        "3": ("VPN Menu Help", vpn_menu_help),
        "0": ("Exit", None),
    }

    while True:
        # Prepare the menu options for display
        options_display = {key: description for key, (description, _) in menu_options.items()}
        display_formatted_menu("VPN Menu", options_display)

        choice = input("Select an option (0-3) or enter '?' for help (e.g., '2?'): ").strip().lower()

        # Check if the user entered a valid option with "?" appended (e.g., "2?")
        if choice.endswith("?"):
            base_choice = choice[:-1]  # Remove "?" from input
            if base_choice in menu_options:
                description, function = menu_options[base_choice]

                print("\n" + "=" * 80)
                print(f"📖 Help for: {description}".center(80))
                print("=" * 80)

                # Special case: vpn_menu_help doesn't take arguments
                if function == vpn_menu_help:
                    function()
                else:
                    function(help_requested=True)  # Call function with help_requested=True
            else:
                print("\n[!] Invalid choice. Please enter a valid number followed by '?' (e.g., '2?').")

        elif choice in menu_options:
            description, function = menu_options[choice]
            if function:  # If a function is assigned
                print("\n" + "-" * 80)
                print(f"🔹 Accessing {description}...".center(80))
                print("-" * 80)
                function()
            else:  # Exit condition
                print("\nExiting to previous menu...")
                break
        else:
            print("\n[!] Invalid choice. Please enter a number between 0 and 3.")
