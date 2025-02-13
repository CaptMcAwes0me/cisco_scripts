from core.utils import get_and_parse_cli_output
import re


def bgp_advertised_routes(suppress_output=False, help_requested=False):
    """Retrieves and optionally displays advertised routes for each BGP neighbor.
       If help_requested=True, it prints the help information instead.
    """

    bgp_advertised_routes_help = {
        'command': 'show bgp neighbor <neighbor> advertised-routes',
        'description': (
            "Displays all routes that have been advertised to a specified BGP neighbor. "
            "This is useful for verifying which routes your router is advertising to its BGP peers."
        ),
        'example_output': """
BGP table version is 7, local router ID is 203.0.113.1
Status codes: s suppressed, d damped, h history, * valid, > best, i - internal,
              r RIB-failure, S Stale, m multipath
Origin codes: i - IGP, e - EGP, ? - incomplete

   Network          Next Hop            Metric LocPrf Weight Path
*> 10.10.10.0/24    203.0.113.2              0             0 200 i
*> 10.180.10.0/24   203.0.113.2              0             0 200 i
*> 172.16.30.0/24   203.0.113.2              0             0 200 i
        """
    }

    # If help is requested, print help content and exit the function
    if help_requested:
        print("\n" + "-" * 80)
        print(f"Help for: {bgp_advertised_routes_help['command']}".center(80))
        print("-" * 80)
        print(f"\n{bgp_advertised_routes_help['description']}\n")
        print("Example Output:")
        print(bgp_advertised_routes_help['example_output'])
        return None  # No actual command execution

    try:
        # Get the BGP summary output
        summary_output = get_and_parse_cli_output("show bgp summary")

        # Locate the neighbor table section (starts after "State/PfxRcd")
        neighbor_section_match = re.search(r"State/PfxRcd\s*\n(-+\n)?([\s\S]+)", summary_output)

        if not neighbor_section_match:
            raise Exception("Failed to locate the neighbor section in 'show bgp summary' output.")

        neighbor_section = neighbor_section_match.group(2)

        # Extract neighbor IP addresses (first column in the neighbor table)
        neighbor_ips = re.findall(r"^\s*(\d+\.\d+\.\d+\.\d+)", neighbor_section, re.MULTILINE)

        if not neighbor_ips:
            raise Exception("No valid BGP neighbors found.")

        # Store output for all neighbors
        all_output = []

        for neighbor in neighbor_ips:
            command = f"show bgp neighbor {neighbor} advertised-routes"
            advertised_output = get_and_parse_cli_output(command)
            formatted_output = f"\nBGP Advertised Routes for {neighbor}:\n" + "-" * 80 + f"\n{advertised_output}\n" + "-" * 80
            all_output.append(formatted_output)

            if not suppress_output:
                print(formatted_output)

        return "\n".join(all_output)

    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
