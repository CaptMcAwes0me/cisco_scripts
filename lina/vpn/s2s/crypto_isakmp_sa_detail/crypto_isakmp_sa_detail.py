from core.utils import get_and_parse_cli_output


def crypto_isakmp_sa_detail(suppress_output=False, help_requested=False):
    """Retrieves and optionally displays the Crypto ISAKMP SA Detail using 'show crypto isakmp sa detail'.
       If help_requested=True, it prints the help information instead.
    """

    crypto_isakmp_sa_detail_help = {
        'command': 'show crypto isakmp sa detail',
        'description': (
            "Displays detailed information about IKEv1 (ISAKMP) and IKEv2 security associations (SAs), "
            "including peer IP addresses, current state, encryption methods, hashing algorithms, "
            "authentication methods, and lifetime details. This command is essential for troubleshooting "
            "IKE phase 1 negotiations and ensuring that ISAKMP SAs are established correctly."
        ),
        'example_output': """
IPv4 Crypto ISAKMP SA
dst             src             state          conn-id status
192.168.1.1     192.168.1.2     QM_IDLE        1001    ACTIVE
  Encr: AES-CBC, Hash: SHA, Auth: preshared, Lifetime: 86400 sec
  Lifetime Remaining: 43200 sec
  NAT-T: Not Detected, DPd: N/A
        """
    }

    # If help is requested, display help content instead of executing the command
    if help_requested:
        print("\n" + "-" * 80)
        print(f"Help for: {crypto_isakmp_sa_detail_help['command']}".center(80))
        print("-" * 80)
        print(f"\n{crypto_isakmp_sa_detail_help['description']}\n")
        print("Example Output:")
        print(crypto_isakmp_sa_detail_help['example_output'])
        return None  # No actual command execution

    # Execute the Crypto ISAKMP SA Detail command
    command = "show crypto isakmp sa detail"
    try:
        output = get_and_parse_cli_output(command)
        if not suppress_output:
            print("\nCrypto ISAKMP SA Detail Output:".center(80))
            print(f"Command: {command}".center(80))
            print("-" * 80)
            print(output)
            print("-" * 80)
        return output

    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
