from core.utils import get_and_parse_cli_output


def ssl_data(suppress_output=False, help_requested=False):
    """
    Retrieves and optionally displays SSL data including Cipher, Errors, and Information.
    If help_requested=True, prints the help information instead of executing commands.
    """

    ssl_data_help = {
        'commands': {
            "show ssl cipher": (
                "Displays the list of SSL ciphers configured on the device, including details such as the "
                "cipher suite name, key exchange method, encryption algorithm, and message authentication code (MAC) algorithm. "
                "This command is useful for verifying the SSL/TLS cipher suites that are available for use in SSL connections."
            ),
            "show ssl errors": (
                "Provides information about SSL errors that have occurred, including details such as the "
                "error type, description, and the number of occurrences. This command helps in diagnosing issues related to SSL/TLS "
                "handshakes and data transmission."
            ),
            "show ssl information": (
                "Displays general SSL information, including details such as the SSL version, session parameters, "
                "and statistics related to SSL connections. This command is useful for obtaining an overview of the SSL/TLS configuration "
                "and operational status."
            )
        },
        'example_output': {
            "show ssl cipher": """
SSL Cipher Suites:
  Cipher Suite Name: ECDHE-RSA-AES256-GCM-SHA384
    Key Exchange Method: ECDHE-RSA
    Encryption Algorithm: AES256-GCM
    MAC Algorithm: SHA384
  Cipher Suite Name: ECDHE-RSA-AES128-GCM-SHA256
    Key Exchange Method: ECDHE-RSA
    Encryption Algorithm: AES128-GCM
    MAC Algorithm: SHA256
            """,
            "show ssl errors": """
SSL Errors:
  Error Type: Handshake Failure
    Description: The SSL handshake failed due to an unsupported cipher suite.
    Occurrences: 5
  Error Type: Certificate Validation Failure
    Description: The SSL certificate presented by the peer could not be validated.
    Occurrences: 3
            """,
            "show ssl information": """
SSL Information:
  SSL Version: TLSv1.2
  Active Sessions: 10
  Session Resumptions: 7
  Session Timeouts: 2
            """
        }
    }

    if help_requested:
        print("\n" + "-" * 80)
        print("Help for: SSL Data".center(80))
        print("-" * 80)

        for command, description in ssl_data_help['commands'].items():
            print(f"\nCommand: {command}")
            print(description)
            print("\nExample Output:")
            print(ssl_data_help['example_output'][command])
            print("-" * 80)

        return None  # No actual execution

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
                print("\n" + "=" * 80)
                print(f"{label} Output".center(80))
                print("=" * 80)
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
