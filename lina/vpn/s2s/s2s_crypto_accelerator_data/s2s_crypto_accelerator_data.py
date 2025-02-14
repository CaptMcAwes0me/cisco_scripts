from core.utils import get_and_parse_cli_output


def s2s_crypto_accelerator_data(suppress_output=False, help_requested=False):
    """Retrieves and optionally displays Crypto Accelerator data including Load-balance, Statistics, Status, and Usage Detail.
       If help_requested=True, it prints the help information instead.
    """

    crypto_accelerator_help = {
        'commands': {
            "show crypto accelerator load-balance ipsec": (
                "Displays how IPSec load balancing is distributed across hardware crypto accelerators. "
                "Useful for verifying load distribution efficiency in multi-core platforms."
            ),
            "show crypto accelerator load-balance detail": (
                "Provides a detailed breakdown of each hardware accelerator's contribution to IPSec processing. "
                "Useful for debugging unbalanced crypto loads."
            ),
            "show crypto accelerator statistics": (
                "Displays statistical data, including packets encrypted/decrypted and offloaded to hardware. "
                "Useful for analyzing cryptographic performance."
            ),
            "show crypto accelerator status": (
                "Shows whether crypto hardware acceleration is enabled or disabled, and provides version details. "
                "Essential for verifying system capabilities."
            ),
            "show crypto accelerator usage detail": (
                "Provides an in-depth view of each crypto accelerator's session and resource utilization. "
                "Useful for capacity planning and troubleshooting."
            )
        },
        'example_output': {
            "show crypto accelerator load-balance ipsec": """
Crypto accelerator load balance for IPSec:
   Core 0:  250 packets, 500000 bytes
   Core 1:  300 packets, 600000 bytes
   Core 2:  280 packets, 560000 bytes
   Core 3:  270 packets, 540000 bytes
            """,
            "show crypto accelerator load-balance detail": """
Crypto accelerator load balance detail:
   Core 0:  Sessions: 5, Packets: 250, Bytes: 500000
   Core 1:  Sessions: 6, Packets: 300, Bytes: 600000
   Core 2:  Sessions: 5, Packets: 280, Bytes: 560000
   Core 3:  Sessions: 4, Packets: 270, Bytes: 540000
            """,
            "show crypto accelerator statistics": """
Crypto accelerator statistics:
   Encrypted packets: 120000
   Decrypted packets: 118000
   Hardware offload: 99.8%
   Failed packets: 50
            """,
            "show crypto accelerator status": """
Crypto accelerator status:
   Hardware acceleration: Enabled
   Firmware version: 2.3.1
   Crypto cores: 4 active
            """,
            "show crypto accelerator usage detail": """
Crypto accelerator usage detail:
   Core 0: Active sessions: 5, Utilization: 70%
   Core 1: Active sessions: 6, Utilization: 75%
   Core 2: Active sessions: 5, Utilization: 72%
   Core 3: Active sessions: 4, Utilization: 68%
            """
        }
    }

    # If help is requested, display command help instead of executing them
    if help_requested:
        print("\n" + "-" * 80)
        print(f"Help for: {crypto_accelerator_help['command']}".center(80))
        print("-" * 80)
        print(f"\n{crypto_accelerator_help['description']}\n")
        print("Example Output:")
        print(crypto_accelerator_help['example_output'])
        return None

    commands = {
        "Crypto Accelerator Load-balance IPSec": "show crypto accelerator load-balance ipsec",
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
                print(f"🔹 {label} Output".center(80))
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