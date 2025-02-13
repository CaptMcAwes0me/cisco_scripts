from core.utils import get_and_parse_cli_output


def isis_running_config(suppress_output=False, help_requested=False):
    """Retrieves and optionally displays the ISIS running configuration.
       If help_requested=True, it prints the help information instead.
    """

    isis_running_config_help = {
        'command': 'show running-config all router isis',
        'description': (
            "Displays the complete ISIS running configuration, including process settings, IS-type, "
            "network statements, authentication, and interface configurations. This command is useful "
            "for verifying ISIS settings and troubleshooting routing inconsistencies."
        ),
        'example_output': """
router isis
 net 49.0001.1921.6800.1001.00
 is-type level-2
 authentication-mode md5
 metric-style wide
 passive-interface default
 no passive-interface GigabitEthernet0/1
        """
    }

    # If help is requested, print help content and exit the function
    if help_requested:
        print("\n" + "-" * 80)
        print(f"Help for: {isis_running_config_help['command']}".center(80))
        print("-" * 80)
        print(f"\n{isis_running_config_help['description']}\n")
        print("Example Output:")
        print(isis_running_config_help['example_output'])
        return None  # No actual command execution

    # Execute the ISIS Running Configuration command
    command = "show running-config all router isis"
    try:
        output = get_and_parse_cli_output(command)
        if not suppress_output:
            print("\nISIS Running Config Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)
        return output
    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
