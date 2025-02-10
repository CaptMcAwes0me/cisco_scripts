from core.utils import get_and_parse_cli_output


def ssl_data(suppress_output=False):
    """Retrieves and optionally displays SSL data including Cipher, Errors, and Information."""

    commands = {
        "SSL Cipher": "show ssl cipher",
        "SSL Errors": "show ssl errors",
        "SSL Information": "show ssl information"
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
