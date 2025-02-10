from core.utils import get_and_parse_cli_output, print_section
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


def s2s_ikev1_policy_based_config(ip_address):
    print("\n")
    print("-" * 80)
    print(f"*** IKEv1 Policy-Based Configuration for {ip_address} ***".center(80))

    tunnel_output = get_and_parse_cli_output(f"show running-config tunnel-group {ip_address}")
    print_section(f"Tunnel Group Configuration for {ip_address}", tunnel_output)

    group_policy_match = re.search(r"default-group-policy (\S+)", tunnel_output)
    if group_policy_match:
        group_policy = group_policy_match.group(1)
        group_policy_output = get_and_parse_cli_output(f"show running-config group-policy {group_policy}")
        print_section(f"Group Policy Configuration for {group_policy}", group_policy_output)

    crypto_map_output = get_and_parse_cli_output(f"show running-config crypto map | include {ip_address}")
    print_section(f"Crypto Map Configuration for {ip_address}", crypto_map_output)

    crypto_map_match = re.search(r"crypto map (\S+) (\d+) set peer", crypto_map_output)
    if crypto_map_match:
        crypto_map_name, crypto_map_number = crypto_map_match.groups()
        crypto_map_details = get_and_parse_cli_output(
            f"show running-config crypto map | include {crypto_map_name} {crypto_map_number}"
        )
        print_section(f"Detailed Crypto Map Configuration: {crypto_map_name} {crypto_map_number}", crypto_map_details)

        acl_match = re.search(r"match address (\S+)", crypto_map_details)
        if acl_match:
            acl_name = acl_match.group(1)
            acl_output = get_and_parse_cli_output(f"show access-list {acl_name}")
            print_section(f"Access-List Configuration: {acl_name}", acl_output)

            transform_set_match = re.search(r"set ikev1 transform-set (\S+)", crypto_map_details)
            if transform_set_match:
                transform_set = transform_set_match.group(1)
                transform_set_output = get_and_parse_cli_output(
                    f"show running-config crypto | include crypto ipsec ikev1 transform-set {transform_set}"
                )
                print_section(f"Transform-Set Configuration: {transform_set}", transform_set_output)

    ikev1_output = get_and_parse_cli_output("show running-config all crypto ikev1")
    print_section("IKEv1 Configuration", ikev1_output)
    sysopt_output = get_and_parse_cli_output("show running-config all sysopt | include vpn")
    print_section("Sysopt Configuration (related to VPN)", sysopt_output)

    print("NOTE: This script does not gather NAT configuration. Manual verification is required for NAT-exemption")
    print("and/or Hairpin NAT statements to ensure they are configured properly.\n")


def s2s_ikev1_vti_config(ip_address):
    print("\n")
    print("-" * 80)
    print(f"*** IKEv1 VTI Configuration for {ip_address} ***".center(80))

    tunnel_output = get_and_parse_cli_output(f"show running-config tunnel-group {ip_address}")
    print_section(f"Tunnel Group Configuration for {ip_address}", tunnel_output)

    group_policy_match = re.search(r"default-group-policy (\S+)", tunnel_output)
    if group_policy_match:
        group_policy = group_policy_match.group(1)
        group_policy_output = get_and_parse_cli_output(f"show running-config group-policy {group_policy}")
        print_section(f"Group Policy Configuration for {group_policy}", group_policy_output)

    interface_output = get_and_parse_cli_output("show running-config interface | begin Tunnel")
    interface_sections = re.findall(r"interface (Tunnel\S+)([\s\S]*?)(?=^interface|\Z)", interface_output, re.MULTILINE)

    for interface, config in interface_sections:
        if re.search(rf"tunnel destination {re.escape(ip_address)}", config):
            tunnel_interface = interface
            tunnel_interface_output = get_and_parse_cli_output(f"show running-config interface {tunnel_interface}")
            print_section(f"Tunnel Interface Configuration for {tunnel_interface}", tunnel_interface_output)

            ipsec_profile_match = re.search(r"tunnel protection ipsec profile (\S+)", tunnel_interface_output)
            if ipsec_profile_match:
                ipsec_profile = ipsec_profile_match.group(1)
                ipsec_profile_output = get_and_parse_cli_output(
                    f"show running-config crypto | include {ipsec_profile}|set ikev1 transform-set"
                )
                print_section(f"IPSec Profile Configuration: {ipsec_profile}", ipsec_profile_output)

                transform_set_match = re.search(r"set ikev1 transform-set (\S+)", ipsec_profile_output)
                if transform_set_match:
                    transform_set = transform_set_match.group(1)
                    transform_set_output = get_and_parse_cli_output(
                        f"show running-config crypto | include crypto ipsec ikev1 transform-set {transform_set}"
                    )
                    print_section(f"Transform-Set Configuration: {transform_set}", transform_set_output)

            nameif_match = re.search(r"nameif (\S+)", tunnel_interface_output)
            if nameif_match:
                nameif = nameif_match.group(1)
                route_output = get_and_parse_cli_output(f"show running-config route | include {nameif}")
                print_section(f"Route Configuration for {nameif}", route_output)

    ikev1_output = get_and_parse_cli_output("show running-config all crypto ikev1")
    print_section("IKEv1 Configuration", ikev1_output)
    sysopt_output = get_and_parse_cli_output("show running-config all sysopt | include vpn")
    print_section("Sysopt Configuration (related to VPN)", sysopt_output)

    print("NOTE: This script does not gather NAT configuration. Manual verification is required for NAT-exemption")
    print("and/or Hairpin NAT statements to ensure they are configured properly.\n")


def s2s_ikev2_policy_based_config(ip_address):
    print("\n")
    print("-" * 80)
    print(f"*** IKEv2 Policy-Based Configuration for {ip_address} ***".center(80))

    tunnel_output = get_and_parse_cli_output(f"show running-config tunnel-group {ip_address}")
    print_section(f"Tunnel Group Configuration for {ip_address}", tunnel_output)

    group_policy_match = re.search(r"default-group-policy (\S+)", tunnel_output)
    if group_policy_match:
        group_policy = group_policy_match.group(1)
        group_policy_output = get_and_parse_cli_output(f"show running-config group-policy {group_policy}")
        print_section(f"Group Policy Configuration for {group_policy}", group_policy_output)

    crypto_map_output = get_and_parse_cli_output(f"show running-config crypto map | include {ip_address}")
    print_section(f"Crypto Map Configuration for {ip_address}", crypto_map_output)

    crypto_map_match = re.search(r"crypto map (\S+) (\d+) set peer", crypto_map_output)
    if crypto_map_match:
        crypto_map_name, crypto_map_number = crypto_map_match.groups()
        crypto_map_details = get_and_parse_cli_output(
            f"show running-config crypto map | include crypto map {crypto_map_name} {crypto_map_number}"
        )
        print_section(f"Detailed Crypto Map Configuration: {crypto_map_name} {crypto_map_number}", crypto_map_details)

        acl_match = re.search(r"match address (\S+)", crypto_map_details)
        if acl_match:
            acl_name = acl_match.group(1)
            acl_output = get_and_parse_cli_output(f"show access-list {acl_name}")
            print_section(f"Access-List Configuration: {acl_name}", acl_output)

        ipsec_proposal_match = re.search(r"set ikev2 ipsec-proposal (\S+)", crypto_map_details)
        if ipsec_proposal_match:
            ipsec_proposal = ipsec_proposal_match.group(1)
            ipsec_proposal_output = get_and_parse_cli_output(
                f"show running-config crypto | include crypto ipsec ikev2 ipsec-proposal {ipsec_proposal}|protocol esp encryption|protocol esp integrity"
            )
            print_section(f"IPSec Proposal Configuration: {ipsec_proposal}", ipsec_proposal_output)

    ikev2_output = get_and_parse_cli_output("show running-config all crypto ikev2")
    print_section("IKEv2 Configuration", ikev2_output)
    sysopt_output = get_and_parse_cli_output("show running-config all sysopt | include vpn")
    print_section("Sysopt Configuration (related to VPN)", sysopt_output)

    print("NOTE: This script does not gather NAT configuration. Manual verification is required for NAT-exemption")
    print("and/or Hairpin NAT statements to ensure they are configured properly.\n")


def s2s_ikev2_vti_config(ip_address):
    print("\n")
    print("-" * 80)
    print(f"*** IKEv2 VTI Configuration for {ip_address} ***".center(80))

    tunnel_output = get_and_parse_cli_output(f"show running-config tunnel-group {ip_address}")
    print_section(f"Tunnel Group Configuration for {ip_address}", tunnel_output)

    group_policy_match = re.search(r"default-group-policy (\S+)", tunnel_output)
    if group_policy_match:
        group_policy = group_policy_match.group(1)
        group_policy_output = get_and_parse_cli_output(f"show running-config group-policy {group_policy}")
        print_section(f"Group Policy Configuration for {group_policy}", group_policy_output)

    interface_output = get_and_parse_cli_output("show running-config interface | begin Tunnel")
    interface_sections = re.findall(r"interface (Tunnel\S+)([\s\S]*?)(?=^interface|\Z)", interface_output, re.MULTILINE)

    for interface, config in interface_sections:
        if re.search(rf"tunnel destination {re.escape(ip_address)}", config):
            tunnel_interface = interface
            tunnel_interface_output = get_and_parse_cli_output(f"show running-config interface {tunnel_interface}")
            print_section(f"Tunnel Interface Configuration for {tunnel_interface}", tunnel_interface_output)

            ipsec_profile_match = re.search(r"tunnel protection ipsec profile (\S+)", tunnel_interface_output)
            if ipsec_profile_match:
                ipsec_profile = ipsec_profile_match.group(1)
                ipsec_profile_output = get_and_parse_cli_output(
                    f"show running-config crypto | include crypto ipsec profile {ipsec_profile}|set ikev2 ipsec-proposal"
                )
                print_section(f"IPSec Profile Configuration: {ipsec_profile}", ipsec_profile_output)

                ipsec_proposal_match = re.search(r"set ikev2 ipsec-proposal (\S+)", ipsec_profile_output)
                if ipsec_proposal_match:
                    ipsec_proposal = ipsec_proposal_match.group(1)
                    ipsec_proposal_output = get_and_parse_cli_output(
                        f"show running-config crypto | include crypto ipsec ikev2 ipsec-proposal {ipsec_proposal}|protocol esp encryption|protocol esp integrity"
                    )
                    print_section(f"IPSec Proposal Configuration: {ipsec_proposal}", ipsec_proposal_output)

            nameif_match = re.search(r"nameif (\S+)", tunnel_interface_output)
            if nameif_match:
                nameif = nameif_match.group(1)
                route_output = get_and_parse_cli_output(f"show running-config route | include {nameif}")
                print_section(f"Route Configuration for {nameif}", route_output)

    ikev2_output = get_and_parse_cli_output("show running-config all crypto ikev2")
    print_section("IKEv2 Configuration", ikev2_output)
    sysopt_output = get_and_parse_cli_output("show running-config all sysopt | include vpn")
    print_section("Sysopt Configuration (related to VPN)", sysopt_output)

    print("NOTE: This script does not gather NAT configuration. Manual verification is required for NAT-exemption")
    print("and/or Hairpin NAT statements to ensure they are configured properly.\n")

