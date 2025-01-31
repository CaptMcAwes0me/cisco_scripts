from core.utils import get_and_parse_cli_output
import re


def bgp_advertised_routes(suppress_output=False):
    """Retrieves and optionally displays advertised routes for each BGP neighbor."""

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
