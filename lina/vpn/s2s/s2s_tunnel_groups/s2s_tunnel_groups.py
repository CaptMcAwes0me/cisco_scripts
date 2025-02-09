import re
from core.utils import get_and_parse_cli_output


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
    tunnel_groups = sorted(set([line.split()[1] for line in cli_output.splitlines() if line.startswith("tunnel-group")]))

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

        # Categorize
        if ikev1:
            if vti_match:
                ikev1_vti.append(ip)
            if policy_match:
                ikev1_policy_based.append(ip)

        if ikev2:
            if vti_match:
                ikev2_vti.append(ip)
            if policy_match:
                ikev2_policy_based.append(ip)

    # Display Results
    def display_section(title, items):
        print("=" * 80)
        print(title.center(80))
        print("=" * 80)
        items = sorted(list(set(items)))  # Remove duplicates and sort
        if items:
            for idx, ip in enumerate(items, 1):
                print(f"{idx}. {ip}")
        else:
            print("No tunnels found.")
        print("=" * 80 + "\n")

    display_section("IKEv1 Policy-Based Tunnels", ikev1_policy_based)
    display_section("IKEv1 VTI Tunnels", ikev1_vti)
    display_section("IKEv2 Policy-Based Tunnels", ikev2_policy_based)
    display_section("IKEv2 VTI Tunnels", ikev2_vti)

    return ikev1_policy_based, ikev1_vti, ikev2_policy_based, ikev2_vti
