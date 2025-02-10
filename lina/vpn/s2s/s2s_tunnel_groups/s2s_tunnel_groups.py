import re
from core.utils import get_and_parse_cli_output
from menus.s2s_menu import s2s_menu


def ip_sort_key(ip):
    return tuple(map(int, ip.split('.')))


def s2s_tunnel_groups():
    """
    Gathers all IPSec S2S tunnels, identifies IKE version, and categorizes as Policy-Based or VTI.
    """
    command = "show running-config tunnel-group | include type ipsec-l2l"
    cli_output = get_and_parse_cli_output(command)

    # Store categories
    ikev1_policy_based = []
    ikev1_vti = []
    ikev2_policy_based = []
    ikev2_vti = []

    # Gather unique IPs
    tunnel_groups = sorted(set([line.split()[1] for line in cli_output.splitlines() if line.startswith("tunnel-group")]), key=ip_sort_key)

    # Mapping for selection
    selection_mapping = {}

    # Process each IP
    for ip in tunnel_groups:
        tunnel_output = get_and_parse_cli_output(f"show running-config tunnel-group {ip}")

        # Determine IKE version
        ikev1 = bool(re.search(r"ikev1 pre-shared-key", tunnel_output))
        ikev2 = bool(re.search(r"ikev2 (remote|local)-authentication pre-shared-key", tunnel_output))

        # Check for Virtual Tunnel Interface
        vti_output = get_and_parse_cli_output("show running-config interface | begin Tunnel")
        vti_match = re.search(rf"tunnel destination {re.escape(ip)}", vti_output)

        # Check for Policy-Based VPN
        policy_output = get_and_parse_cli_output("show running-config crypto map")
        policy_match = re.search(rf"set peer {re.escape(ip)}", policy_output)

        # Categorize and append tuples with (IP, IKE version, VPN type)
        if ikev1:
            if vti_match:
                ikev1_vti.append((ip, 'ikev1', 'vti'))
            if policy_match:
                ikev1_policy_based.append((ip, 'ikev1', 'policy'))

        if ikev2:
            if vti_match:
                ikev2_vti.append((ip, 'ikev2', 'vti'))
            if policy_match:
                ikev2_policy_based.append((ip, 'ikev2', 'policy'))

    # Display Results
    def display_section(title, items, start_index):
        print("=" * 80)
        print(title.center(80))
        print("=" * 80)
        items = sorted(list(set(items)), key=lambda x: ip_sort_key(x[0]))  # Remove duplicates, sort numerically
        index = start_index
        if items:
            for ip_info in items:
                print(f"{index}. {ip_info[0]}")
                selection_mapping[str(index)] = ip_info
                index += 1
        else:
            print("No tunnels found.")
        print("-" * 80 + "\n")
        return index

    index = 1
    index = display_section("IKEv1 Policy-Based Tunnels", ikev1_policy_based, index)
    index = display_section("IKEv1 VTI Tunnels", ikev1_vti, index)
    index = display_section("IKEv2 Policy-Based Tunnels", ikev2_policy_based, index)
    index = display_section("IKEv2 VTI Tunnels", ikev2_vti, index)

    # User selection
    while True:
        choice = input("Select an option (0 to exit, Enter for All): ").strip()

        if choice == "0":
            print("\nExiting to previous menu...")
            return None
        elif choice == "":
            print("\nSelected All Tunnel Groups")
            selected_peers = ikev1_policy_based + ikev1_vti + ikev2_policy_based + ikev2_vti
            break
        elif choice in selection_mapping:
            selected_peers = [selection_mapping[choice]]
            print(f"\nSelected Tunnel Group: {selection_mapping[choice][0]}")
            break
        else:
            print("\n[!] Invalid choice. Please enter a valid option.")

    s2s_menu(selected_peers)  # Pass selected peers to the s2s_menu
