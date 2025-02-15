import os
import tarfile
from datetime import datetime
from lina.blocks.blocks.blocks import blocks
from lina.blocks.blocks_exhaustion_snapsnot.blocks_exhaustion_snapshot import blocks_exhaustion_snapshot
from lina.blocks.blocks_queue_history_core_local.blocks_queue_history_core_local import blocks_queue_history_core_local
from lina.blocks.blocks_queue_history_detail.blocks_queue_history_detail import blocks_queue_history_detail
from lina.blocks.blocks_old.blocks_old import blocks_old
from lina.blocks.blocks_old_dump.blocks_old_dump import blocks_old_dump
from lina.blocks.blocks_exhaustion_history.blocks_exhaustion_history import blocks_exhaustion_history


def dump_all_blocks_data():
    """Gathers output from all blocks-related commands, writes each to a separate file, and compresses them into a .tar.gz archive."""

    # Define the directory path
    troubleshooting_dir = "/var/log/fp_troubleshooting_data"

    # Ensure the directory exists
    if not os.path.exists(troubleshooting_dir):
        try:
            os.makedirs(troubleshooting_dir)
            print(f"[+] Created directory: {troubleshooting_dir}")
        except Exception as e:
            print(f"[!] Error creating directory: {e}")
            return

    # Generate timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # Create the working directory named "<timestamp>_show_tech_blocks"
    log_dir = os.path.join(troubleshooting_dir, f"{timestamp}_show_tech_blocks")

    try:
        os.makedirs(log_dir)  # Create the timestamped directory
    except Exception as e:
        print(f"[!] Error creating log directory: {e}")
        return

    # Define commands and their corresponding functions
    commands = {
        "blocks": blocks,
        "blocks_exhaustion_history": blocks_exhaustion_history,
        "blocks_exhaustion_snapshot": blocks_exhaustion_snapshot,
        "blocks_queue_history_core_local": blocks_queue_history_core_local,
        "blocks_queue_history_detail": blocks_queue_history_detail,
        "blocks_old": blocks_old,
        "blocks_old_dump": blocks_old_dump
    }

    # Execute each command and write to separate timestamped log files
    for filename, function in commands.items():
        file_path = os.path.join(log_dir, f"{timestamp}_{filename}.log")
        try:
            output = function(suppress_output=True)
            with open(file_path, "w") as f:
                f.write(output + "\n")
            print(f"[+] Wrote output to: {file_path}")
        except Exception as e:
            print(f"[!] Error retrieving data for {filename}: {e}")

    # Compress all logs into a .tar.gz archive with the required naming format
    archive_path = os.path.join(troubleshooting_dir, f"{timestamp}_show_tech_blocks.tar.gz")
    try:
        with tarfile.open(archive_path, "w:gz") as tar:
            tar.add(log_dir, arcname=os.path.basename(log_dir))
        print(f"[+] Compressed logs into: {archive_path}")

        # Cleanup: Remove the temporary log directory and files after compression
        for file in os.listdir(log_dir):
            os.remove(os.path.join(log_dir, file))  # Remove individual log files
        os.rmdir(log_dir)  # Remove empty directory
    except Exception as e:
        print(f"[!] Error compressing logs: {e}")
