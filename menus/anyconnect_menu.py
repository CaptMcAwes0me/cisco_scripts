from core.utils import display_formatted_menu
from lina.vpn.anyconnect.anyconnect_config.anyconnect_config import anyconnect_config
from lina.vpn.anyconnect.vpn_sessiondb_anyconnect.vpn_sessiondb_anyconnect import vpn_sessiondb_anyconnect
from lina.vpn.anyconnect.crypto_ca_data.crypto_ca_data import crypto_ca_data
from lina.vpn.anyconnect.ssl_data.ssl_data import ssl_data
from lina.vpn.anyconnect.anyconnect_help.anyconnect_help import anyconnect_help
from lina.vpn.anyconnect.anyconnect_crypto_accelerator_data.anyconnect_crypto_accelerator_data import anyconnect_crypto_accelerator_data


def anyconnect_menu(selected_group, tunnel_groups=[]):
    """Displays a menu for AnyConnect-related tasks."""

    if not tunnel_groups:
        tunnel_groups = [selected_group]

    menu_options = {
        "1": ("AnyConnect Configuration", anyconnect_config),
        "2": ("VPN Session Database", vpn_sessiondb_anyconnect),
        "3": ("Crypto CA Data", crypto_ca_data),
        "4": ("SSL Data", ssl_data),
        "5": ("Crypto Accelerator Data", anyconnect_crypto_accelerator_data),
        "6": ("AnyConnect Help", anyconnect_help),
        "0": ("Exit", None),
    }

    while True:
        options_display = {key: description for key, (description, _) in menu_options.items()}
        display_formatted_menu(f"AnyConnect Menu - Selected Group: {selected_group}", options_display)

        choice = input("Select an option (0-6) or enter '?' for help (e.g., '2?'): ").strip()

        # Handle help requests (X?)
        if choice.endswith("?"):
            base_choice = choice[:-1]  # Remove "?" from input
            if base_choice in menu_options:
                description, function = menu_options[base_choice]

                print("\n" + "=" * 80)
                print(f"📖 Help for: {description}".center(80))
                print("=" * 80)

                # Special case: `anyconnect_help` does not need parameters
                if function == anyconnect_help:
                    function()
                # Special case: `anyconnect_config` and `vpn_sessiondb_anyconnect` require tunnel_group
                elif function in [anyconnect_config, vpn_sessiondb_anyconnect]:
                    function(selected_group, help_requested=True)
                # Default behavior for other functions
                else:
                    function(help_requested=True)

            else:
                print("\n[!] Invalid choice. Please enter a valid number followed by '?' (e.g., '3?').")

        elif choice in menu_options:
            description, function = menu_options[choice]

            if function:
                print("\n" + "-" * 80)
                print(f"Accessing {description}...".center(80))
                print("-" * 80)

                # Handle multiple tunnel groups for specific functions
                if function in [anyconnect_config, vpn_sessiondb_anyconnect]:
                    for group in tunnel_groups:
                        function(group)
                else:
                    function()

            else:
                print("\nExiting to previous menu...")
                break
        else:
            print("\n[!] Invalid choice. Please enter a number between 0 and 6.")
