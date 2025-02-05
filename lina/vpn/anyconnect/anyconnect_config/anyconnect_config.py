from core.utils import get_and_parse_cli_output


def anyconnect_config(suppress_output=False):
    """Retrieves and optionally displays AnyConnect-related configurations."""

    commands = [
        "show running-config all tunnel-group",
        "show running-config all group-policy",
        "show running-config all webvpn",
        "show running-config all crypto trustpoint"
    ]

    results = {}

    try:
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
