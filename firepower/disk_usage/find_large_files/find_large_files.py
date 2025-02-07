# Description: Find files greater than a user-specified size and display their sizes in a table.

import subprocess


def find_large_files():
    """
    Find files greater than a user-specified size and display their sizes in a table.
    """
    try:
        size = input("\nEnter the file size (e.g., 100M, 1G) or '0' to return to the menu: ").strip()
        if size == '0':
            print("\nReturning to the previous menu...")
            return

        print(f"\nFinding files greater than {size}...\n")
        find_command = f"find / -type f -size +{size} -exec ls -lh {{}} + 2>/dev/null | awk '{{print $9, $5}}'"

        result = subprocess.run(find_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        if result.stdout:
            # Parse the results and split into file paths and sizes
            rows = []
            for line in result.stdout.strip().split("\n"):
                file_path, file_size = line.rsplit(" ", 1)
                rows.append((file_path, file_size))

            # Determine column widths
            path_width = max(len(row[0]) for row in rows)
            size_width = max(len(row[1]) for row in rows)

            # Print the table header
            print(f"{'File Path'.ljust(path_width)}  {'Size'.rjust(size_width)}")
            print("-" * (path_width + size_width + 2))

            # Print each row
            for file_path, file_size in rows:
                print(f"{file_path.ljust(path_width)}  {file_size.rjust(size_width)}")
        else:
            print(f"\n[!] No files found greater than {size}.")
    except Exception as e:
        print(f"An error occurred while finding large files: {e}")
