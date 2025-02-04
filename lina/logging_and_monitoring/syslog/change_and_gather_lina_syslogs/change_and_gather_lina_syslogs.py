# Description: This script changes the logging_and_monitoring level on the ASA and gathers logs for a specified duration.

import time
import shutil
import subprocess
from core.utils import get_and_parse_cli_output


def log_analysis():
    """
    Function to analyze logs based on user-specified logging_and_monitoring level and duration.
    """
    # Define logging_and_monitoring levels with corresponding descriptions
    logging_levels = {
        1: 'alerts',
        2: 'critical',
        3: 'errors',
        4: 'warnings',
        5: 'notifications',
        6: 'informational',
        7: 'debugging'
    }

    # Display available logging_and_monitoring levels and prompt user to select one
    print("Select the logging_and_monitoring level to parse:")
    for level, description in logging_levels.items():
        print(f"{level}: {description}")

    try:
        # Get user input for the logging_and_monitoring level, default to 6 (informational)
        log_level = int(input("Enter the logging_and_monitoring level (default is 6): ") or 6)
        if log_level not in logging_levels:
            raise ValueError
    except ValueError:
        # Handle invalid input by defaulting to level 6
        print("Invalid input. Defaulting to level 6 (informational).")
        log_level = 6

    try:
        # Get user input for the duration to parse logs, default to 60 seconds
        duration = int(input("Enter the duration to parse logs (in seconds, default is 60): ") or 60)
        if duration <= 0:
            raise ValueError
    except ValueError:
        # Handle invalid input by defaulting to 60 seconds
        print("Invalid input. Defaulting to 60 seconds.")
        duration = 60

    # Get the current logging_and_monitoring buffered configuration from the system
    initial_config = get_and_parse_cli_output("show running-config logging_and_monitoring | include logging_and_monitoring buffered")
    print(f"Current logging_and_monitoring configuration: {initial_config.strip()}")

    # Update the logging_and_monitoring level based on user input
    new_logging_command = f'LinaConfigTool "logging_and_monitoring buffered {logging_levels[log_level]}"'
    subprocess.run(new_logging_command, shell=True, check=True)
    print(f"Setting logging_and_monitoring level: {logging_levels[log_level]}\nRunning command: {new_logging_command}")

    # Wait for the specified duration to allow logs to be gathered
    print(f"Waiting {duration} seconds to gather logs...")
    time.sleep(duration)

    # Redirect logs to a file with a timestamp
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    log_filename = f"disk0:{timestamp}_lina_syslog.log"
    log_command = f"show logging_and_monitoring | redirect {log_filename}"
    print(f"Redirecting logs with command: {log_command}")
    get_and_parse_cli_output(log_command)

    # Move the generated log file to a common directory for storage
    source_path = f"/ngfw/mnt/disk0/{timestamp}_lina_syslog.log"
    destination_path = "/ngfw/var/common/"

    try:
        print(f"Moving file from {source_path} to {destination_path}...")
        shutil.move(source_path, destination_path)
    except FileNotFoundError:
        # Handle file not found error by restoring the original logging_and_monitoring configuration
        print("Error: Log file not found.")
        restore_original_config(initial_config, log_level, logging_levels)  # Pass the arguments here
        return
    except Exception as e:
        # Handle other exceptions and restore the original logging_and_monitoring configuration
        print(f"Error: {e}")
        restore_original_config(initial_config, log_level, logging_levels)  # Pass the arguments here
        return

    # Restore the original logging_and_monitoring configuration at the end of the process
    restore_original_config(initial_config, log_level, logging_levels)  # Pass the arguments here


def restore_original_config(initial_config, log_level, logging_levels):
    """
    Restores the original logging_and_monitoring configuration. If the initial config is empty,
    disables buffered logging_and_monitoring by pushing the appropriate command.
    """
    if not initial_config.strip():  # Check if initial config is empty
        # If initial configuration is empty, disable buffered logging_and_monitoring
        print("Initial config is empty. Disabling buffered logging_and_monitoring...")
        new_logging_command = f'LinaConfigTool "no logging_and_monitoring buffered {logging_levels.get(log_level, "informational")}"'
    else:
        # Restore the original logging_and_monitoring configuration
        print("Restoring the original logging_and_monitoring configuration...")
        new_logging_command = f'LinaConfigTool "{initial_config.strip()}"'

    # Execute the command to restore or modify the logging_and_monitoring configuration
    subprocess.run(new_logging_command, shell=True, check=True)
