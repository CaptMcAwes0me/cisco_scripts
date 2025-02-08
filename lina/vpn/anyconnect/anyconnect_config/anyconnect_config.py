from core.utils import get_and_parse_cli_output
import re


def anyconnect_config(tunnel_group):
    """
    Gathers and displays configuration details for the selected AnyConnect tunnel group.
    """
    # Step 1: Gather and print tunnel-group configuration
    command = f"show running-config tunnel-group {tunnel_group}"
    output = get_and_parse_cli_output(command)
    print("-" * 80)
    print(output)
    print("-" * 80)

    # Step 2: Extract address-pool and default-group-policy
    address_pool_match = re.search(r"address-pool (\S+)", output)
    group_policy_match = re.search(r"default-group-policy (\S+)", output)

    address_pool = address_pool_match.group(1) if address_pool_match else None
    group_policy = group_policy_match.group(1) if group_policy_match else None

    if group_policy:
        # Step 3: Show group-policy configuration
        group_policy_cmd = f"show running-config group-policy {group_policy}"
        group_policy_output = get_and_parse_cli_output(group_policy_cmd)
        print("-" * 80)
        print(group_policy_output)
        print("-" * 80)

        # Step 4: Check for split-tunnel-policy
        if re.search(r"(?<!ipv6-)split-tunnel-policy tunnelspecified", group_policy_output):
            print("Split tunneling enabled")

            # Step 5: Extract ACL name and show access-list
            acl_match = re.search(r"split-tunnel-network-list value (\S+)", group_policy_output)
            if acl_match:
                acl_name = acl_match.group(1)
                acl_command = f"show access-list {acl_name}"
                acl_output = get_and_parse_cli_output(acl_command)
                print("-" * 80)
                print(acl_output)
                print("-" * 80)
        elif re.search(r"(?<!ipv6-)split-tunnel-policy tunnelall", group_policy_output):
            print("Split tunneling disabled")

    if address_pool:
        # Show IP local pool configuration
        ip_pool_cmd = f"show running-config ip local pool {address_pool}"
        ip_pool_output = get_and_parse_cli_output(ip_pool_cmd)
        print("-" * 80)
        print(ip_pool_output)
        print("-" * 80)
