from core.utils import display_formatted_menu
from lina.logging_and_monitoring.snmp.snmp_config.snmp_config import snmp_config
from lina.logging_and_monitoring.snmp.snmp_engineid.snmp_engineid import snmp_engineid
from lina.logging_and_monitoring.snmp.snmp_group.snmp_group import snmp_group
from lina.logging_and_monitoring.snmp.snmp_host.snmp_host import snmp_host
from lina.logging_and_monitoring.snmp.snmp_user.snmp_user import snmp_user
from lina.logging_and_monitoring.snmp.snmp_stats.snmp_stats import snmp_stats
from lina.logging_and_monitoring.snmp.snmp_help.snmp_help import snmp_help


def snmp_menu(help_requested=False):
    """Displays a menu for SNMP-related tasks.
       Supports 'X?' functionality to display help for each menu option.
    """

    snmp_menu_help_info = {
        'command': 'SNMP Menu',
        'description': (
            "The SNMP Menu provides options for configuring, monitoring, and troubleshooting "
            "Simple Network Management Protocol (SNMP). This includes SNMP engine settings, "
            "groups, hosts, user configurations, and statistics. These commands help ensure "
            "proper SNMP functionality and diagnose connectivity issues with SNMP servers."
        ),
        'troubleshooting_steps': [
            "🔹 **Step 1: Verify SNMP Configuration**",
            "   - Run `SNMP Config` to ensure SNMP is enabled and configured properly.",
            "   - Check for correct community strings or SNMPv3 authentication settings.",
            "🔹 **Step 2: Validate SNMP Engine and ID**",
            "   - Use `SNMP Engine ID` to verify the local SNMP engine identification.",
            "   - Ensure that the Engine ID matches what is expected by the SNMP server.",
            "🔹 **Step 3: Check SNMP Groups and Users**",
            "   - Run `SNMP Group` to review group permissions and assigned access levels.",
            "   - Use `SNMP User` to validate SNMPv3 user authentication and privileges.",
            "🔹 **Step 4: Confirm SNMP Host Configuration**",
            "   - Run `SNMP Host` to check whether the correct SNMP manager IPs are configured.",
            "   - If an SNMP trap destination is missing, add it and test connectivity.",
            "🔹 **Step 5: Monitor SNMP Traffic and Stats**",
            "   - Use `SNMP Stats` to verify if SNMP requests and traps are being sent/received.",
            "   - If there are errors or dropped messages, adjust polling intervals or check logs."
        ],
        'example_output': """
================================================================================
                                   SNMP Menu
================================================================================
1) SNMP Configuration
2) SNMP Engine ID
3) SNMP Group
4) SNMP Host
5) SNMP User
6) SNMP Stats
7) SNMP Help
0) Exit
================================================================================
        """
    }

    if help_requested:
        print("\n" + "=" * 80)
        print(f"📖 Help for: {snmp_menu_help_info['command']}".center(80))
        print("=" * 80)
        print(f"\n{snmp_menu_help_info['description']}\n")
        print("Troubleshooting Steps:")
        for step in snmp_menu_help_info['troubleshooting_steps']:
            print(f"   {step}")
        print("\nExample Output:")
        print(snmp_menu_help_info['example_output'])
        return None

    menu_options = {
        "1": ("SNMP Configuration", snmp_config),
        "2": ("SNMP Engine ID", snmp_engineid),
        "3": ("SNMP Group", snmp_group),
        "4": ("SNMP Host", snmp_host),
        "5": ("SNMP User", snmp_user),
        "6": ("SNMP Stats", snmp_stats),
        "7": ("SNMP Help", snmp_help),
        "0": ("Exit", None),
    }

    while True:
        # Prepare menu display
        options_display = {key: description for key, (description, _) in menu_options.items()}
        display_formatted_menu("SNMP Menu", options_display)

        choice = input("Select an option (0-7) or enter '?' for help (e.g., '3?'): ").strip()

        # Handle 'X?' help functionality
        if choice.endswith("?"):
            base_choice = choice[:-1]  # Remove "?" from input
            if base_choice in menu_options:
                description, function = menu_options[base_choice]

                # Special case: `snmp_help` runs directly
                if function == snmp_help:
                    function()
                elif function:
                    print("\n" + "=" * 80)
                    print(f"📖 Help for: {description}".center(80))
                    print("=" * 80)
                    function(help_requested=True)  # Call function in help mode
                else:
                    print("\n[!] Help not available for this option.")
            else:
                print("\n[!] Invalid choice. Please enter a valid number followed by '?' (e.g., '2?').")

        elif choice in menu_options:
            description, function = menu_options[choice]
            if function:
                print("\n" + "-" * 80)
                print(f"Accessing {description}...".center(80))
                print("-" * 80)
                function()  # Normal function execution
            else:
                print("\nReturning to the previous menu...")
                break

        else:
            print("\n[!] Invalid choice. Please enter a number between 0 and 7.")
