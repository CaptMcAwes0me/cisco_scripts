# Description: This script retrieves and optionally displays the ARP table using 'show arp' or a filtered version.

from core.utils import get_and_parse_cli_output


def arp(suppress_output=False, help_requested=False):
    """
    Retrieves and optionally displays the ARP table using 'show arp' or a filtered version.
    If help_requested=True, it prints the help information instead.
    """

    arp_help_info = {
        'command': 'show arp',
        'description': (
            "The 'show arp' command displays the Address Resolution Protocol (ARP) table, "
            "which maps IP addresses to MAC addresses for Layer 2 communication. This is useful "
            "for troubleshooting connectivity issues, identifying MAC addresses of active devices, "
            "and verifying dynamic/static ARP entries."
        ),
        'example_output': """
FTDv# show arp
outside  14.38.117.1     f80b.cbbb.b27e    1
outside  14.38.117.97    0050.5684.f9d3    290
outside  14.38.117.123   dead.dead.dead    -
fover    1.1.1.2         0050.5684.3b31    41
        """,
        'notes': (
            "Each line represents an ARP entry with the following details:\n"
            "  - **Interface**: The interface where the ARP entry is learned.\n"
            "  - **IP Address**: The corresponding Layer 3 address.\n"
            "  - **MAC Address**: The associated Layer 2 address.\n"
            "  - **Age**: The time (in minutes) since the entry was last updated. "
            "A '-' signifies a static ARP entry."
        ),
        'related_commands': [
            {'command': 'arp', 'description': 'Adds a static ARP entry.'},
            {'command': 'clear arp', 'description': 'Clears the ARP cache.'},
            {'command': 'show arp statistics', 'description': 'Displays ARP-related statistics.'},
            {'command': 'show running-config arp', 'description': 'Shows the current ARP timeout configuration.'},
            {'command': 'show interface', 'description': 'Displays interface details, including ARP timeout values.'},
        ]
    }

    if help_requested:
        print("\n" + "-" * 80)
        print(f"📖 Help for: {arp_help_info['command']}".center(80))
        print("-" * 80)
        print(f"\nDescription:\n{arp_help_info['description']}\n")
        print("Example Output:")
        print(arp_help_info['example_output'])
        print("\nNotes:")
        print(arp_help_info['notes'])
        print("\nRelated Commands:")
        for related in arp_help_info['related_commands']:
            print(f"  - {related['command']}: {related['description']}")
        return None

    ip_filter = input("Enter an IP address to filter by (or press enter to show all): ").strip()
    command = f"show arp | include {ip_filter}" if ip_filter else "show arp"

    try:
        output = get_and_parse_cli_output(command)

        if not suppress_output:
            print("\nARP Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)

        return output

    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message


def arp_dump(suppress_output=False, help_requested=False):
    """Retrieves and optionally displays the arp using 'show arp'."""

    arp_help_info = {
        'command': 'show arp',
        'description': (
            "The 'show arp' command displays the Address Resolution Protocol (ARP) table, "
            "which maps IP addresses to MAC addresses for Layer 2 communication. This is useful "
            "for troubleshooting connectivity issues, identifying MAC addresses of active devices, "
            "and verifying dynamic/static ARP entries."
        ),
        'example_output': """
    FTDv# show arp
    outside  14.38.117.1     f80b.cbbb.b27e    1
    outside  14.38.117.97    0050.5684.f9d3    290
    outside  14.38.117.123   dead.dead.dead    -
    fover    1.1.1.2         0050.5684.3b31    41
            """,
        'notes': (
            "Each line represents an ARP entry with the following details:\n"
            "  - **Interface**: The interface where the ARP entry is learned.\n"
            "  - **IP Address**: The corresponding Layer 3 address.\n"
            "  - **MAC Address**: The associated Layer 2 address.\n"
            "  - **Age**: The time (in minutes) since the entry was last updated. "
            "A '-' signifies a static ARP entry."
        ),
        'related_commands': [
            {'command': 'arp', 'description': 'Adds a static ARP entry.'},
            {'command': 'clear arp', 'description': 'Clears the ARP cache.'},
            {'command': 'show arp statistics', 'description': 'Displays ARP-related statistics.'},
            {'command': 'show running-config arp', 'description': 'Shows the current ARP timeout configuration.'},
            {'command': 'show interface', 'description': 'Displays interface details, including ARP timeout values.'},
        ]
    }

    if help_requested:
        print("\n" + "-" * 80)
        print(f"📖 Help for: {arp_help_info['command']}".center(80))
        print("-" * 80)
        print(f"\nDescription:\n{arp_help_info['description']}\n")
        print("Example Output:")
        print(arp_help_info['example_output'])
        print("\nNotes:")
        print(arp_help_info['notes'])
        print("\nRelated Commands:")
        for related in arp_help_info['related_commands']:
            print(f"  - {related['command']}: {related['description']}")
        return None

    command = "show arp"

    try:
        output = get_and_parse_cli_output(command)

        if not suppress_output:
            print("\nARP Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)

        return output

    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message