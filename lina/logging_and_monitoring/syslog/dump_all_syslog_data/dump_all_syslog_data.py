import os
from datetime import datetime
from lina.logging_and_monitoring.syslog.logging_config.logging_config import logging_config
from lina.logging_and_monitoring.syslog.logging_queue.logging_queue import logging_queue
from lina.logging_and_monitoring.syslog.logging_message.logging_message import logging_message
from lina.logging_and_monitoring.syslog.logging_manager_detail.logging_manager_detail import logging_manager_detail
from lina.logging_and_monitoring.syslog.logging_dynamic_rate_limit.logging_dynamic_rate_limit \
    import logging_dynamic_rate_limit
from lina.logging_and_monitoring.syslog.logging_unified_client.logging_unified_client import logging_unified_client
from lina.logging_and_monitoring.syslog.logging_unified_client_stats.logging_unified_client_stats \
    import logging_unified_client_stats
from lina.logging_and_monitoring.syslog.logging_buffered_output.logging_buffered_output import logging_buffered_output


def dump_all_syslog_data():
    """Gathers output from all Syslog-related commands and writes them to a log file under
    /var/log/fp_troubleshooting_data."""

    # Define the directory path
    troubleshooting_dir = "/var/log/fp_troubleshooting_data"

    # Check if the directory exists, if not, create it
    if not os.path.exists(troubleshooting_dir):
        try:
            os.makedirs(troubleshooting_dir)
            print(f"[+] Created directory: {troubleshooting_dir}")
        except Exception as e:
            print(f"[!] Error creating directory: {e}")
            return

    # Generate timestamp for the log file
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = os.path.join(troubleshooting_dir, f"{timestamp}_syslog_dump.log")

    try:
        # Gather outputs
        data_to_dump = [
            ("Logging Configuration", logging_config(suppress_output=True)),
            ("Logging Queue", logging_queue(suppress_output=True)),
            ("Logging Message Details", logging_message(suppress_output=True)),
            ("Logging Manager Detail", logging_manager_detail(suppress_output=True)),
            ("Logging Dynamic Rate Limit", logging_dynamic_rate_limit(suppress_output=True)),
            ("Logging Unified Client", logging_unified_client(suppress_output=True)),
            ("Logging Unified Client Stats", logging_unified_client_stats(suppress_output=True)),
            ("Logging Buffered Output", logging_buffered_output(suppress_output=True)),
        ]

        # Write all outputs to the log file
        with open(log_file, "w") as f:
            for title, output in data_to_dump:
                f.write(f"{'=' * 80}\n")
                f.write(f"{title}\n")
                f.write(f"{'-' * 80}\n")
                f.write(f"{output}\n")
                f.write(f"{'=' * 80}\n\n")

        print(f"\n[+] All Syslog data written to: {log_file}")

    except Exception as e:
        print(f"[!] Error writing Syslog data to file: {e}")
