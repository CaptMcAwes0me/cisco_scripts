import re
from core.utils import get_and_parse_cli_output
from lina.vpn.s2s.s2s_config.s2s_config import (
    s2s_ikev1_vti_config,
    s2s_ikev1_policy_based_config,
    s2s_ikev2_vti_config,
    s2s_ikev2_policy_based_config
)


def ip_sort_key(ip):
    return tuple(map(int, ip.split('.')))


def s2s_tunnel_groups():
    command = "show running-config tunnel-group | include type ipsec-l2l"
    cli_output = get_and_parse_cli_output(command)

    ikev1_policy_based = []
    ikev1_vti = []
    ikev2_policy_based = []
    ikev2_vti = []

    tunnel_groups = sorted(set([line.split()[1] for line in cli_output.splitlines() if line.startswith("tunnel-group")]), key=ip_sort_key)
    selection_mapping = {}

    for ip in tunnel_groups:
        tunnel_output = get_and_parse_cli_output(f"show running-config tunnel-group {ip}")

        ikev1 = bool(re.search(r"ikev1 pre-shared-key", tunnel_output))
        ikev2 = bool(re.search(r"ikev2 (remote|local)-authentication pre-shared-key", tunnel_output))

        vti_output = get_and_parse_cli_output("show running-config interface | begin Tunnel")
        vti_match = re.search(rf"tunnel destination {re.escape(ip)}", vti_output)

        policy_output = get_and_parse_cli_output("show running-config crypto map")
        policy_match = re.search(rf"set peer {re.escape(ip)}", policy_output)

        if ikev1:
            if vti_match:
                ikev1_vti.append((ip, vti_match.group()))
            if policy_match:
                ikev1_policy_based.append(ip)

        if ikev2:
            if vti_match:
                ikev2_vti.append((ip, vti_match.group()))
            if policy_match:
                ikev2_policy_based.append(ip)

    def display_section(title, items, start_index):
        print("=" * 80)
        print(title.center(80))
        print("=" * 80)
        index = start_index
        for item in items:
            ip = item[0] if isinstance(item, tuple) else item
            print(f"{index}. {ip}")
            selection_mapping[str(index)] = item
            index += 1
        print("=" * 80 + "\n")
        return index

    index = 1
    index = display_section("IKEv1 Policy-Based Tunnels", ikev1_policy_based, index)
    index = display_section("IKEv1 VTI Tunnels", ikev1_vti, index)
    index = display_section("IKEv2 Policy-Based Tunnels", ikev2_policy_based, index)
    index = display_section("IKEv2 VTI Tunnels", ikev2_vti, index)

    while True:
        choice = input("Select an option (0 to exit, Enter for All): ").strip()

        if choice == "0":
            print("\nExiting to previous menu...")
            return None
        elif choice == "":
            print("\nSelected All Tunnel Groups")
            selected_peers = tunnel_groups
            break
        elif choice in selection_mapping:
            selected_item = selection_mapping[choice]
            ip_address = selected_item[0] if isinstance(selected_item, tuple) else selected_item
            matched_interface = selected_item[1] if isinstance(selected_item, tuple) else None

            if selected_item in ikev1_vti:
                s2s_ikev1_vti_config(ip_address)
            elif selected_item in ikev1_policy_based:
                s2s_ikev1_policy_based_config(ip_address)
            elif selected_item in ikev2_vti:
                s2s_ikev2_vti_config(ip_address)
            elif selected_item in ikev2_policy_based:
                s2s_ikev2_policy_based_config(ip_address)
            break
        else:
            print("\n[!] Invalid choice. Please enter a valid option.")
