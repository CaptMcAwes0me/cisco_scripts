from core.utils import display_formatted_menu
from lina.vpn.s2s.s2s_config.s2s_config import (
    s2s_ikev1_vti_config,
    s2s_ikev1_policy_based_config,
    s2s_ikev2_vti_config,
    s2s_ikev2_policy_based_config,
)
from lina.vpn.s2s.s2s_crypto_accelerator_data.s2s_crypto_accelerator_data import s2s_crypto_accelerator_data
from lina.vpn.s2s.crypto_isakmp_sa_detail.crypto_isakmp_sa_detail import crypto_isakmp_sa_detail
from lina.vpn.s2s.crypto_ipsec_sa_detail.crypto_ipsec_sa_detail import crypto_ipsec_sa_detail
from lina.vpn.s2s.s2s_help.s2s_help import s2s_help


def s2s_menu(selected_peers):
    """
    Displays a menu for Site-to-Site VPN-related tasks.
    Allows '?' suffix for inline help on any option.
    Allows 'Enter' to select all tunnel groups.
    """
    menu_options = {
        "1": ("Site-to-Site Configuration", None),
        "2": ("Crypto ISAKMP SA Detail", crypto_isakmp_sa_detail),
        "3": ("Crypto IPSec SA Detail", crypto_ipsec_sa_detail),
        "4": ("Crypto Accelerator Data", s2s_crypto_accelerator_data),
        "5": ("Site-to-Site Help", s2s_help),
        "0": ("Exit", None),
    }

    all_selected = False  # Flag to track if "All" is selected

    while True:
        # Prepare the menu options for display
        options_display = {key: description for key, (description, _) in menu_options.items()}
        display_formatted_menu("Site-to-Site VPN Menu", options_display)

        choice = input("Select an option (0 to exit, Enter for All): ").strip().lower()

        # Handle 'Enter' for All Tunnel Groups (just select them, don't execute)
        if choice == "":
            all_selected = True
            print("\n✅ All peers have been selected. Choose an option to execute.\n")
            continue  # Redisplay menu instead of executing anything now

        # Check if the user entered a valid option with "?" appended (e.g., "3?")
        elif choice.endswith("?"):
            base_choice = choice[:-1]  # Remove "?" from input
            if base_choice in menu_options:
                description, function = menu_options[base_choice]

                if base_choice == "1":
                    print("\n" + "=" * 80)
                    print("📖 Site-to-Site Configuration Help".center(80))
                    print("=" * 80)

                    peers_to_process = selected_peers if all_selected else [selected_peers[0]]

                    for peer in peers_to_process:
                        ip_address, ike_version, vpn_type = peer  # Unpack peer details

                        print(f"\n🔍 Help for peer: {ip_address} (IKEv{ike_version.upper()} - {vpn_type.upper()})")

                        if ike_version == "ikev1" and vpn_type == "vti":
                            s2s_ikev1_vti_config(ip_address, help_requested=True)
                        elif ike_version == "ikev1" and vpn_type == "policy":
                            s2s_ikev1_policy_based_config(ip_address, help_requested=True)
                        elif ike_version == "ikev2" and vpn_type == "vti":
                            s2s_ikev2_vti_config(ip_address, help_requested=True)
                        elif ike_version == "ikev2" and vpn_type == "policy":
                            s2s_ikev2_policy_based_config(ip_address, help_requested=True)

                elif function:
                    print("\n" + "=" * 80)
                    print(f"📖 Help for: {description}".center(80))
                    print("=" * 80)

                    if function == crypto_ipsec_sa_detail:
                        function(selected_peers, help_requested=True)
                    elif function == s2s_help:
                        function()
                    else:
                        function(help_requested=True)

                else:
                    print("\n[!] Help not available for this option.")
            else:
                print("\n[!] Invalid choice. Please enter a valid number followed by '?' (e.g., '3?').")

        # Process standard menu selections
        elif choice in menu_options:
            description, function = menu_options[choice]

            # Handle Site-to-Site Configuration (Option 1)
            if choice == "1":
                print("\n" + "=" * 80)
                print("🔹 Running Site-to-Site Configuration for Selected Peers".center(80))
                print("=" * 80)

                peers_to_process = selected_peers if all_selected else [selected_peers[0]]

                for peer in peers_to_process:
                    ip_address, ike_version, vpn_type = peer  # Unpack peer details

                    print(f"\n🔍 Configuring peer: {ip_address} (IKEv{ike_version.upper()} - {vpn_type.upper()})")

                    if ike_version == "ikev1" and vpn_type == "vti":
                        s2s_ikev1_vti_config(ip_address)
                    elif ike_version == "ikev1" and vpn_type == "policy":
                        s2s_ikev1_policy_based_config(ip_address)
                    elif ike_version == "ikev2" and vpn_type == "vti":
                        s2s_ikev2_vti_config(ip_address)
                    elif ike_version == "ikev2" and vpn_type == "policy":
                        s2s_ikev2_policy_based_config(ip_address)

                print("\n✅ Configuration Complete.")

            # Execute the chosen function for options 2-5
            elif function:
                print("\n" + "=" * 80)
                print(f"🔹 Accessing {description}".center(80))
                print("=" * 80)

                if function == crypto_ipsec_sa_detail:
                    function(selected_peers, help_requested=False)
                elif function in (crypto_isakmp_sa_detail, s2s_crypto_accelerator_data):
                    function(help_requested=False)
                else:
                    function()

            # Exit condition
            else:
                print("\nExiting to previous menu...")
                break

        else:
            print("\n[!] Invalid choice. Please enter a number between 0 and 5.")
