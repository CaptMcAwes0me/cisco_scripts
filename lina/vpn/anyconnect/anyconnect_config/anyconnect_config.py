from core.utils import get_and_parse_cli_output


def anyconnect_config(suppress_output=False):
    """Retrieves and optionally displays AnyConnect-related configurations."""

    commands = [
        "show running-config all tunnel-group",
        "show running-config all group-policy",
        "show running-config all webvpn",
        "show running-config all crypto ca trustpoint"
    ]

    try:
        outputs = {cmd: get_and_parse_cli_output(cmd) for cmd in commands}

        formatted_output = "\n".join([
            "-" * 80,
            "                     Accessing AnyConnect Configuration...",
            "-" * 80,
            "\nAnyConnect (Secure Client) Configuration Output:",
            "-" * 80
        ])

        for cmd, output in outputs.items():
            formatted_output += f"\n\n{cmd} Output:\n" + "-" * 80 + f"\n{output.strip()}"

        formatted_output += "\n" + "-" * 80

        if not suppress_output:
            print(formatted_output)

        return formatted_output  # Ensure it returns a single formatted string

    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
