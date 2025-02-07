# Description: Display disk usage with 'df -TH'.

import subprocess


def display_disk_usage():
    """
    Display disk usage with 'df -TH'.
    """
    try:
        result = subprocess.run(["df", "-TH"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print(result.stdout)
    except Exception as e:
        print(f"An error occurred while running 'df -TH': {e}")
