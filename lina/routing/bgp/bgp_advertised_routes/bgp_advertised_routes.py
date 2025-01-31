from core.utils import get_and_parse_cli_output
import re

def bgp_advertised_routes(suppress_output=False):
    """Retrieves and optionally displays advertised routes for each BGP neighbor."""

    try:
        # Get the BGP summary output
        summary_output = get_and_parse_cli_output("show bgp summary")

        # Extract neighbor IP addresses
        neighbor_section_match = re.search(r"State/PfxRcd\s*\n(-+\n)?([\s\S]+)", summary_output)

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
