from core.utils import get_and_parse_cli_output
import re


def anyconnect_config(tunnel_group):
    """
    Gathers and displays configuration details for the selected AnyConnect tunnel group.
    """
    # Step 1: Gather and print tunnel-group configuration
    print("=" * 80)
    print(f"Tunnel Group {tunnel_group} Configuration".center(80))
    print("=" * 80)
    command = f"show running-config all tunnel-group {tunnel_group}"
    output = get_and_parse_cli_output(command)
    print(output)
    print("=" * 80 + "\n")

    # Step 2: Extract address-pool and default-group-policy
    address_pool_match = re.search(r"address-pool (\S+)", output)
    group_policy_match = re.search(r"default-group-policy (\S+)", output)

    address_pool = address_pool_match.group(1) if address_pool_match else None
    group_policy = group_policy_match.group(1) if group_policy_match else None

    if group_policy:
        # Step 3: Show group-policy configuration
        print("=" * 80)
        print(f"Group Policy Configuration for {tunnel_group}".center(80))
        print("=" * 80)
        group_policy_cmd = f"show running-config all group-policy {group_policy}"
        group_policy_output = get_and_parse_cli_output(group_policy_cmd)
        print(group_policy_output)
        print("=" * 80 + "\n")

        # Step 4: Check for split-tunnel-policy
        for policy_type in ["split-tunnel-policy", "ipv6-split-tunnel-policy"]:
            if re.search(rf"(?<!ipv6-){policy_type} tunnelspecified", group_policy_output):
                print(f"{policy_type.upper()} ENABLED")
                print("-" * 80)

                # Step 5: Extract ACL name and show access-list
                acl_match = re.search(rf"{policy_type.replace('policy', 'network-list value')} (\S+)", group_policy_output)
                if acl_match:
                    acl_name = acl_match.group(1)
                    acl_command = f"show access-list {acl_name}"
                    acl_output = get_and_parse_cli_output(acl_command)
                    print("=" * 80)
                    print(f"Access List Configuration ({acl_name})".center(80))
                    print("=" * 80)
                    print(acl_output)
                    print("=" * 80 + "\n")
            elif re.search(rf"(?<!ipv6-){policy_type} tunnelall", group_policy_output):
                print(f"{policy_type.upper()} DISABLED")
                print("-" * 80 + "\n")

        # Step 5.1: Check for vpn-filter and show access-list
        vpn_filter_match = re.search(r"vpn-filter value (\S+)", group_policy_output)
        if vpn_filter_match:
            acl_name = vpn_filter_match.group(1)
            print("=" * 80)
            print(f"VPN-FILTER ENABLED (ACL: {acl_name})")
            print("=" * 80)
            acl_command = f"show access-list {acl_name}"
            acl_output = get_and_parse_cli_output(acl_command)
            print(acl_output)
            print("=" * 80 + "\n")
        else:
            print("VPN-FILTER DISABLED")
            print("-" * 80 + "\n")

    if address_pool:
        # Show IP local pool configuration
        print("=" * 80)
        print(f"IP Local Pool Configuration for {tunnel_group}".center(80))
        print("=" * 80)
        ip_pool_cmd = f"show running-config ip local pool {address_pool}"
        ip_pool_output = get_and_parse_cli_output(ip_pool_cmd)
        print(ip_pool_output)
        print("=" * 80 + "\n")

    # Step 6: Gather and print sysopt configuration related to VPN
    print("=" * 80)
    print("Sysopt Configuration (related to VPN)".center(80))
    print("=" * 80)
    sysopt_cmd = "show running-config all sysopt | include vpn"
    sysopt_output = get_and_parse_cli_output(sysopt_cmd)
    print(sysopt_output)
    print("=" * 80 + "\n")

    # Note about NAT configuration
    print("NOTE: This script does not gather NAT configuration. Manual verification is required for NAT-exemption "
          "and/or Hairpin NAT statements to ensure they are configured properly.")
    print("\n")


def anyconnect_config_dump(suppress_output=False):
    """Retrieves and optionally displays the full AnyConnect configuration."""

    command1 = "show running-config all tunnel-group"
    command2 = "show running-config all group-policy"
    command3 = "show running-config all webvpn"
    command4 = "show running-config ip local pool"
    command5 = "show running-config all sysopt"
    command6 = "show running-config all ssl"

    try:
        output1 = get_and_parse_cli_output(command1)
        output2 = get_and_parse_cli_output(command2)
        output3 = get_and_parse_cli_output(command3)
        output4 = get_and_parse_cli_output(command4)
        output5 = get_and_parse_cli_output(command5)
        output6 = get_and_parse_cli_output(command6)

        if not suppress_output:
            print("\n" + "Tunnel Group Output:".center(80))
            print("-" * 80)
            print(output1)
            print("-" * 80)

            print("\n" + "Group Policy Output:".center(80))
            print("-" * 80)
            print(output2)
            print("-" * 80)

            print("\n" + "WebVPN Output:".center(80))
            print("-" * 80)
            print(output3)
            print("-" * 80)

            print("\n" + "IP Local Pool Output:".center(80))
            print("-" * 80)
            print(output4)
            print("-" * 80)

            print("\n" + "Sysopt Output:".center(80))
            print("-" * 80)
            print(output5)
            print("-" * 80)

            print("\n" + "SSL Output:".center(80))
            print("-" * 80)
            print(output6)
            print("-" * 80)

        return output1, output2, output3, output4, output5, output6

    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)

