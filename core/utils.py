# Description: This file contains utility functions that are used by other modules in the application.

import re
import sys
import termios


def flush_stdin():
    """Flush stdin to clear any leftover input."""
    try:
        termios.tcflush(sys.stdin, termios.TCIFLUSH)
    except Exception:
        pass  # Ignore if flushing fails (e.g., on non-Unix systems)


def validate_uuid(uuid):
    """Validate if the given UUID matches the standard UUID format."""
    uuid_pattern = re.compile(r'^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$', re.IGNORECASE)
    return bool(uuid_pattern.match(uuid))


def validate_ip(ip_address):
    """Validate if the given IP address is in the correct IPv4 format."""
    ip_pattern = re.compile(
        r'^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$')
    return bool(ip_pattern.match(ip_address))


def validate_hex_uuid(uuid):
    """Validate the format of the UUID (32 hex characters in uppercase)."""
    uuid_pattern = re.compile(r'^[A-F0-9]{32}$')
    return bool(uuid_pattern.match(uuid))


def print_warning_box(message):
    """Prints the given message inside a formatted box for emphasis."""
    lines = message.split('\n')
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
        with open(file_path, 'r') as file:
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
