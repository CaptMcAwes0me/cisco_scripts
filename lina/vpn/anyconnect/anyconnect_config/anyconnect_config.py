from core.utils import get_and_parse_cli_output


def anyconnect_config(suppress_output=False):
    """Retrieves and optionally displays AnyConnect-related configurations."""

    command1 = "show running-config all tunnel-group"
    command2 = "show running-config all group-policy"
    command3 = "show running-config all webvpn"
    command4 = "show running-config all crypto ca trustpoint"


    try:
        output1 = get_and_parse_cli_output(command1)
        output2 = get_and_parse_cli_output(command2)
        output3 = get_and_parse_cli_output(command3)
        output4 = get_and_parse_cli_output(command4)

        if not suppress_output:
            print("\nAnyConnect (Secure Client) Configuration Output:")
            print("-" * 80)
            print(f"\n{command1} Output:")
            print("-" * 80)
            print(output1)
            print(f"\n{command2} Output:")
            print(output2)
            print(f"\n{command3} Output:")
            print(output3)
            print(f"\n{command4} Output:")
            print(output4)
            print("-" * 80)

        return output1, output2, output3, output4

    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return {"error": error_message}
