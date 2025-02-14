from core.utils import get_and_parse_cli_output


def crypto_ca_data(suppress_output=False, help_requested=False):
    """
    Retrieves and optionally displays Crypto CA data, including Trustpoint, Trustpool, Certificates, and CRLs.
    If help_requested=True, prints the help information instead of executing commands.
    """

    crypto_ca_data_help = {
        'commands': {
            "show crypto ca trustpoint": (
                "Displays the list of configured Certificate Authority (CA) trustpoints, which store "
                "identity certificates, enrollment parameters, and authentication details. This command is useful "
                "for verifying the configuration and status of each trustpoint."
            ),
            "show crypto ca trustpool": (
                "Provides information about the trustpool, a collection of trusted CA certificates used "
                "for validating remote peers. This command helps in viewing the certificates that constitute the trustpool."
            ),
            "show crypto ca certificates": (
                "Lists all installed CA certificates, including details such as the certificate's subject name, "
                "issuer name, serial number, and validity period. This command is essential for managing and verifying "
                "the installed certificates."
            ),
            "show crypto ca crls": (
                "Displays Certificate Revocation Lists (CRLs), which are used to verify the revocation "
                "status of certificates. This command helps in ensuring that the system is aware of any revoked certificates."
            )
        },
        'example_output': {
            "show crypto ca trustpoint": """
Trustpoint: MyCA
  Enrollment URL: http://ca-server.com/enroll
  Certificate: Installed
  Status: Available
            """,
            "show crypto ca trustpool": """
CA Trustpool:
  Root CA Cert 1: Valid until 2026
  Root CA Cert 2: Valid until 2028
            """,
            "show crypto ca certificates": """
Certificate
  Status: Available
  Certificate Serial Number: 0123456789ABCDEF0123456789ABCDEF
  Certificate Usage: General Purpose
  Issuer:
    cn=CompanyCA
    o=Company
    c=US
  Subject:
    Name: myrouter.example.com
    IP Address: 10.0.0.1
            """,
            "show crypto ca crls": """
CRL Issuer: cn=CompanyCA
  LastUpdate: Jan 1 12:00:00 2024 GMT
  NextUpdate: Jan 1 12:00:00 2025 GMT
  CRL Serial Number: 1234567890ABCDEF1234567890ABCDEF
            """
        }
    }

    if help_requested:
        print("\n" + "-" * 80)
        print("Help for: Crypto CA Data".center(80))
        print("-" * 80)

        for command, description in crypto_ca_data_help['commands'].items():
            print(f"\nCommand: {command}")
            print(description)
            print("\nExample Output:")
            print(crypto_ca_data_help['example_output'][command])
            print("-" * 80)

        return None  # No actual execution

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
