from core.utils import get_and_parse_cli_output


def asp_table_routing_all(suppress_output=False, help_requested=False):
    """Retrieves and optionally displays the ASP table routing information for all using
       the 'show asp table routing all' command. If help_requested=True, it prints the help information instead.
    """

    asp_table_routing_all_help = {
        'command': 'show asp table routing all',
        'description': (
            "Displays the Adaptive Security Processing (ASP) routing table used internally by the ASA. "
            "This table includes identity routes, static routes, dynamic routes, and routes associated "
            "with VPN tunnels. It is useful for diagnosing how traffic is processed and routed within the ASA."
        ),
        'example_output': """
Route Table Timestamp: 136

in   169.254.1.1     255.255.255.255 identity
in   127.1.0.1       255.255.255.255 identity
in   172.18.124.170  255.255.255.255 identity
in   1.1.1.1         255.255.255.255 via 14.36.117.100, inside
in   192.168.100.0   255.255.255.0   via 14.36.117.100, inside
in   172.18.108.0    255.255.255.0   via 172.18.124.1, outside
in   0.0.0.0         0.0.0.0         via 172.18.124.1, outside
        """
    }

    # If help is requested, print help content and exit the function
    if help_requested:
        print("\n" + "-" * 80)
        print(f"Help for: {asp_table_routing_all_help['command']}".center(80))
        print("-" * 80)
        print(f"\n{asp_table_routing_all_help['description']}\n")
        print("Example Output:")
        print(asp_table_routing_all_help['example_output'])
        return None  # No actual command execution

    # Execute the ASP Table Routing All command
    command = "show asp table routing all"
    try:
        output = get_and_parse_cli_output(command)

        if not suppress_output:
            print("\nASP Table Routing All Output:")
            print("-" * 80)

            # Format the output to improve readability
            formatted_output = []
            for line in output.splitlines():
                if line.startswith("Route Table Timestamp"):
                    formatted_output.append(f"\n🔹 {line}")
                else:
                    formatted_output.append(line)

            print("\n".join(formatted_output))
            print("-" * 80)

        return output

    except Exception as e:
        error_message = f"[!] Error: {e}"
        if not suppress_output:
            print(error_message)
        return error_message
