from core.utils import get_and_parse_cli_output
import re


def s2s_config(output_file="s2s_config.txt", suppress_output=False):
    """Retrieves Site-to-Site VPN-related configurations and writes them to a file."""

    commands = [
        "show running-config all crypto",
        "show running-config all tunnel-group",
        "show running-config all group-policy",
        "show running-config all interface Tunnel<number>"  # Placeholder for dynamic tunnel interfaces
    ]

    try:
        with open(output_file, "w") as file:
            for command in commands[:-1]:  # Execute all commands except the placeholder
                output = get_and_parse_cli_output(command)
                file.write(f"\n{command} Output:\n")
                file.write("-" * 80 + "\n")
                file.write(output + "\n")
                file.write("-" * 80 + "\n")

                if not suppress_output:
                    print(f"\n{command} Output:")
                    print("-" * 80)
                    print(output)
                    print("-" * 80)

            # Find tunnel interfaces dynamically
            tunnel_interfaces_output = get_and_parse_cli_output("show running-config all interface")
            tunnel_interfaces = re.findall(r"interface Tunnel(\d+)", tunnel_interfaces_output)

            for tunnel in tunnel_interfaces:
                tunnel_command = f"show running-config all interface Tunnel{tunnel}"
                tunnel_output = get_and_parse_cli_output(tunnel_command)
                file.write(f"\n{tunnel_command} Output:\n")
                file.write("-" * 80 + "\n")
                file.write(tunnel_output + "\n")
                file.write("-" * 80 + "\n")

                if not suppress_output:
                    print(f"\n{tunnel_command} Output:")
                    print("-" * 80)
                    print(tunnel_output)
                    print("-" * 80)

    except Exception as e:
        error_message = f"[!] Error: {e}"
        with open(output_file, "a") as file:
            file.write(error_message + "\n")
        if not suppress_output:
            print(error_message)
