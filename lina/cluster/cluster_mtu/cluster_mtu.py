
from core.utils import get_and_parse_cli_output


def cluster_mtu(suppress_output=False):
    """Retrieves and optionally displays the All MTUs Configured using 'show running-config | include mtu'."""

    command = "show running-config mtu"

    try:
        output = get_and_parse_cli_output(command)

        if not suppress_output:
            print("\nAll MTUs Configured Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)
            print(
                "\033[1;33m[NOTE]\033[0m: The Cluster Control Link (CCL) MTU should be configured to at least 100 bytes"
                " larger than Data Interfaces to ensure stable cluster communication and performance.\n")

        return output

    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
