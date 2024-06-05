*** This script takes the output from "cluster exec show nat pool" from an ASA/FTD cluster member and determines the percentage of allocation of ports in use per IP address in the pat pool. ***

To run:
1.) Gather output of 'cluster exec show nat pool' and save to a text file
2.) Run the above script (ex. python3 calculate_pat_pool_usage_v16.py)
3.) Follow the prompts
