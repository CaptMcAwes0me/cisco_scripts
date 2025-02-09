from core.utils import display_formatted_menu, get_and_parse_cli_output
from lina.vpn.anyconnect.anyconnect_config.anyconnect_config import anyconnect_config
from lina.vpn.anyconnect.vpn_sessiondb_anyconnect.vpn_sessiondb_anyconnect import vpn_sessiondb_anyconnect
from lina.vpn.anyconnect.crypto_ca_certificates.crypto_ca_certificates import crypto_ca_certificates
from lina.vpn.anyconnect.crypto_ca_trustpoint.crypto_ca_trustpoint import crypto_ca_trustpoint
from lina.vpn.anyconnect.crypto_ca_trustpool.crypto_ca_trustpool import crypto_ca_trustpool
from lina.vpn.anyconnect.crypto_ca_crls.crypto_ca_crls import crypto_ca_crls
from lina.vpn.anyconnect.ssl_cipher.ssl_cipher import ssl_cipher
from lina.vpn.anyconnect.ssl_information.ssl_information import ssl_information
from lina.vpn.anyconnect.ssl_errors.ssl_errors import ssl_errors
from lina.vpn.anyconnect.anyconnect_help.anyconnect_help import anyconnect_help


def anyconnect_menu(selected_group, tunnel_groups=[]):
    """Displays a menu for AnyConnect-related tasks."""

    if not tunnel_groups:
        tunnel_groups = [selected_group]

    menu_options = {
        "1": ("AnyConnect Configuration", anyconnect_config),
        "2": ("VPN Session Database", vpn_sessiondb_anyconnect),
        "3": ("Crypto CA Certificates", crypto_ca_certificates),
        "4": ("Crypto CA Trustpoints", crypto_ca_trustpoint),
        "5": ("Crypto CA Trustpool", crypto_ca_trustpool),
        "6": ("Crypto CA CRLs", crypto_ca_crls),
        "7": ("SSL Cipher", ssl_cipher),
        "8": ("SSL Information", ssl_information),
        "9": ("SSL Errors", ssl_errors),
        "10": ("Anyconnect Help", anyconnect_help),
        "0": ("Exit", None),
    }

    while True:
        options_display = {key: description for key, (description, _) in menu_options.items()}
        display_formatted_menu(f"AnyConnect Menu - Selected Group: {selected_group}", options_display)

        choice = input("Select an option (0-9): ").strip()

        if choice in menu_options:
            description, function = menu_options[choice]
            if function:
                print("\n" + "-" * 80)
                print(f"Accessing {description}...".center(80))
                print("-" * 80)

                # Conditionally handle multiple tunnel groups
                if function in [anyconnect_config, vpn_sessiondb_anyconnect]:
                    for group in tunnel_groups:
                        function(group)
                else:
                    function()

            else:
                print("\nExiting to previous menu...")
                break
        else:
            print("\n[!] Invalid choice. Please enter a number between 0 and 9.")
