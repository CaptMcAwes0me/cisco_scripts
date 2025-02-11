from lina.vpn.s2s.s2s_tunnel_groups.s2s_tunnel_groups import s2s_tunnel_groups
from lina.vpn.anyconnect.dump_all_anyconnect_data.dump_all_anyconnect_data import dump_all_anyconnect_data
from lina.vpn.s2s.dump_all_s2s_data.dump_all_s2s_data import dump_all_s2s_data
from core.utils import display_formatted_menu


def vpn_dump_menu():
    menu_options = {
        "1": ("AnyConnect (Secure Client) Dump", dump_all_anyconnect_data),
        "2": ("Site-to-Site VPN Dump", dump_all_s2s_data),
        "0": ("Exit", None),
    }

    while True:
        options_display = {key: description for key, (description, _) in menu_options.items()}
        display_formatted_menu("VPN Menu", options_display)

        choice = input("Select an option (0-2): ").strip()

        if choice in menu_options:
            description, function = menu_options[choice]
            if function:
                print("\n" + "-" * 80)
                print(f"Accessing {description}...".center(80))
                print("-" * 80)

                if choice == "2":  # Site-to-Site VPN Dump
                    selected_peers = s2s_tunnel_groups()  # Gather tunnel groups
                    if selected_peers:
                        function(selected_peers)
                    else:
                        print("[!] No tunnel groups found.")
                else:
                    function()

            else:
                print("\nExiting to previous menu...")
                break
        else:
            print("\n[!] Invalid choice. Please enter a number between 0 and 2.")
