# Description: This script retrieves and optionally displays service-policy statistics using 'show service-policy'.

from core.utils import get_and_parse_cli_output

def service_policy(suppress_output=False, help_requested=False):
    """
    Retrieves and optionally displays the Service-Policy information using 'show service-policy'.
    If help_requested=True, it prints the help information instead.
    """

    service_policy_help_info = {
        'command': 'show service-policy',
        'description': (
            "The 'show service-policy' command displays statistics and details for applied policy maps, including "
            "how traffic is classified, prioritized, and shaped. This helps administrators monitor Quality of Service (QoS) "
            "and firewall policy enforcement."
        ),
        'example_output': """
FTDv# show service-policy

Global policy:
  Service-policy: global_policy
    Class-map: inspection_default
      Inspect: dns preset_dns_map, packet 100, drop 2
      Inspect: ftp, packet 50, drop 0
      Inspect: http, packet 500, drop 10
      Inspect: icmp, packet 300, drop 5
      Inspect: pop3, packet 20, drop 1
      Inspect: esmtp, packet 15, drop 0
      Inspect: imap, packet 12, drop 0
      Inspect: sip, packet 200, drop 3
    Class-map: qos_default
      Police: cir 10000000 bps, bc 312500 bytes
        conformed 1200000 packets, exceeded 3500 packets
        conformed 7500000000 bytes, exceeded 15000000 bytes
      Drop: 5000 packets
        """,
        'notes': (
            "Key fields in the output include:\n"
            "  - **Global Policy**: The default global service-policy applied across the firewall.\n"
            "  - **Class-map Inspection**: Displays protocol-specific inspections (e.g., HTTP, SIP, DNS).\n"
            "  - **Police**: Defines rate-limiting rules and displays conformed/exceeded packets.\n"
            "  - **Drop**: Indicates the number of dropped packets due to policing or firewall restrictions.\n"
            "  - **QoS Policing**: Monitors traffic shaping and rate limits applied to traffic classes.\n"
        ),
        'related_commands': [
            {'command': 'show service-policy interface', 'description': 'Displays service policies per interface.'},
            {'command': 'show service-policy inspect', 'description': 'Shows packet inspection statistics.'},
            {'command': 'show run policy-map', 'description': 'Displays the configured policy maps.'},
        ]
    }

    if help_requested:
        print("\n" + "-" * 80)
        print(f"📖 Help for: {service_policy_help_info['command']}".center(80))
        print("-" * 80)
        print(f"\nDescription:\n{service_policy_help_info['description']}\n")
        print("Example Output:")
        print(service_policy_help_info['example_output'])
        print("\nNotes:")
        print(service_policy_help_info['notes'])
        print("\nRelated Commands:")
        for related in service_policy_help_info['related_commands']:
            print(f"  - {related['command']}: {related['description']}")
        return None

    command = "show service-policy"

    try:
        output = get_and_parse_cli_output(command)

        if not suppress_output:
            print("\nService-Policy Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)

        return output

    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
