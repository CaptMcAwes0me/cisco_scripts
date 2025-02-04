
from core.utils import get_and_parse_cli_output

def snmp_engineid(suppress_output=False):
    """Retrieves and optionally displays the SNMP EngineID using 'show snmp-server engineID'."""

    command = "show snmp-server engineID"

    try:
        output = get_and_parse_cli_output(command)

        if not suppress_output:
            print("\nSNMP EngineID Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)

        return output

    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
