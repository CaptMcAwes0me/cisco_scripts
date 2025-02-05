from core.utils import get_and_parse_cli_output
import re
import os
import datetime

def s2s_config(output_dir="/var/log/fp_troubleshooting_data", suppress_output=False):
    """Retrieves and optionally writes Site-to-Site VPN-related configurations."""

    # Initial commands to gather S2S-related configuration
    commands = [
        "show running-config all crypto",
        "show running-config all tunnel-group",
        "show running-config all group-policy",
        "show running-config all interface Tunnel<number>",  # Placeholder for dynamic commands
    ]

    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Generate timestamped filename
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file_path = os.path.join(output_dir, f"{timestamp}_s2s_dump.log")

    try:
        with open(log_file_path, "w") as log_file:
            log_file.write("=" * 80 + "\n")
            log_file.write("S2S Configuration\n")
            log_file.write("-" * 80 + "\n\n")

            # Execute initial commands (excluding Tunnel<number> placeholder)
            for command in commands[:-1]:
                output = get_and_parse_cli_output(command)
                log_file.write(f"{command} Output:\n")
                log_file.write("-" * 80 + "\n")
                log_file.write(output + "\n")
                log_file.write("-" * 80 + "\n\n")

                if not suppress_output:
                    print(f"{command} Output:\n" + "-" * 80)
                    print(output)
                    print("-" * 80)

            # Find and retrieve tunnel interfaces
            tunnel_interfaces_output = get_and_parse_cli_output("show running-config all interface")
            tunnel_interfaces = re.findall(r"interface Tunnel(\d+)", tunnel_interfaces_output)

            for tunnel in tunnel_interfaces:
                tunnel_command = f"show running-config all interface Tunnel{tunnel}"
                tunnel_output = get_and_parse_cli_output(tunnel_command)

                log_file.write(f"{tunnel_command} Output:\n")
                log_file.write("-" * 80 + "\n")
                log_file.write(tunnel_output + "\n")
                log_file.write("-" * 80 + "\n\n")

                if not suppress_output:
                    print(f"{tunnel_command} Output:\n" + "-" * 80)
                    print(tunnel_output)
                    print("-" * 80)

            log_file.write("=" * 80 + "\n")

        return log_file_path  # Return path for debugging

    except Exception as e:
        error_message = f"[!] Error: {e}"
        with open(log_file_path, "a") as log_file:
            log_file.write(error_message + "\n")
        if not suppress_output:
            print(error_message)
        return {"error": error_message}
