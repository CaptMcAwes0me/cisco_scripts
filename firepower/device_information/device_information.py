# Description: Display device information from the configuration file.

import os
from core.utils import parse_config
from core.utils import display_table

# Path to the configuration file
config_file_path = "/etc/sf/ims.conf"

# Fields to extract
fields_to_extract = ["SWVERSION", "SWBUILD", "MODEL", "APPLIANCE_UUID"]

def device_information():
    if not os.path.exists(config_file_path):
        print(f"Configuration file '{config_file_path}' does not exist.")
        return

    config_data = parse_config(config_file_path, fields_to_extract)
    if config_data:
        display_table(config_data)
    else:
        print("No matching fields found in the configuration file.")