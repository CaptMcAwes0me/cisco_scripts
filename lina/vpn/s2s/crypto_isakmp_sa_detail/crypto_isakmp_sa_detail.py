from core.utils import get_and_parse_cli_output


def crypto_isakmp_sa_detail(suppress_output=False):
    """Retrieves and optionally displays the Crypto ISAKMP SA Detail using 'show crypto isakmp sa detail'."""

    command = "show crypto isakmp sa detail"

    try:
        output = get_and_parse_cli_output(command)

        if not suppress_output:
            print("Crypto ISAKMP SA Detail Output:".center(80))
            print(f"Command: {command}".center(80))
            print("-" * 80)
            print(output)
            print("-" * 80)

        return output

    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
