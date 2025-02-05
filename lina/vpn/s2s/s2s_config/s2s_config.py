from core.utils import get_and_parse_cli_output


def s2s_config(suppress_output=False):
    """Retrieves and optionally displays Site-to-Site VPN-related configurations."""

    commands = [
        "show running-config all crypto",
        "show running-config all tunnel-group",
        "show running-config all group-policy"
    ]

    results = {}

    try:
        # Execute initial commands
        for command in commands:
            output = get_and_parse_cli_output(command)
            results[command] = output

            if not suppress_output:
                print(f"\n{command} Output:")
                print("-" * 80)
                print(output)
                print("-" * 80)

        return results

    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return {"error": error_message}
