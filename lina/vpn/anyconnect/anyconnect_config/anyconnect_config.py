from core.utils import get_and_parse_cli_output, print_section
import re


def anyconnect_config(tunnel_group):
    print("\n")
    print("-" * 80)
    print(f"*** AnyConnect Configuration for {tunnel_group} ***".center(80))

    tunnel_output = get_and_parse_cli_output(f"show running-config all tunnel-group {tunnel_group}")
    print_section(f"Tunnel Group Configuration for {tunnel_group}", tunnel_output)

    address_pool_match = re.search(r"address-pool (\S+)", tunnel_output)
    group_policy_match = re.search(r"default-group-policy (\S+)", tunnel_output)
    auth_server_match = re.search(r"authentication-server-group (\S+)", tunnel_output)

    address_pool = address_pool_match.group(1) if address_pool_match else None
    group_policy = group_policy_match.group(1) if group_policy_match else None
    auth_server = auth_server_match.group(1) if auth_server_match else None

    if group_policy:
        group_policy_output = get_and_parse_cli_output(f"show running-config all group-policy {group_policy}")
        print_section(f"Group Policy Configuration for {tunnel_group}", group_policy_output)

    if auth_server:
        if auth_server.lower() != "local":
            auth_server_output = get_and_parse_cli_output(f"show running-config aaa-server {auth_server}")
            print_section(f"AAA Server Configuration ({auth_server})", auth_server_output)
        else:
            local_user_output = get_and_parse_cli_output("show running-config username")
            print_section("Local User Configuration", local_user_output)

    split_tunnel_enabled = []
    for policy_type in ["split-tunnel-policy", "ipv6-split-tunnel-policy"]:
        if re.search(rf"(?<!ipv6-){policy_type} tunnelspecified", group_policy_output):
            split_tunnel_enabled.append(f"- {policy_type.replace('-', ' ').title()} Enabled")
            acl_match = re.search(rf"{policy_type.replace('policy', 'network-list value')} (\S+)", group_policy_output)
            if acl_match:
                acl_name = acl_match.group(1)
                acl_output = get_and_parse_cli_output(f"show access-list {acl_name}")
                print_section(f"Split-Tunnel ACL Configuration ({acl_name})", acl_output)
        elif re.search(rf"(?<!ipv6-){policy_type} tunnelall", group_policy_output):
            split_tunnel_enabled.append(f"- {policy_type.replace('-', ' ').title()} Disabled")

    if split_tunnel_enabled:
        print_section("Split-Tunnel Policy Overview", "\n".join(split_tunnel_enabled))

    vpn_filter_match = re.search(r"vpn-filter value (\S+)", group_policy_output)
    if vpn_filter_match:
        acl_name = vpn_filter_match.group(1)
        acl_output = get_and_parse_cli_output(f"show access-list {acl_name}")
        print_section(f"VPN-FILTER Configuration (ACL: {acl_name})", acl_output)
    else:
        print("*** VPN-FILTER *** [DISABLED]")
        print("-" * 80 + "\n")

    if address_pool:
        ip_pool_output = get_and_parse_cli_output(f"show running-config ip local pool {address_pool}")
        print_section(f"IP Local Pool Configuration for {tunnel_group}", ip_pool_output)

    sysopt_output = get_and_parse_cli_output("show running-config all sysopt | include vpn")
    print_section("Sysopt Configuration (related to VPN)", sysopt_output)

    print("NOTE: This script does not gather NAT configuration. Manual verification is required for NAT-exemption")
    print("and/or Hairpin NAT statements to ensure they are configured properly.\n")


def anyconnect_config_dump(suppress_output=False):
    commands = {
        "Tunnel Group": "show running-config all tunnel-group",
        "Group Policy": "show running-config all group-policy",
        "WebVPN": "show running-config all webvpn",
        "IP Local Pool": "show running-config ip local pool",
        "Sysopt": "show running-config all sysopt",
        "SSL": "show running-config all ssl"
    }

    try:
        outputs = {label: get_and_parse_cli_output(cmd) for label, cmd in commands.items()}

        if not suppress_output:
            for label, output in outputs.items():
                print_section(f"{label} Output", output)

        return outputs
    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
