from core.utils import get_and_parse_cli_output


def crypto_ca_data(suppress_output=False):
    """Retrieves and optionally displays Crypto CA data including Trustpoint, Trustpool, Certificates, and CRLs."""

    commands = {
        "Crypto CA Trustpoint": "show crypto ca trustpoint",
        "Crypto CA Trustpool": "show crypto ca trustpool",
        "Crypto CA Certificates": "show crypto ca certificates",
        "Crypto CA CRLs": "show crypto ca crls"
    }

    outputs = {}

    for label, command in commands.items():
        try:
            output = get_and_parse_cli_output(command)
            outputs[label] = output

            if not suppress_output:
                print(f"\n{label} Output:")
                print("-" * 80)
                print(output)
                print("-" * 80)

        except Exception as e:
            error_message = f"[!] Error retrieving {label}: {e}"
            outputs[label] = error_message

            if not suppress_output:
                print(error_message)

    return outputs
