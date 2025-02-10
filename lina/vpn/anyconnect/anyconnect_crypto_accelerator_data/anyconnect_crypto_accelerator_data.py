from core.utils import get_and_parse_cli_output


def anyconnect_crypto_accelerator_data(suppress_output=False):
    """Retrieves and optionally displays Crypto Accelerator data including Load-balance, Statistics, Status and Usage Detail."""

    commands = {
        "Crypto Accelerator Load-balance SSL": "show crypto accelerator load-balance ssl",
        "Crypto Accelerator Load-balance Detail": "show crypto accelerator load-balance detail",
        "Crypto Accelerator Statistics": "show crypto accelerator statistics",
        "Crypto Accelerator Status": "show crypto accelerator status",
        "Crypto Accelerator Usage Detail": "show crypto accelerator usage detail"
    }

    outputs = {}

    for label, command in commands.items():
        try:
            output = get_and_parse_cli_output(command)
            outputs[label] = output

            if not suppress_output:
                print(f"{label} Output".center(80))
                print(f"Command: {command}".center(80))
                print("-" * 80)
                print(output)
                print("-" * 80)

        except Exception as e:
            error_message = f"[!] Error retrieving {label}: {e}"
            outputs[label] = error_message

            if not suppress_output:
                print(error_message)

    return outputs
