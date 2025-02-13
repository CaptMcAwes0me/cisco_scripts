from core.utils import get_and_parse_cli_output

def nat_running_config(suppress_output=False, help_requested=False):
    """Retrieves and optionally displays the NAT Running Configuration using 'show running-config all nat'.
       If help_requested=True, it prints the help information instead.
    """

    nat_running_config_help = {
        'command': 'show running-config all nat',
        'description': (
            "Displays the full NAT configuration, including static and dynamic NAT rules "
            " (manual, auto, and manual after-auto). This command is essential for verifying "
            "NAT settings and troubleshooting connectivity issues related to address translation."
        ),
        'example_output': """
NAT Running Configuration:

object network INTERNAL_NET
 nat (inside,outside) dynamic interface
!
object network WEB_SERVER
 host 192.168.1.100
 nat (dmz,outside) static 203.0.113.100
!
nat (inside,outside) source dynamic any interface
        """
    }

    # If help is requested, print help content and exit the function
    if help_requested:
        print("\n" + "-" * 80)
        print(f"Help for: {nat_running_config_help['command']}".center(80))
        print("-" * 80)
        print(f"\n{nat_running_config_help['description']}\n")
        print("Example Output:")
        print(nat_running_config_help['example_output'])
        return None  # No actual command execution

    # Execute the NAT Running Config command
    command = "show running-config all nat"
    try:
        output = get_and_parse_cli_output(command)
        if not suppress_output:
            print("\nNAT Running Configuration Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)
        return output
    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
