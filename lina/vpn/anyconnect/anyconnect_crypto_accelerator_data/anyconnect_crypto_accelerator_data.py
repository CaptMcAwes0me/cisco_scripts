from core.utils import get_and_parse_cli_output


def anyconnect_crypto_accelerator_data(suppress_output=False, help_requested=False):
    """
    Retrieves and optionally displays Crypto Accelerator data, including Load-balance, Statistics, Status, and Usage Detail.
    If help_requested=True, prints the help information instead of executing commands.
    """

    crypto_accelerator_help = {
        'commands': {
            "show crypto accelerator load-balance ssl": (
                "Displays the SSL load-balancing information for the crypto accelerator. This command helps in understanding how SSL sessions are distributed across the available hardware accelerators."
            ),
            "show crypto accelerator load-balance detail": (
                "Provides detailed load-balancing information for the crypto accelerator, including session distribution and load metrics. Useful for in-depth analysis of load distribution."
            ),
            "show crypto accelerator statistics": (
                "Shows global and accelerator-specific statistics from the hardware crypto accelerator MIB. This includes data on processed packets, errors, and performance metrics."
            ),
            "show crypto accelerator status": (
                "Displays the current status of the crypto accelerator, indicating whether it is enabled or disabled, and provides details about the hardware and firmware versions."
            ),
            "show crypto accelerator usage detail": (
                "Provides detailed information on the usage of the crypto accelerator, including session counts, resource utilization, and operational status."
            )
        },
        'example_output': {
            "show crypto accelerator load-balance ssl": """
SSL Load-Balancing Information:
  Accelerator 1:
    Active Sessions: 150
    Peak Sessions: 200
  Accelerator 2:
    Active Sessions: 130
    Peak Sessions: 180
            """,
            "show crypto accelerator load-balance detail": """
Load-Balancing Detail:
  Accelerator 1:
    Total Sessions: 5000
    Current Load: 75%
  Accelerator 2:
    Total Sessions: 4500
    Current Load: 70%
            """,
            "show crypto accelerator statistics": """
Crypto Accelerator Statistics:
  Packets Processed: 1,000,000
  Encryption Errors: 5
  Decryption Errors: 3
            """,
            "show crypto accelerator status": """
Crypto Accelerator Status:
  Status: Enabled
  Hardware Version: 1.2
  Firmware Version: 3.4.5
            """,
            "show crypto accelerator usage detail": """
Crypto Accelerator Usage Detail:
  Accelerator 1:
    Active Sessions: 150
    Resource Utilization: 60%
  Accelerator 2:
    Active Sessions: 130
    Resource Utilization: 55%
            """
        }
    }

    if help_requested:
        print("\n" + "-" * 80)
        print("Help for: Crypto Accelerator Data".center(80))
        print("-" * 80)

        for command, description in crypto_accelerator_help['commands'].items():
            print(f"\nCommand: {command}")
            print(description)
            print("\nExample Output:")
            print(crypto_accelerator_help['example_output'][command])
            print("-" * 80)

        return None  # No actual execution

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
