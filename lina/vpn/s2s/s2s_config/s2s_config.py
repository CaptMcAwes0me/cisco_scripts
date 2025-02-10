from core.utils import get_and_parse_cli_output
import re


def s2s_vti_config(ip_address, ike_version):
    """
    Gathers and displays configuration details for Site-to-Site IKEv1 and IKEv2 VTI connections.
    """
    print("=" * 80)
    print(f"Tunnel Group {ip_address} Configuration ({ike_version.upper()})".center(80))
    print("=" * 80)
    command = f"show running-config all tunnel-group {ip_address}"
    output = get_and_parse_cli_output(command)
    print(output)
    print("=" * 80 + "\n")

    # Extract default-group-policy
    group_policy_match = re.search(r"default-group-policy (\S+)", output)
    group_policy = group_policy_match.group(1) if group_policy_match else None

    if group_policy:
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
        if ipsec_profile:
            print("=" * 80)
            print(f"IPSec Profile Configuration: {ipsec_profile}".center(80))
            print("=" * 80)
            profile_output = re.findall(rf"crypto ipsec profile {ipsec_profile}[\s\S]+?(?=crypto|$)", ipsec_output)
            for section in profile_output:
                print(section.strip())
            print("=" * 80 + "\n")

            ipsec_proposal_match = re.search(rf"set ikev2 ipsec-proposal (\S+)", ipsec_output) if ike_version == 'ikev2' else re.search(rf"set transform-set (\S+)", ipsec_output)
            ipsec_proposal = ipsec_proposal_match.group(1) if ipsec_proposal_match else None

            if ipsec_proposal:
                print("=" * 80)
                print(f"IPSec Proposal/Transform-Set Configuration: {ipsec_proposal}".center(80))
                print("=" * 80)
                proposal_output = re.findall(rf"crypto ipsec (ikev2 ipsec-proposal|transform-set) {ipsec_proposal}[\s\S]+?(?=crypto|$)", ipsec_output)
                for section in proposal_output:
                    print(section.strip())
                print("=" * 80 + "\n")

    # Display IKE-specific configurations
    if ike_version == 'ikev2':
        ike_output = get_and_parse_cli_output("show running-config crypto ikev2")
    else:
        ike_output = get_and_parse_cli_output("show running-config crypto isakmp")

    print("=" * 80)
    print(f"Crypto {ike_version.upper()} Configuration".center(80))
    print("=" * 80)
    print(ike_output)
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
    if nameif:
        route_output = get_and_parse_cli_output(f"show route interface {nameif}")
        print("=" * 80)
        print(f"Route Configuration for Interface: {nameif}".center(80))
        print("=" * 80)
        print(route_output)
        print("=" * 80 + "\n")

    print("NOTE: This script does not gather NAT configuration. Manual verification is required for NAT-exemption")
    print("and/or Hairpin NAT statements to ensure they are configured properly.\n")


def s2s_policy_based_config(ip_address, ike_version):
    """
    Gathers and displays configuration details for Site-to-Site IKEv1 and IKEv2 Policy-Based VPNs (Crypto Map).
    """
    print("=" * 80)
    print(f"Policy-Based Configuration for {ip_address} ({ike_version.upper()})".center(80))
    print("=" * 80)

    # Gather Crypto Map Configuration
    crypto_map_output = get_and_parse_cli_output(f"show running-config crypto map | include {ip_address}")
    print(crypto_map_output)
    print("=" * 80 + "\n")

    # Extract Transform-Set or Proposal
    if ike_version == 'ikev2':
        proposal_command = f"show running-config crypto ipsec ikev2 ipsec-proposal"
    else:
        proposal_command = f"show running-config crypto ipsec transform-set"

    proposal_output = get_and_parse_cli_output(proposal_command)
    print("=" * 80)
    print(f"{('IKEv2 IPSec Proposal' if ike_version == 'ikev2' else 'IKEv1 Transform-Set')} Configuration".center(80))
    print("=" * 80)
    print(proposal_output)
    print("=" * 80 + "\n")

    # Display IKE-specific configurations
    if ike_version == 'ikev2':
        ike_output = get_and_parse_cli_output("show running-config crypto ikev2")
    else:
        ike_output = get_and_parse_cli_output("show running-config crypto isakmp")

    print("=" * 80)
    print(f"Crypto {ike_version.upper()} Configuration".center(80))
    print("=" * 80)
    print(ike_output)
    print("=" * 80 + "\n")

    print("NOTE: This script does not gather NAT configuration. Manual verification is required for NAT-exemption")
    print("and/or Hairpin NAT statements to ensure they are configured properly.\n")
