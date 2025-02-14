from core.utils import get_and_parse_cli_output


def crypto_ipsec_sa_detail(selected_peers, help_requested=False):
    """Retrieves and displays detailed IPSec Security Association (SA) information for selected peers.
       If help_requested=True, it prints the help information instead.
    """

    crypto_ipsec_sa_detail_help = {
        'command': 'show crypto ipsec sa peer <IP> detail',
        'description': (
            "Displays detailed information about the IPSec Security Associations (SAs) for a specified peer. "
            "This includes encryption/authentication algorithms, tunnel mode, lifetimes, inbound and outbound SPI values, "
            "packets encrypted/decrypted, and error statistics. This command is crucial for debugging IPSec tunnel connectivity issues."
        ),
        'example_output': """
peer: 192.168.1.2 port 500
    Crypto map tag: outside_map, seq num: 10, local addr: 172.16.1.1
  access-list inside_outside_acl permit ip 10.1.1.0 255.255.255.0 10.2.2.0 255.255.255.0
    local ident (addr/mask/prot/port): (10.1.1.0/255.255.255.0/0/0)
    remote ident (addr/mask/prot/port): (10.2.2.0/255.255.255.0/0/0)
    current_peer: 192.168.1.2
    inbound ESP SAs: 
      SPI: 0xAABBCCDD (27398)
         transform: esp-aes-256 esp-sha-hmac 
         in use settings: Tunnel, UDP Encapsulation
         lifetime: 28800 seconds, 4608000 kilobytes
         bytes decrypted: 1234567
         packets decrypted: 12345, dropped: 0
    outbound ESP SAs: 
      SPI: 0x11223344 (9823)
         transform: esp-aes-256 esp-sha-hmac 
         in use settings: Tunnel, UDP Encapsulation
         lifetime: 28800 seconds, 4608000 kilobytes
         bytes encrypted: 2345678
         packets encrypted: 23456, dropped: 0
        """
    }

    # If help is requested, display help content instead of executing the command
    if help_requested:
        print("\n" + "-" * 80)
        print(f"Help for: {crypto_ipsec_sa_detail_help['command']}".center(80))
        print("-" * 80)
        print(f"\n{crypto_ipsec_sa_detail_help['description']}\n")
        print("Example Output:")
        print(crypto_ipsec_sa_detail_help['example_output'])
        return None  # No actual command execution

    # Execute the Crypto IPSec SA Detail command for each selected peer
    try:
        for peer in selected_peers:
            ip_address = peer[0]  # Extract the IP address from the peer tuple
            command = f"show crypto ipsec sa peer {ip_address} detail"
            output = get_and_parse_cli_output(command)

            print(f"\nCrypto IPSec SA Detail Output for {ip_address}:".center(80))
            print(f"Command: {command}".center(80))
            print("-" * 80)
            print(output)
            print("-" * 80)

        return output

    except Exception as e:
        error_message = f"[!] Error: {e}"
        print(error_message)
        return error_message
