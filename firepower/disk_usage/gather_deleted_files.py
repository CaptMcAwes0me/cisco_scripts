# Description: Gather information about deleted files with 'lsof | grep -i deleted' and save it to a file.

import time
import subprocess


def gather_deleted_files_info():
    """
    Gather information about deleted files with 'lsof | grep -i deleted' and save it to a file.
    """
    try:
        # Get current date and time
        current_time = time.strftime("%Y%m%d_%H%M%S")
        output_file = f"/var/common/{current_time}_deleted_files.txt"

        # Run the command to find deleted files
        result = subprocess.run("lsof | grep -i deleted", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # Write the output to a file
        with open(output_file, 'w') as file:
            file.write(result.stdout)

        print(f"\nDeleted file information has been saved to {output_file}")

    except Exception as e:
        print(f"An error occurred while gathering deleted file information: {e}")
