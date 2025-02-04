
from core.utils import get_and_parse_cli_output

def snmp_user(suppress_output=False):
    """Retrieves and optionally displays the SNMP User using 'show snmp-server user'."""

    command = "show snmp-server user"

    try:
        output = get_and_parse_cli_output(command)

        if not suppress_output:
            print("\nSNMP User Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)

        return output

    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
