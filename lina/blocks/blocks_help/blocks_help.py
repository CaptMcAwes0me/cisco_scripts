def blocks_help():
    """Displays help information for Blocks-related commands and their troubleshooting applications."""

    blocks_help_info = {
        'command': 'Blocks Menu',
        'description': (
            "The Blocks Menu provides commands for monitoring memory block allocation and usage. "
            "These commands are useful for diagnosing memory fragmentation, block exhaustion, "
            "queue history, and debugging memory-related performance issues in the system."
        ),
        'help_sections': {
            "1. Monitoring Block Usage": [
                "🔹 Use `show blocks` to display current memory block allocation across different sizes.",
                "🔹 If block exhaustion is suspected, check `show blocks exhaustion history` for past exhaustion events.",
                "🔹 Example:",
                "   1️⃣ Run: show blocks (Check current memory block allocation)",
                "   2️⃣ Run: show blocks exhaustion history (Review past block exhaustion trends)"
            ],
            "2. Investigating Block Exhaustion": [
                "🔹 Use `show blocks exhaustion snapshot` to capture a real-time view of block allocation states.",
                "🔹 Example:",
                "   1️⃣ Run: show blocks exhaustion snapshot (Get a snapshot of block allocation at the moment of execution)"
            ],
            "3. Analyzing Queue History": [
                "🔹 Use `show blocks history core-local` to review memory usage within the core processor.",
                "🔹 Use `show blocks queue history detail` to track detailed queue-level allocation statistics.",
                "🔹 Example:",
                "   1️⃣ Run: show blocks history core-local (Analyze block allocation in the core)",
                "   2️⃣ Run: show blocks queue history detail (Check memory usage trends over time)"
            ],
            "4. Debugging Old Block Allocations": [
                "🔹 Use `show blocks old` to display the list of old memory blocks still in use.",
                "🔹 Use `show blocks old dump` to view detailed hex dumps of memory blocks for debugging.",
                "🔹 Example:",
                "   1️⃣ Run: show blocks old (Check for long-lived blocks that may indicate memory retention issues)",
                "   2️⃣ Run: show blocks old dump (Analyze memory contents of retained blocks)"
            ]
        }
    }

    print("\n" + "=" * 80)
    print(f"📖 Help for: {blocks_help_info['command']}".center(80))
    print("=" * 80)
    print(f"\n{blocks_help_info['description']}\n")

    for section, steps in blocks_help_info['help_sections'].items():
        print(f"\n🟢 {section}")
        for step in steps:
            print(f"   {step}")

    print("\n" + "=" * 80)
    print("🔍 Tip: Use 'X?' to see help for a specific command (e.g., '3?' for Blocks Exhaustion Snapshot).")
    print("=" * 80)
