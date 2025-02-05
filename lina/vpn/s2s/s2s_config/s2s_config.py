from core.utils import get_and_parse_cli_output
import re


def s2s_config(output_file="s2s_config.txt", suppress_output=False):
    """Retrieves Site-to-Site VPN-related configurations and writes them to a file."""

    commands = [
        "show running-config all crypto",
        "show running-config all tunnel-group",
        "show running-config all group-policy"
    ]

    try:
        with open(output_file, "w") as file:
            file.write("=" * 80 + "\nS2S Configuration\n" + "-" * 80 + "\n")

            for command in commands:
                output = get_and_parse_cli_output(command)

                if output is None:
                    output = "[!] No output received"  # Prevent writing None

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

            if tunnel_interfaces_output:
                tunnel_interfaces = re.findall(r"interface Tunnel(\d+)", tunnel_interfaces_output)

                for tunnel in tunnel_interfaces:
                    tunnel_command = f"show running-config all interface Tunnel{tunnel}"
                    tunnel_output = get_and_parse_cli_output(tunnel_command)

                    if tunnel_output is None:
                        tunnel_output = "[!] No output received"

                    file.write(f"\n{tunnel_command} Output:\n")
                    file.write("-" * 80 + "\n")
                    file.write(tunnel_output + "\n")
                    file.write("-" * 80 + "\n")

                    if not suppress_output:
                        print(f"\n{tunnel_command} Output:")
                        print("-" * 80)
                        print(tunnel_output)
                        print("-" * 80)

            file.write("=" * 80 + "\n")  # Close the section in the file

    except Exception as e:
        error_message = f"[!] Error: {e}"
        with open(output_file, "a") as file:
            file.write(error_message + "\n")
        if not suppress_output:
            print(error_message)
