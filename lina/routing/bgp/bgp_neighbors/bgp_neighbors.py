from core.utils import get_and_parse_cli_output


def bgp_neighbors(suppress_output=False, help_requested=False):
    """Retrieves and optionally displays the BGP neighbors using 'show bgp neighbors'.
       If help_requested=True, it prints the help information instead.
    """

    bgp_neighbors_help = {
        'command': 'show bgp neighbors',
        'description': (
            "Displays detailed information about BGP neighbors, including their state, "
            "BGP version, remote router ID, and session statistics."
        ),
        'example_output': """
BGP neighbor is 203.0.113.2, remote AS 200, external link
  BGP version 4, remote router ID 203.0.113.2
  BGP state = Established, up for 00:04:42
  Last read 00:00:13, hold time is 180, keepalive interval is 60 seconds
  Neighbor sessions:
    1 active, is not multisession capable (disabled)
  Neighbor capabilities:
    Route refresh: advertised and received(new)
  For address family: IPv4 Unicast
    BGP table version 7, neighbor version 7/0
    Output queue size : 0
    Index 1
    1 update-group member
                               Sent       Rcvd
      Prefixes Current:       3          3          (Consumes 240 bytes)
      Prefixes Total:         3          3
      Implicit Withdraw:      0          0
      Explicit Withdraw:      0          0
      Used as bestpath:       n/a        3
      Used as multipath:      n/a        0
        """
    }

    # If help is requested, print help content and exit the function
    if help_requested:
        print("\n" + "-" * 80)
        print(f"Help for: {bgp_neighbors_help['command']}".center(80))
        print("-" * 80)
        print(f"\n{bgp_neighbors_help['description']}\n")
        print("Example Output:")
        print(bgp_neighbors_help['example_output'])
        return None  # No actual command execution

    # Execute the BGP Neighbors command
    command = "show bgp neighbors"

    try:
        output = get_and_parse_cli_output(command)

        if not suppress_output:
            print("\nBGP Neighbors Output:")
            print("-" * 80)
            print(output)
            print("-" * 80)

        return output

    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
