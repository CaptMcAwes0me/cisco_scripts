import re
from core.utils import get_and_parse_cli_output, display_formatted_menu
from lina.vpn.s2s.crypto_isakmp_sa_detail.crypto_isakmp_sa_detail import crypto_isakmp_sa_detail
from lina.vpn.s2s.crypto_ipsec_sa_detail.crypto_ipsec_sa_detail import crypto_ipsec_sa_detail
from lina.vpn.s2s.s2s_help.s2s_help import s2s_help
from lina.vpn.s2s.s2s_config.s2s_config import s2s_vti_config, s2s_policy_based_config


def ip_sort_key(ip):
    return tuple(map(int, ip.split('.')))


def detect_and_route(ip_address, selected_ike_version=None):
    """
    Detects the IKE version and VPN type (VTI or Policy-Based) for the given IP and routes to the correct function.
    """
    # Detect IKE version
    tunnel_output = get_and_parse_cli_output(f"show running-config tunnel-group {ip_address}")
    ike_version = None

    if selected_ike_version:
        ike_version = selected_ike_version
    else:
        if re.search(r"ikev1 pre-shared-key", tunnel_output):
            ike_version = 'ikev1'
        elif re.search(r"ikev2 (remote|local)-authentication", tunnel_output):
            ike_version = 'ikev2'

    if not ike_version:
        print(f"Unable to determine IKE version for {ip_address}.")
        return

    # Detect VPN Type (VTI or Policy-Based)
    vti_output = get_and_parse_cli_output("show running-config interface | begin Tunnel")
    policy_output = get_and_parse_cli_output("show running-config crypto map")

    # Extract all tunnel interface blocks
    tunnel_blocks = re.findall(r"(interface Tunnel\S+[\s\S]*?)(?=\ninterface|\Z)", vti_output)

    matched_interface = None
    for block in tunnel_blocks:
        if re.search(rf"tunnel destination {re.escape(ip_address)}", block):
            matched_interface = re.search(r"interface (Tunnel\S+)", block).group(1)
            break

    policy_match = re.search(rf"set peer {re.escape(ip_address)}", policy_output)

    if matched_interface:
        s2s_vti_config(ip_address, ike_version, matched_interface)
    elif policy_match:
        s2s_policy_based_config(ip_address, ike_version)
    else:
        print(f"Unable to determine VPN type for {ip_address}.")


def s2s_menu(selected_peers):
    """
    Displays a menu for Site-to-Site VPN-related tasks.
    """
    menu_options = {
        "1": ("Site-to-Site Configuration", detect_and_route),
        "2": ("Crypto ISAKMP SA Detail", crypto_isakmp_sa_detail),
        "3": ("Crypto IPSec SA Detail", crypto_ipsec_sa_detail),
        "4": ("Site-to-Site Help", s2s_help),
        "0": ("Exit", None),
    }

    while True:
        options_display = {key: description for key, (description, _) in menu_options.items()}
        display_formatted_menu("Site-to-Site VPN Menu", options_display)

        choice = input("Select an option (0-4): ").strip()

        if choice in menu_options:
            description, function = menu_options[choice]
            if function:
                print("\n" + "-" * 80)
                print(f"Accessing {description}...".center(80))
                print("-" * 80)

                if function == detect_and_route:
                    for ip_address in selected_peers:
                        detect_and_route(ip_address)
                else:
                    function(selected_peers)
            else:
                print("\nExiting to previous menu...")
                break
        else:
            print("\n[!] Invalid choice. Please enter a number between 0 and 4.")
