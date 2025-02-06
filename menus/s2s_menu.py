from core.utils import display_formatted_menu
from lina.vpn.s2s.s2s_config.s2s_config import s2s_config
from lina.vpn.s2s.crypto_isakmp_sa_detail.crypto_isakmp_sa_detail import crypto_isakmp_sa_detail
from lina.vpn.s2s.crypto_ipsec_sa_detail.crypto_ipsec_sa_detail import crypto_ipsec_sa_detail
from lina.vpn.s2s.s2s_help.s2s_help import s2s_help


def s2s_menu():
    """Displays a menu for Site-to-Site VPN-related tasks."""

    menu_options = {
        "1": ("Site-to-Site Configuration", s2s_config),
        "2": ("Crypto ISAKMP SA Detail", crypto_isakmp_sa_detail),
        "3": ("Crypto IPSec SA Detail", crypto_ipsec_sa_detail),
        "4": ("Site-to-Site Help", s2s_help),
        "0": ("Exit", None),
    }

    while True:
        # Prepare the menu options for display
        options_display = {key: description for key, (description, _) in menu_options.items()}
        display_formatted_menu("Site-to-Site VPN Menu", options_display)

        choice = input("Select an option (0-3): ").strip()

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
            print("\n[!] Invalid choice. Please enter a number between 0 and 3.")
