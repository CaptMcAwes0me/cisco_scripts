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
            "                     Accessing Site-to-Site VPN Configuration...",
            "-" * 80,
            "\nSite-to-Site VPN Configuration Output:",
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


def s2s_vti_config(ip_address, ike_version, tunnel_interface):
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
            proposal_output = re.findall(rf"crypto ipsec ikev2 ipsec-proposal {ipsec_proposal}[\s\S]+?(?=crypto|$)", ipsec_output)
            for section in proposal_output:
                print(section.strip())
            print("=" * 80 + "\n")

    # Display IKE-specific configurations
    if ike_version == 'ikev2':
        ike_output = get_and_parse_cli_output("show running-config crypto ikev2")
    else:
        ike_output = get_and_parse_cli_output("show running-config crypto ikev1")

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
    crypto_map_output = get_and_parse_cli_output(f"show running-config crypto map")
    crypto_map_lines = [line for line in crypto_map_output.splitlines() if ip_address in line]

    if crypto_map_lines:
        # Extract Crypto Map Name and Sequence Number
        crypto_map_match = re.search(rf"crypto map (\S+) (\d+) set peer {re.escape(ip_address)}", "\n".join(crypto_map_lines))
        if crypto_map_match:
            crypto_map_name, crypto_map_number = crypto_map_match.groups()

            # Get the full crypto map configuration
            crypto_map_details = get_and_parse_cli_output(
                f"show running-config crypto map | include {crypto_map_name} {crypto_map_number}"
            )

            print("=" * 80)
            print(f"Crypto Map Configuration: {crypto_map_name} {crypto_map_number}".center(80))
            print("=" * 80)
            print(crypto_map_details)
            print("=" * 80 + "\n")

            # Extract the transform-set name
            transform_set_match = re.search(rf"set ikev1 transform-set (\S+)", crypto_map_details)
            transform_set_name = transform_set_match.group(1) if transform_set_match else None

            if transform_set_name:
                transform_set_output = get_and_parse_cli_output(
                    f"show running-config crypto | include crypto ipsec ikev1 transform-set {transform_set_name}"
                )
                print("=" * 80)
                print(f"Transform-Set Configuration: {transform_set_name}".center(80))
                print("=" * 80)
                print(transform_set_output)
                print("=" * 80 + "\n")

            # Extract the ACL name
            acl_match = re.search(rf"match address (\S+)", crypto_map_details)
            acl_name = acl_match.group(1) if acl_match else None

            if acl_name:
                acl_output = get_and_parse_cli_output(f"show access-list {acl_name}")
                print("=" * 80)
                print(f"Access-List Configuration: {acl_name}".center(80))
                print("=" * 80)
                print(acl_output)
                print("=" * 80 + "\n")

    # Display IKE-specific configurations
    if ike_version == 'ikev2':
        ike_output = get_and_parse_cli_output("show running-config crypto ikev2")
    else:
        ike_output = get_and_parse_cli_output("show running-config crypto ikev1")

    print("=" * 80)
    print(f"Crypto {ike_version.upper()} Configuration".center(80))
    print("=" * 80)
    print(ike_output)
    print("=" * 80 + "\n")

    sysopt_output = get_and_parse_cli_output("show running-config all sysopt | include vpn")
    print("=" * 80)
    print("Sysopt Configuration (related to VPN)".center(80))
    print("=" * 80)
    print(sysopt_output)
    print("=" * 80 + "\n")

    print("NOTE: This script does not gather NAT configuration. Manual verification is required for NAT-exemption")
    print("and/or Hairpin NAT statements to ensure they are configured properly.\n")
