from core.utils import get_and_parse_cli_output


def crypto_ipsec_sa_detail():
    """Retrieves and displays detailed IPSec Security Association (SA) information, optionally filtered by peer IP."""

    peer_ip = input("Enter peer IP to filter (Press Enter for all SAs): ").strip()

    if peer_ip:
        command = f"show crypto ipsec sa peer {peer_ip} detail"
    else:
        command = "show crypto ipsec sa detail"

    try:
        output = get_and_parse_cli_output(command)

        print(f"\n{command} Output:")
        print("-" * 80)
        print(output)
        print("-" * 80)

        return output

    except Exception as e:
        error_message = f"[!] Error: {e}"
        print(error_message)
        return error_message
