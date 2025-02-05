from core.utils import get_and_parse_cli_output
import re


def s2s_config(suppress_output=False):
    """Retrieves and optionally displays Site-to-Site VPN-related configurations."""

    # Initial commands to gather S2S-related configuration
    commands = [
        "show running-config all crypto",
        "show running-config all tunnel-group",
        "show running-config all group-policy",
        "show running-config all interface Tunnel<number>",  # Placeholder for dynamic commands
    ]

    results = {}

    try:
        # Execute initial commands
        for command in commands[:-1]:  # Exclude the Tunnel<number> placeholder for now
            output = get_and_parse_cli_output(command)
            results[command] = output

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
            results[tunnel_command] = tunnel_output

            if not suppress_output:
                print(f"\n{tunnel_command} Output:")
                print("-" * 80)
                print(tunnel_output)
                print("-" * 80)

        return results

    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return {"error": error_message}
