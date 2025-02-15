# Description: This script contains the Blocks menu and its associated functions.

from core.utils import display_formatted_menu
from lina.blocks.blocks.blocks import blocks
from lina.blocks.blocks_exhaustion_history.blocks_exhaustion_history import blocks_exhaustion_history
from lina.blocks.blocks_exhaustion_snapshot.blocks_exhaustion_snapshot import blocks_exhaustion_snapshot
from lina.blocks.blocks_queue_history_core_local.blocks_queue_history_core_local import blocks_queue_history_core_local
from lina.blocks.blocks_queue_history_detail.blocks_queue_history_detail import blocks_queue_history_detail
from lina.blocks.blocks_old.blocks_old import blocks_old
from lina.blocks.blocks_old_dump.blocks_old_dump import blocks_old_dump
from lina.blocks.blocks_help.blocks_help import blocks_help


def blocks_menu():
    """Displays a menu for Blocks-related tasks.
       Supports 'X?' functionality to display help for each menu option.
    """

    menu_options = {
        "1": ("Blocks", blocks),
        "2": ("Blocks Exhaustion History", blocks_exhaustion_history),
        "3": ("Blocks Exhaustion Snapshot", blocks_exhaustion_snapshot),
        "4": ("Blocks Queue History Core-local", blocks_queue_history_core_local),
        "5": ("Blocks Queue History Detail", blocks_queue_history_detail),
        "6": ("Blocks Old", blocks_old),
        "7": ("Blocks Old Dump", blocks_old_dump),
        "8": ("Blocks Help", blocks_help),
        "0": ("Exit", None),
    }

    while True:
        # Prepare the menu options for display
        options_display = {key: description for key, (description, _) in menu_options.items()}
        display_formatted_menu("Blocks Menu", options_display)

        choice = input("Select an option (0-8) or enter '?' for help (e.g., '3?'): ").strip()

        # Handle 'X?' help functionality
        if choice.endswith("?"):
            base_choice = choice[:-1]  # Remove "?" from input
            if base_choice in menu_options:
                description, function = menu_options[base_choice]

                # Special case: `blocks_help` runs directly
                if function == blocks_help:
                    function()
                elif function:
                    print("\n" + "=" * 80)
                    print(f"Help for: {description}".center(80))
                    print("=" * 80)
                    function(help_requested=True)  # Call function in help mode
                else:
                    print("\n[!] Help not available for this option.")
            else:
                print("\n[!] Invalid choice. Please enter a valid number followed by '?' (e.g., '2?').")

        elif choice in menu_options:
            description, function = menu_options[choice]
            if function:
                print("\n" + "-" * 80)
                print(f"Accessing {description}...".center(80))
                print("-" * 80)
                function()  # Normal function execution
            else:
                print("\nExiting to previous menu...")
                break

        else:
            print("\n[!] Invalid choice. Please enter a number between 0 and 8.")
