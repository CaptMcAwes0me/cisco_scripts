import os
import tarfile
from core.utils import get_and_parse_cli_output


def xlate_detail(suppress_output=False, help_requested=False):
    """
    Retrieves and optionally displays the Xlate Detail Table using 'show xlate detail'.
    If help_requested=True, it prints the help information instead.
    """

    xlate_detail_help = {
        'command': 'show xlate detail',
        'description': (
            "Displays detailed information about current Network Address Translation (NAT) translations (xlates) on the FTD. "
            "This includes protocol, source and destination addresses and ports, translation types, flags, idle times, and timeouts. "
            "This command is useful for monitoring and troubleshooting NAT operations, providing insights into how internal addresses are being translated."
        ),
        'example_output': """
        firepower# show xlate detail
        3 in use, 8 most used
        Flags: D - DNS, e - extended, I - identity, i - dynamic, r - portmap,
               s - static, T - twice, N - net-to-net
        NAT from inside:192.168.1.5/12345 to outside:203.0.113.5/54321 flags ri idle 0:00:10 timeout 0:00:50
        NAT from inside:192.168.1.6/12346 to outside:203.0.113.6/54322 flags ri idle 0:00:20 timeout 0:00:40
        NAT from inside:192.168.1.7/12347 to outside:203.0.113.7/54323 flags ri idle 0:00:30 timeout 0:00:30
        """
    }

    # If help is requested, print help content and exit the function
    if help_requested:
        print("\n" + "-" * 80)
        print(f"Help for: {xlate_detail_help['command']}".center(80))
        print("-" * 80)
        print(f"\n{xlate_detail_help['description']}\n")
        print("Example Output:")
        print(xlate_detail_help['example_output'])
        return None  # No actual command execution

    # Execute the 'show xlate detail' command
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


def xlate_detail_interactive(suppress_output=False, help_requested=False):
    """
    Retrieves and optionally displays the Xlate Detail Table using 'show xlate detail'.
    Provides an interactive option to print to screen or write to a compressed file.
    If help_requested=True, it prints the help information instead.
    """

    xlate_detail_help = {
        'command': 'show xlate detail',
        'description': (
            "Displays detailed information about current Network Address Translation (NAT) translations (xlates) on the FTD. "
            "This includes protocol, source and destination addresses and ports, translation types, flags, idle times, and timeouts. "
            "This command is useful for monitoring and troubleshooting NAT operations, providing insights into how internal addresses are being translated."
        ),
        'example_output': """
        firepower# show xlate detail
        3 in use, 8 most used
        Flags: D - DNS, e - extended, I - identity, i - dynamic, r - portmap,
               s - static, T - twice, N - net-to-net
        NAT from inside:192.168.1.5/12345 to outside:203.0.113.5/54321 flags ri idle 0:00:10 timeout 0:00:50
        NAT from inside:192.168.1.6/12346 to outside:203.0.113.6/54322 flags ri idle 0:00:20 timeout 0:00:40
        NAT from inside:192.168.1.7/12347 to outside:203.0.113.7/54323 flags ri idle 0:00:30 timeout 0:00:30
        """
    }

    # If help is requested, print help content and exit the function
    if help_requested:
        print("\n" + "-" * 80)
        print(f"Help for: {xlate_detail_help['command']}".center(80))
        print("-" * 80)
        print(f"\n{xlate_detail_help['description']}\n")
        print("Example Output:")
        print(xlate_detail_help['example_output'])
        return None  # No actual command execution

    # Execute the 'show xlate detail' command
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
