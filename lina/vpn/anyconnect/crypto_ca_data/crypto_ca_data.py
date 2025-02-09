from core.utils import get_and_parse_cli_output


def crypto_ca_data(suppress_output=False):
    """Retrieves and optionally displays Crypto CA data including Trustpoint, Trustpool, Certificates, and CRLs."""

    command1 = "show crypto ca trustpoint"
    command2 = "show crypto ca trustpool"
    command3 = "show crypto ca certificates"
    command4 = "show crypto ca crls"

    try:
        output1 = get_and_parse_cli_output(command1)
        output2 = get_and_parse_cli_output(command2)
        output3 = get_and_parse_cli_output(command3)
        output4 = get_and_parse_cli_output(command4)

        if not suppress_output:
            print("\n" + "Crypto CA Trustpoint Output:".center(80))
            print("-" * 80)
            print(output1)
            print("-" * 80)

            print("\n" + "Crypto CA Trustpool Output:".center(80))
            print("-" * 80)
            print(output2)
            print("-" * 80)

            print("\n" + "Crypto CA Certificates Output:".center(80))
            print("-" * 80)
            print(output3)
            print("-" * 80)

            print("\n" + "Crypto CA CRLs Output:".center(80))
            print("-" * 80)
            print(output4)
            print("-" * 80)

        return output1, output2, output3, output4

    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message

