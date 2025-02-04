
from core.utils import get_and_parse_cli_output

def snmp_group(suppress_output=False):
    """Retrieves and optionally displays the SNMP Group using 'show snmp-server group'."""

    command = "show snmp-server group"

    try:
        output = get_and_parse_cli_output(command)

        if not suppress_output:
            print("\nSNMP Group Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)

        return output

    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
