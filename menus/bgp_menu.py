def bgp_menu():
    menu_options = {
        "1": ("BGP Running Configuration", bgp_running_config),
        "2": ("BGP Summary", bgp_summary),
        "3": ("BGP Neighbors", bgp_neighbors),
        "4": ("BGP IPv4 Unicast", bgp_ipv4_unicast),
        "5": ("BGP CIDR-Only", bgp_cidr_only),
        "6": ("BGP Paths", bgp_paths),
        "7": ("BGP Pending Prefixes", bgp_pending_prefixes),
        "8": ("BGP RIB Failure", bgp_rib_failure),
        "9": ("BGP Get Advertised Routes", bgp_advertised_routes),
        "10": ("BGP Update-group", bgp_update_group),
        "11": ("BGP Help", bgp_help),
        "0": ("Exit", None),
    }

    while True:
        # Prepare the menu options for display (excluding hidden help shortcuts)
        options_display = {key: description for key, (description, _) in menu_options.items()}
        display_formatted_menu("BGP Menu", options_display)

        choice = input("Select an option (0-11): ").strip().lower()

        # Check if the user entered a valid option with "?" appended (e.g., "2?")
        if choice.endswith("?"):
            base_choice = choice[:-1]  # Remove "?" from input
            if base_choice in menu_options:
                description, function = menu_options[base_choice]
                if function:
                    print("\n" + "-" * 80)
                    print(f"Help for: {description}".center(80))
                    print("-" * 80)
                    function(help_requested=True)  # Call function in help mode
                else:
                    print("\n[!] Help not available for this option.")
            else:
                print("\n[!] Invalid choice. Please enter a valid number from the menu.")

        elif choice in menu_options:
            description, function = menu_options[choice]
            if function:
                print("\n" + "-" * 80)
                print(f"Accessing {description}...".center(80))
                print("-" * 80)
                function()  # Normal function execution
            else:  # Exit condition
                print("\nExiting to previous menu...")
                break
        else:
            print("\n[!] Invalid choice. Please enter a valid number from the menu.")
