from core.utils import get_and_parse_cli_output
import re


def s2s_config(suppress_output=False, filename=None):
    """Retrieves and optionally displays Site-to-Site VPN-related configurations.
       If a filename is provided, the output is written to the specified file."""

    commands = [
        "show running-config all crypto",
        "show running-config all tunnel-group",
        "show running-config all group-policy",
        "show running-config all interface Tunnel<number>",  # Placeholder
    ]

    results = {}
    output_lines = []  # Store formatted output for writing to a file

    try:
        # Execute initial commands
        for command in commands[:-1]:  # Exclude the Tunnel<number> placeholder
            output = get_and_parse_cli_output(command)
            results[command] = output

            formatted_output = f"\n{command} Output:\n" + ("-" * 80) + f"\n{output}\n" + ("-" * 80)
            output_lines.append(formatted_output)

            if not suppress_output:
                print(formatted_output)

        # Find tunnel interfaces dynamically
        tunnel_interfaces_output = get_and_parse_cli_output("show running-config all interface")
        tunnel_interfaces = re.findall(r"interface Tunnel(\d+)", tunnel_interfaces_output)

        for tunnel in tunnel_interfaces:
            tunnel_command = f"show running-config all interface Tunnel{tunnel}"
            tunnel_output = get_and_parse_cli_output(tunnel_command)
            results[tunnel_command] = tunnel_output

            formatted_output = f"\n{tunnel_command} Output:\n" + ("-" * 80) + f"\n{tunnel_output}\n" + ("-" * 80)
            output_lines.append(formatted_output)

            if not suppress_output:
                print(formatted_output)

        # Write to file if filename is provided
        if filename:
            try:
                with open(filename, 'w') as file:
                    file.write("=" * 80 + "\n")
                    file.write("S2S Configuration\n")
                    file.write("-" * 80 + "\n\n")
                    file.writelines("\n".join(output_lines))
                print(f"[+] Successfully wrote S2S configuration to {filename}")
            except Exception as e:
                print(f"[!] Error writing to file: {e}")

        return results

    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return {"error": error_message}
