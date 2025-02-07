
from core.utils import get_and_parse_cli_output

def sla_operational_state(suppress_output=False):
    """Retrieves and optionally displays the SLA Operational State using 'sh sla monitor operational-state'."""

    command = "sh sla monitor operational-state"

    try:
        output = get_and_parse_cli_output(command)

        if not suppress_output:
            print("\nSLA Operational State Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)

        return output

    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
