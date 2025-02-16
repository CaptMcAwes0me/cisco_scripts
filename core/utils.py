# Description: This file contains utility functions that are used by other modules in the application.

import html
import re
import subprocess
import sys
import termios
import xml.etree.ElementTree as ET


def flush_stdin():
    """Flush stdin to clear any leftover input."""
    try:
        termios.tcflush(sys.stdin, termios.TCIFLUSH)
    except Exception:
        pass  # Ignore if flushing fails (e.g., on non-Unix systems)


def validate_uuid(uuid):
    """Validate if the given UUID matches the standard UUID format."""
    uuid_pattern = re.compile(
        r"^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$", re.IGNORECASE
    )
    return bool(uuid_pattern.match(uuid))


def validate_ip(ip_address):
    """Validate if the given IP address is in the correct IPv4 format."""
    ip_pattern = re.compile(
        r"^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\."
        r"(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\."
        r"(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\."
        r"(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
    )
    return bool(ip_pattern.match(ip_address))


def validate_hex_uuid(uuid):
    """Validate the format of the UUID (32 hex characters in uppercase)."""
    uuid_pattern = re.compile(r"^[A-F0-9]{32}$")
    return bool(uuid_pattern.match(uuid))


def print_warning_box(message):
    """Prints the given message inside a formatted box for emphasis."""
    lines = message.split("\n")
    longest_line = max(len(line) for line in lines)
    border = "*" * (longest_line + 4)

    print(border)
    for line in lines:
        print(f"* {line.ljust(longest_line)} *")
    print(border)


# Path to the configuration file
config_file_path = "/etc/sf/ims.conf"
fields_to_extract = ["SWVERSION", "SWBUILD", "MODEL", "APPLIANCE_UUID"]


def parse_config(file_path, keys_to_extract):
    """Parses the configuration file and returns specified key-value pairs."""
    config_data = {}
    try:
        with open(file_path, "r") as file:
            for line in file:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                if "=" in line:
                    key, value = map(str.strip, line.split("=", 1))
                    if key in keys_to_extract:
                        config_data[key] = value
    except FileNotFoundError:
        print(f"Error: Configuration file '{file_path}' not found.")
    except Exception as e:
        print(f"Error reading configuration file: {e}")
    return config_data


def get_and_parse_cli_output(command):
    """Executes the ConvergedCliClient command and extracts the desired CLI output."""

    # Execute the command using subprocess
    result = subprocess.run(
        ["ConvergedCliClient", command], capture_output=True, text=True
    )

    # Parse the output, which is XML-like with HTML-encoded content
    raw_output = result.stdout
    start = raw_output.find("<message>")
    end = raw_output.find("</message>") + len("</message>")
    xml_content = raw_output[start:end]

    # Parse the XML content using ElementTree
    root = ET.fromstring(xml_content)
    content = root.find(".//content")

    if content is not None:
        # HTML unescape to get the actual CLI output
        cli_output = html.unescape(content.text)

        # Extract the stuff between <cli> tags
        cli_start = cli_output.find("<cli")
        cli_end = cli_output.find("</cli>") + len("</cli>")
        cli_section = cli_output[cli_start:cli_end]

        # Further extract the text within <cli>...</cli>
        cli_text_start = cli_section.find(">") + 1
        cli_text_end = cli_section.find("</cli>")
        desired_output = cli_section[cli_text_start:cli_text_end].strip()

        return desired_output
    else:
        raise Exception("Failed to extract CLI output from response.")


def display_table(data):
    """Displays the configuration data in a more readable table format."""
    field_width = max(len(key) for key in data.keys()) + 2
    value_width = max(len(value) for value in data.values()) + 2
    table_width = field_width + value_width + 7

    # Print the table
    print("+" + "-" * (table_width - 2) + "+")
    print(f"| {'Field'.center(field_width)} | {'Value'.center(value_width)} |")
    print("+" + "-" * (table_width - 2) + "+")

    for key, value in data.items():
        print(f"| {key.ljust(field_width)} | {value.ljust(value_width)} |")

    print("+" + "-" * (table_width - 2) + "+")


def display_formatted_menu(title, options):
    """
    Displays a formatted menu.

    Parameters:
        title (str): The title of the menu.
        options (dict): A dictionary where keys are menu option numbers/letters,
                        and values are option descriptions.

    Returns:
        None
    """
    print("\n" + "=" * 80)
    print(f" {title} ".center(80, "="))
    print("=" * 80)
    for key, description in options.items():
        print(f"{key}) {description}")
    print("=" * 80)


def print_section(title, content):
    separator = "-" * 80
    title_line = f"| {title.center(76)} |"
    print(separator)
    print(title_line)
    print(separator)
    print(content)
    print(separator + "\n")


def ip_sort_key(ip):
    return tuple(map(int, ip.split('.')))


def convert_bps_to_readable(bps):
    """ Converts bytes per second (Bps) into human-readable format (KBps, MBps, GBps). """
    units = ["bps", "Kbps", "MBps", "Gbps"]
    index = 0
    while bps >= 1024 and index < len(units) - 1:
        bps /= 1024
        index += 1
    return f"{bps:.2f} {units[index]}"


def traffic_table(headers, data):
    """ Prints a well-formatted CLI table with consistent spacing. """
    col_widths = [max(len(str(item)) for item in col) for col in zip(headers, *data)]
    format_str = " | ".join(f"{{:<{w}}}" for w in col_widths)
    border = "-+-".join("-" * w for w in col_widths)

    print(border)
    print(format_str.format(*headers))
    print(border)
    for row in data:
        print(format_str.format(*row))
    print(border)