# Description: This script queries the database for geodb peer information and provides the output.

import subprocess

def geodb_table():
    """
    Query the database for geodb peer information and provide the output.
    """
    print("Running query for GEO DB data...")

    # Construct the OmniQuery command to fetch SSL peer data from the database
    query_command = "OmniQuery.pl -db mdb -e \"select * from geodb_version;\""

    try:
        # Execute the OmniQuery command and capture the output with explicit encoding handling
        result = subprocess.run(
            query_command,
            shell=True,  # Using shell=True to allow multi-part commands
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,  # Text mode to automatically decode
            encoding='utf-8',  # Try UTF-8 encoding, fallback can be added if needed
            errors='ignore'  # Ignore characters that can't be decoded
        )

        if result.returncode == 0:
            output = result.stdout.strip()
            if output:
                print("Query result:")
                print(output)
            else:
                print("No results found for SSL peer data.")
        else:
            print(f"Error executing query: {result.stderr.strip()}")
    except Exception as e:
        print(f"An error occurred while querying the SSL peer data: {e}")

    # Revert to main menu after querying the SSL peer data
    input("\nPress Enter to return to the main menu...")
    return