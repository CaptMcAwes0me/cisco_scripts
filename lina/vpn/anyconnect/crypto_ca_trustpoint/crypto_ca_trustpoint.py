
from core.utils import get_and_parse_cli_output

def crypto_ca_trustpoint(suppress_output=False):
    """Retrieves and optionally displays the Crypto CA Trustpoint using 'show crypto ca trustpoint'."""

    command = "show crypto ca trustpoint"

    try:
        output = get_and_parse_cli_output(command)

        if not suppress_output:
            print("\nCrypto CA Trustpoint Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)

        return output

    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
