from core.utils import get_and_parse_cli_output
import re


def anyconnect_config(tunnel_group):
    """
    Gathers and displays configuration details for the selected AnyConnect tunnel group.
    """
    # Step 1: Gather and print tunnel-group configuration
    print("-" * 80)
    print("Tunnel Group Configuration:")
    print("-" * 80)
    command = f"show running-config tunnel-group {tunnel_group}"
    output = get_and_parse_cli_output(command)
    print(output)
    print("-" * 80)
    print("-" * 80)

    # Step 2: Extract address-pool and default-group-policy
    address_pool_match = re.search(r"address-pool (\S+)", output)
    group_policy_match = re.search(r"default-group-policy (\S+)", output)

    address_pool = address_pool_match.group(1) if address_pool_match else None
    group_policy = group_policy_match.group(1) if group_policy_match else None

    if group_policy:
        # Step 3: Show group-policy configuration
        print("-" * 80)
        print("Group Policy Configuration:")
        print("-" * 80)
        group_policy_cmd = f"show running-config group-policy {group_policy}"
        group_policy_output = get_and_parse_cli_output(group_policy_cmd)
        print(group_policy_output)
        print("-" * 80)
        print("-" * 80)

        # Step 4: Check for split-tunnel-policy
        for policy_type in ["split-tunnel-policy", "ipv6-split-tunnel-policy"]:
            if re.search(rf"(?<!ipv6-){policy_type} tunnelspecified", group_policy_output):
                print(f"{policy_type} enabled")

                # Step 5: Extract ACL name and show access-list
                acl_match = re.search(rf"{policy_type.replace('policy', 'network-list value')} (\S+)", group_policy_output)
                if acl_match:
                    acl_name = acl_match.group(1)
                    acl_command = f"show access-list {acl_name}"
                    acl_output = get_and_parse_cli_output(acl_command)
                    print("-" * 80)
                    print("Access List Configuration:")
                    print("-" * 80)
                    print(acl_output)
                    print("-" * 80)
                    print("-" * 80)
            elif re.search(rf"(?<!ipv6-){policy_type} tunnelall", group_policy_output):
                print(f"{policy_type} disabled")
                print("-" * 80)
                print("-" * 80)

        # Step 5.1: Check for vpn-filter and show access-list
        vpn_filter_match = re.search(r"vpn-filter value (\S+)", group_policy_output)
        if vpn_filter_match:
            acl_name = vpn_filter_match.group(1)
            print(f"vpn-filter enabled (ACL: {acl_name})")
            acl_command = f"show access-list {acl_name}"
            acl_output = get_and_parse_cli_output(acl_command)
            print("-" * 80)
            print("VPN Filter Configuration:")
            print("-" * 80)
            print(acl_output)
            print("-" * 80)
            print("-" * 80)
        else:
            print("vpn-filter disabled")
            print("-" * 80)
            print("-" * 80)

    if address_pool:
        # Show IP local pool configuration
        print("-" * 80)
        print("IP Local Pool Configuration:")
        print("-" * 80)
        ip_pool_cmd = f"show running-config ip local pool {address_pool}"
        ip_pool_output = get_and_parse_cli_output(ip_pool_cmd)
        print(ip_pool_output)
        print("-" * 80)
        print("-" * 80)

    # Step 6: Gather and print sysopt configuration related to VPN
    print("-" * 80)
    print("Sysopt Configuration (related to VPN):")
    print("-" * 80)
    sysopt_cmd = "show running-config all sysopt | include vpn"
    sysopt_output = get_and_parse_cli_output(sysopt_cmd)
    print(sysopt_output)
    print("-" * 80)
    print("-" * 80)

    # Note about NAT configuration
    print("\nNOTE: This script does not gather NAT configuration. Manual verification is required for NAT-exemption "
          "and/or Hairpin NAT statements to ensure they are configured properly.")
