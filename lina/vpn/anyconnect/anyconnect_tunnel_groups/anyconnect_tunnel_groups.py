from core.utils import get_and_parse_cli_output, display_formatted_menu


def anyconnect_tunnel_groups():
    """
    Executes the 'show running-config tunnel-group | include type remote-access' command,
    parses the output, and displays a numbered menu for the user to select a tunnel group.

    Returns the selected tunnel group name.
    """
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
        display_formatted_menu("Select a Tunnel Group", menu_options)
        choice = input("Select an option (0-{}): ".format(len(tunnel_groups))).strip()

        if choice == "0":
            print("\nExiting to previous menu...")
            return None
        elif choice in menu_options:
            selected_group = menu_options[choice]
            print(f"\nSelected Tunnel Group: {selected_group}")
            return selected_group
        else:
            print("\n[!] Invalid choice. Please enter a valid option.")
