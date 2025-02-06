# Description: This script contains the Cluster menu and its associated functions.

from core.utils import display_formatted_menu
from lina.blocks.blocks.blocks import blocks
from lina.blocks.blocks_exhaustion_history.blocks_exhaustion_history import blocks_exhaustion_history
from lina.blocks.blocks_exhaustion_snapsnot.blocks_exhaustion_snapshot import blocks_exhaustion_snapshot
from lina.blocks.blocks_queue_history_core_local.blocks_queue_history_core_local import blocks_queue_history_core_local
from lina.blocks.blocks_queue_history_detail.blocks_queue_history_detail import blocks_queue_history_detail
from lina.blocks.blocks_old.blocks_old import blocks_old
from lina.blocks.blocks_old_dump.blocks_old_dump import blocks_old_dump


def blocks_menu():
    menu_options = {
        "1": ("Blocks", blocks),
        "2": ("Blocks Exhaustion History", blocks_exhaustion_history),
        "3": ("Blocks Exhaustion Snapshot", blocks_exhaustion_snapshot),
        "4": ("Blocks Queue History Core-local", blocks_queue_history_core_local),
        "5": ("Blocks Queue History Detail", blocks_queue_history_detail),
        "6": ("Blocks Old", blocks_old),
        "7": ("Blocks Old Dump", blocks_old_dump),
        "0": ("Exit", None),
    }

    while True:
        # Prepare the menu options for display
        options_display = {key: description for key, (description, _) in menu_options.items()}
        display_formatted_menu("Cluster Menu", options_display)

        choice = input("Select an option (0-9): ").strip()

        if choice in menu_options:
            description, function = menu_options[choice]
            if function:  # If a function is assigned
                print("\n" + "-" * 80)
                print(f"Accessing {description}...".center(80))
                print("-" * 80)
                function()
            else:  # Exit condition
                print("\nExiting to previous menu...")
                break
        else:
            print("\n[!] Invalid choice. Please enter a number between 0 and 9.")
