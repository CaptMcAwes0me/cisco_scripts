from core.utils import get_and_parse_cli_output, display_formatted_menu
from menus.anyconnect_menu import anyconnect_menu


def anyconnect_tunnel_groups(help_requested=False):
    """
    Executes the 'show running-config tunnel-group | include type remote-access' command,
    parses the output, and displays a numbered menu for the user to select a tunnel group.

    Returns the selected tunnel group name or all tunnel groups if Enter is pressed.
    """

    anyconnect_menu_help_info = {
            'command': 'AnyConnect (Secure Client) VPN Menu',
            'description': (
                "The AnyConnect VPN Menu provides options for managing and troubleshooting "
                "remote-access VPNs using Cisco AnyConnect (Secure Client). Users can view tunnel "
                "group configurations, check session details, analyze SSL settings, and debug VPN-related "
                "issues such as authentication failures and certificate errors."
            ),
            'example_output': """
================================================================================
================= AnyConnect Menu - Selected Group: test_group =================
================================================================================
1) AnyConnect Configuration
2) VPN Session Database
3) Crypto CA Data
4) SSL Data
5) Crypto Accelerator Data
6) AnyConnect Help
0) Exit
================================================================================
            """

    }
    if help_requested:
        print("\n" + "=" * 80)
        print(f"📖 Help for: {anyconnect_menu_help_info['command']}".center(80))
        print("=" * 80)
        print(f"\n{anyconnect_menu_help_info['description']}\n")
        print("Example Output:")
        print(anyconnect_menu_help_info['example_output'])
        return None

    command = "show running-config tunnel-group | include type remote-access"
    cli_output = get_and_parse_cli_output(command)

    tunnel_groups = []

    for line in cli_output.splitlines():
        line = line.strip()
        if line.startswith("tunnel-group"):
            parts = line.split()
            if len(parts) >= 2:
                tunnel_groups.append(parts[1])

    if not tunnel_groups:
        print("No tunnel groups found.")
        return None

    menu_options = {str(index + 1): group for index, group in enumerate(tunnel_groups)}
    menu_options["0"] = "Exit"

    while True:
        display_formatted_menu("Select a Tunnel Group (press Enter to select all)", menu_options)
        choice = input("Select an option (0-{} or Enter for all): ".format(len(tunnel_groups))).strip()

        if choice == "0":
            print("\nExiting to previous menu...")
            return None
        elif choice == "":
            print("\nSelected All Tunnel Groups")
            selected_groups = tunnel_groups
            anyconnect_menu("All", selected_groups)  # Fixed: passing selected_groups
            return selected_groups
        elif choice in menu_options:
            selected_group = menu_options[choice]
            print(f"\nSelected Tunnel Group: {selected_group}")
            anyconnect_menu(selected_group)
            return selected_group
        else:
            print("\n[!] Invalid choice. Please enter a valid option.")
