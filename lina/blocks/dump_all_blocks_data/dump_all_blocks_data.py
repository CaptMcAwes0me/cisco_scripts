import os
from datetime import datetime
from lina.blocks.blocks.blocks import blocks
from lina.blocks.blocks_exhaustion_snapsnot.blocks_exhaustion_snapshot import blocks_exhaustion_snapshot
from lina.blocks.blocks_queue_history_core_local.blocks_queue_history_core_local import blocks_queue_history_core_local
from lina.blocks.blocks_queue_history_detail.blocks_queue_history_detail import blocks_queue_history_detail
from lina.blocks.blocks_old.blocks_old import blocks_old
from lina.blocks.blocks_old_dump.blocks_old_dump import blocks_old_dump
from lina.blocks.blocks_exhaustion_history.blocks_exhaustion_history import blocks_exhaustion_history


def dump_all_blocks_data():
    """Gathers output from all blocks-related commands and writes them to a log file under /var/log/fp_troubleshooting_data."""

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
    log_file = os.path.join(troubleshooting_dir, f"{timestamp}_blocks_dump.log")

    try:
        # Gather outputs
        data_to_dump = [
            ("Blocks", blocks(suppress_output=True)),
            ("Blocks Exhaustion History", blocks_exhaustion_history(suppress_output=True)),
            ("Blocks Exhaustion Snapshot", blocks_exhaustion_snapshot(suppress_output=True)),
            ("Blocks Queue History Core Local", blocks_queue_history_core_local(suppress_output=True)),
            ("Blocks Queue History Detail", blocks_queue_history_detail(suppress_output=True)),
            ("Blocks Old", blocks_old(suppress_output=True)),
            ("Blocks Old Dump", blocks_old_dump(suppress_output=True))
        ]

        # Write all outputs to the log file
        with open(log_file, "w") as f:
            for title, output in data_to_dump:
                f.write(f"{'=' * 80}\n")
                f.write(f"{title}\n")
                f.write(f"{'-' * 80}\n")
                f.write(f"{output}\n")
                f.write(f"{'=' * 80}\n\n")

        print(f"\n[+] All Blocks-related data written to: {log_file}")

    except Exception as e:
        print(f"[!] Error writing Blocks-related data to file: {e}")
