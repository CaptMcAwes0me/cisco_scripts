from core.utils import get_and_parse_cli_output


def crypto_ipsec_sa_detail(selected_peers):
    """Retrieves and displays detailed IPSec Security Association (SA) information for selected peers."""

    try:
        for peer in selected_peers:
            ip_address = peer[0]  # Extract the IP address from the peer tuple

            command = f"show crypto ipsec sa peer {ip_address} detail"
            output = get_and_parse_cli_output(command)

            print(f"\n{command} Output for {ip_address}:")
            print("-" * 80)
            print(output)
            print("-" * 80)

        return output

    except Exception as e:
        error_message = f"[!] Error: {e}"
        print(error_message)
        return error_message
