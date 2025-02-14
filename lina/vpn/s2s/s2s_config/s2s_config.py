from core.utils import get_and_parse_cli_output, print_section
import re


def s2s_ikev1_policy_based_config(ip_address, help_requested=False):
    """Retrieves IKEv1 policy-based configuration details for a given peer IP.
       If help_requested=True, it prints the help information instead.
    """

    help_info = {
        'command': 'show running-config tunnel-group <peer_ip>',
        'description': (
            "Displays the configuration of an IKEv1 policy-based Site-to-Site VPN tunnel. "
            "Includes tunnel-group settings, crypto map, access lists, and transform sets."
        ),
        'example_output': """
tunnel-group 192.168.1.1 type ipsec-l2l
tunnel-group 192.168.1.1 ipsec-attributes
 peer-id-validate nocheck
 isakmp keepalive threshold 10 retry 2
 default-group-policy GroupPolicy1
crypto map outside_map 1 set peer 192.168.1.1
crypto map outside_map 1 match address ACL_VPN
crypto map outside_map 1 set ikev1 transform-set TS1
        """
    }

    # If help is requested, display it and return
    if help_requested:
        print("\n" + "-" * 80)
        print(f"Help for: {help_info['command']}".center(80))
        print("-" * 80)
        print(f"\n{help_info['description']}\n")
        print("Example Output:")
        print(help_info['example_output'])
        return None  # No actual command execution

    # Execute the actual configuration retrieval
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

    ikev1_output = get_and_parse_cli_output("show running-config crypto ikev1")
    print_section("IKEv1 Configuration", ikev1_output)
    sysopt_output = get_and_parse_cli_output("show running-config all sysopt | include vpn")
    print_section("Sysopt Configuration (related to VPN)", sysopt_output)

    print("NOTE: This script does not gather NAT configuration. Manual verification is required for NAT-exemption")
    print("and/or Hairpin NAT statements to ensure they are configured properly.\n")


def s2s_ikev1_vti_config(ip_address, help_requested=False):
    """Retrieves IKEv1 VTI configuration details for a given peer IP.
       If help_requested=True, it prints the help information instead.
    """

    help_info = {
        'command': 'show running-config interface TunnelX | include tunnel destination <peer_ip>',
        'description': (
            "Displays the configuration of an IKEv1 Virtual Tunnel Interface (VTI) for a given peer. "
            "Includes tunnel-group settings, interface configurations, IPSec profile details, and route settings."
        ),
        'example_output': """
interface Tunnel10
 nameif vti10
 tunnel source GigabitEthernet0/0
 tunnel destination 192.168.1.1
 tunnel protection ipsec profile IKEv1_PROFILE
crypto ipsec profile IKEv1_PROFILE
 set ikev1 transform-set TRANSFORM1
        """
    }

    # If help is requested, display it and return
    if help_requested:
        print("\n" + "-" * 80)
        print(f"Help for: {help_info['command']}".center(80))
        print("-" * 80)
        print(f"\n{help_info['description']}\n")
        print("Example Output:")
        print(help_info['example_output'])
        return None  # No actual command execution

    # Execute the actual configuration retrieval
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

    ikev1_output = get_and_parse_cli_output("show running-config crypto ikev1")
    print_section("IKEv1 Configuration", ikev1_output)
    sysopt_output = get_and_parse_cli_output("show running-config all sysopt | include vpn")
    print_section("Sysopt Configuration (related to VPN)", sysopt_output)

    print("NOTE: This script does not gather NAT configuration. Manual verification is required for NAT-exemption")
    print("and/or Hairpin NAT statements to ensure they are configured properly.\n")


def s2s_ikev2_policy_based_config(ip_address, help_requested=False):
    """Retrieves IKEv2 Policy-Based configuration details for a given peer IP.
       If help_requested=True, it prints the help information instead.
    """

    # Help Information
    s2s_ikev2_policy_based_config_help = {
        'command': 'show running-config crypto map | include <peer_ip>',
        'description': (
            "Displays the policy-based VPN configuration for a specified IKEv2 peer. "
            "Includes tunnel-group settings, crypto map entries, access-list rules, "
            "IPSec proposal settings, and sysopt configurations."
        ),
        'example_output': """
crypto map outside_map 10 match address ACL_VPN
crypto map outside_map 10 set peer 192.168.1.1
crypto map outside_map 10 set ikev2 ipsec-proposal AES-GCM
crypto map outside_map interface outside
        """
    }

    # If help is requested, print help content and exit the function
    if help_requested:
        print("\n" + "-" * 80)
        print(f"Help for: {s2s_ikev2_policy_based_config_help['command']}".center(80))
        print("-" * 80)
        print(f"\n{s2s_ikev2_policy_based_config_help['description']}\n")
        print("Example Output:")
        print(s2s_ikev2_policy_based_config_help['example_output'])
        return None  # No actual command execution

    # Normal function execution
    if ip_address is None:
        print("[!] Error: No IP address provided.")
        return None

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

    ikev2_output = get_and_parse_cli_output("show running-config crypto ikev2")
    print_section("IKEv2 Configuration", ikev2_output)
    sysopt_output = get_and_parse_cli_output("show running-config all sysopt | include vpn")
    print_section("Sysopt Configuration (related to VPN)", sysopt_output)

    print("NOTE: This script does not gather NAT configuration. Manual verification is required for NAT-exemption")
    print("and/or Hairpin NAT statements to ensure they are configured properly.\n")


def s2s_ikev2_vti_config(ip_address, help_requested=False):
    """Retrieves IKEv2 VTI configuration details for a given peer IP.
       If help_requested=True, it prints the help information instead.
    """

    # Help Information
    s2s_ikev2_vti_config_help = {
        'command': 'show running-config interface | begin Tunnel',
        'description': (
            "Displays the IKEv2 VTI (Virtual Tunnel Interface) configuration for a specified peer IP. "
            "Includes tunnel-group settings, interface configurations, IPsec profile details, "
            "IPsec proposal settings, and sysopt configurations."
        ),
        'example_output': """
interface Tunnel100
 nameif VTI100
 ip address 192.168.10.1 255.255.255.252
 tunnel source GigabitEthernet0/0
 tunnel destination 203.0.113.2
 tunnel mode ipsec ipv4
 tunnel protection ipsec profile VTI_PROFILE
crypto ipsec profile VTI_PROFILE
 set ikev2 ipsec-proposal AES-GCM
        """
    }

    # If help is requested, print help content and exit the function
    if help_requested:
        print("\n" + "-" * 80)
        print(f"Help for: {s2s_ikev2_vti_config_help['command']}".center(80))
        print("-" * 80)
        print(f"\n{s2s_ikev2_vti_config_help['description']}\n")
        print("Example Output:")
        print(s2s_ikev2_vti_config_help['example_output'])
        return None  # No actual command execution

    # Normal function execution
    if ip_address is None:
        print("[!] Error: No IP address provided.")
        return None

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

    ikev2_output = get_and_parse_cli_output("show running-config crypto ikev2")
    print_section("IKEv2 Configuration", ikev2_output)
    sysopt_output = get_and_parse_cli_output("show running-config all sysopt | include vpn")
    print_section("Sysopt Configuration (related to VPN)", sysopt_output)

    print("NOTE: This script does not gather NAT configuration. Manual verification is required for NAT-exemption")
    print("and/or Hairpin NAT statements to ensure they are configured properly.\n")
