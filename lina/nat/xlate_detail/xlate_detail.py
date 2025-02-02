import os
import tarfile
from core.utils import get_and_parse_cli_output


def xlate_detail(suppress_output=False):
    """Retrieves and optionally displays the Xlate Detail Table using 'show xlate detail'."""

    command = "show xlate detail"

    try:
        output = get_and_parse_cli_output(command)

        if not suppress_output:
            print("\nXlate Detail Table Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)

        return output

    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message


def xlate_detail_interactive(suppress_output=False):
    """Retrieves and optionally displays the Xlate Detail Table using 'show xlate detail'."""

    command = "show xlate detail"
    output_dir = "/var/common/fp_troubleshooting_data"

    try:
        output = get_and_parse_cli_output(command)

        if not suppress_output:
            print("\n⚠ WARNING: The output of this command can be large and may take time to process. ⚠\n")
            choice = input("Would you like to (1) print to screen or (2) write to file? Enter 1 or 2: ").strip()

            if choice == "1":
                print("\nXlate Detail Table Output:")
                print("-" * 80)
                print(output)
                print("-" * 80)

            elif choice == "2":
                # Ensure directory exists
                os.makedirs(output_dir, exist_ok=True)

                filename = "xlate_detail_output.txt"
                file_path = os.path.join(output_dir, filename)

                # Write output to file
                with open(file_path, "w") as f:
                    f.write(output)

                # Compress file
                tar_path = file_path + ".tar.gz"
                with tarfile.open(tar_path, "w:gz") as tar:
                    tar.add(file_path, arcname=filename)

                # Remove the original text file after compression
                os.remove(file_path)

                print(f"✅ Output written and compressed to: {tar_path}")

            else:
                print("Invalid choice. Defaulting to printing on screen.")
                print("\nXlate Detail Table Output:")
                print("-" * 80)
                print(output)
                print("-" * 80)

        return output

    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
