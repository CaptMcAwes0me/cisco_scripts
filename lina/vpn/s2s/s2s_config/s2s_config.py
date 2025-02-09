from core.utils import get_and_parse_cli_output
import re


def s2s_config(suppress_output=False):
    """Retrieves and optionally writes Site-to-Site VPN-related configurations."""

    commands = [
        "show running-config all crypto",
        "show running-config all tunnel-group",
        "show running-config all group-policy",
        "show running-config all interface | begin Tunnel"
    ]

    try:
        outputs = {cmd: get_and_parse_cli_output(cmd) for cmd in commands}

        formatted_output = "\n".join([
            "-" * 80,
            "Accessing Site-to-Site VPN Configuration...".center(80),
            "-" * 80,
            "Site-to-Site VPN Configuration Output".center(80),
            "-" * 80
        ])

        for cmd, output in outputs.items():
            formatted_output += f"\n\n{cmd} Output:\n" + "-" * 80 + f"\n{output.strip()}"

        formatted_output += "\n" + "-" * 80

        if not suppress_output:
            print(formatted_output)

        return formatted_output  # Returns a formatted string instead of a tuple

    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message


def s2s_ikev2_vti_config():
    """
    Gathers and displays configuration details for Site-to-Site IKEv2 VTI connections.
    """
    def process_tunnel_group(ip_address):
        print("=" * 80)
        print(f"Tunnel Group {ip_address} Configuration".center(80))
        print("=" * 80)
        command = f"show running-config all tunnel-group {ip_address}"
        output = get_and_parse_cli_output(command)

        # Skip remote-access tunnel-groups
        if re.search(r"tunnel-group \S+ type remote-access", output):
            return

        print(output)
        print("=" * 80 + "\n")

        # Extract default-group-policy
        group_policy_match = re.search(r"default-group-policy (\S+)", output)
        group_policy = group_policy_match.group(1) if group_policy_match else None

        if group_policy and group_policy not in processed_group_policies:
            processed_group_policies.add(group_policy)
            print("=" * 80)
            print(f"Group Policy Configuration for {group_policy}".center(80))
            print("=" * 80)
            gp_command = f"show running-config all group-policy {group_policy}"
            gp_output = get_and_parse_cli_output(gp_command)
            print(gp_output)
            print("=" * 80 + "\n")

        # Identify Tunnel Interface
        tunnel_output = get_and_parse_cli_output("show running-config interface | begin Tunnel")
        tunnel_match = re.search(r"interface (Tunnel\S+)[\s\S]+?tunnel destination " + re.escape(ip_address), tunnel_output)

        if tunnel_match:
            tunnel_interface = tunnel_match.group(1)
            print("=" * 80)
            print(f"Tunnel Interface Configuration: {tunnel_interface}".center(80))
            print("=" * 80)
            tunnel_interface_cmd = f"show running-config all interface {tunnel_interface}"
            tunnel_interface_output = get_and_parse_cli_output(tunnel_interface_cmd)
            print(tunnel_interface_output)
            print("=" * 80 + "\n")

            # Extract IPSec Profile
            ipsec_profile_match = re.search(r"tunnel protection ipsec profile (\S+)", tunnel_interface_output)
            ipsec_profile = ipsec_profile_match.group(1) if ipsec_profile_match else None

            # IPSec Profile and Proposal Configuration
            ipsec_output = get_and_parse_cli_output("show running-config ipsec")
            if ipsec_profile and ipsec_profile not in processed_ipsec_profiles:
                processed_ipsec_profiles.add(ipsec_profile)
                print("=" * 80)
                print(f"IPSec Profile Configuration: {ipsec_profile}".center(80))
                print("=" * 80)
                profile_config_match = re.search(rf"crypto ipsec profile {ipsec_profile}[\s\S]+?set ikev2 ipsec-proposal (\S+)", ipsec_output)
                ipsec_proposal = profile_config_match.group(1) if profile_config_match else None
                profile_output = re.findall(rf"crypto ipsec profile {ipsec_profile}[\s\S]+?(?=crypto|$)", ipsec_output)
                for section in profile_output:
                    print(section.strip())
                print("=" * 80 + "\n")

                if ipsec_proposal and ipsec_proposal not in processed_ipsec_proposals:
                    processed_ipsec_proposals.add(ipsec_proposal)
                    print("=" * 80)
                    print(f"IPSec Proposal Configuration: {ipsec_proposal}".center(80))
                    print("=" * 80)
                    proposal_output = re.findall(rf"crypto ipsec ikev2 ipsec-proposal {ipsec_proposal}[\s\S]+?(?=crypto|$)", ipsec_output)
                    for section in proposal_output:
                        print(section.strip())
                    print("=" * 80 + "\n")

            # Crypto IKEv2 Configuration
            ikev2_output = get_and_parse_cli_output("show running-config crypto ikev2")
            print("=" * 80)
            print("Crypto IKEv2 Configuration".center(80))
            print("=" * 80)
            print(ikev2_output)
            print("=" * 80 + "\n")

            # Sysopt Configuration Related to VPN
            sysopt_output = get_and_parse_cli_output("show running-config all sysopt | include vpn")
            print("=" * 80)
            print("Sysopt Configuration (related to VPN)".center(80))
            print("=" * 80)
            print(sysopt_output)
            print("=" * 80 + "\n")

            # Show Route Interface
            nameif_match = re.search(r"nameif (\S+)", tunnel_interface_output)
            nameif = nameif_match.group(1) if nameif_match else None
            if nameif and nameif not in processed_route_interfaces:
                processed_route_interfaces.add(nameif)
                route_output = get_and_parse_cli_output(f"show route interface {nameif}")
                print("=" * 80)
                print(f"Route Configuration for Interface: {nameif}".center(80))
                print("=" * 80)
                print(route_output)
                print("=" * 80 + "\n")

    processed_group_policies = set()
    processed_ipsec_profiles = set()
    processed_ipsec_proposals = set()
    processed_route_interfaces = set()

    while True:
        ip_address = input("Enter IP Address (Enter for All or 0 to exit): ").strip()
        if ip_address == '0':
            return

        if ip_address:
            process_tunnel_group(ip_address)
        else:
            tunnel_groups_output = get_and_parse_cli_output("show running-config tunnel-group | include tunnel-group")
            ip_addresses = re.findall(r"tunnel-group (\S+) type (?!remote-access)", tunnel_groups_output)
            for ip in ip_addresses:
                process_tunnel_group(ip)

        print("NOTE: This script does not gather NAT configuration. Manual verification is required for NAT-exemption")
        print("and/or Hairpin NAT statements to ensure they are configured properly.\n")


