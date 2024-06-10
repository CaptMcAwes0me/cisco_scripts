
## TITLE  
  
- Calculates pat pool usage percentage based upon the unit(s) per protocol/IP address.  
  
## DESCRIPTION  

- This script takes the output from "cluster exec show nat pool" from an ASA/FTD cluster member and determines the percentage of allocation of ports in use per IP address and protocol in the pat pool.  

## INSTALL/RUN  
  
- Python3 (tested on Python 3.12.3) on Mac OSX.  
- Download/save "calculate_pat_pool_usage_v16.py" script.  
- To run "python3 calculate_pat_pool_usage_v16.py"

 ## HOW TO USE  
  
- Gather output of 'cluster exec show nat pool' and save to a file.  
- Run the script and follow the prompts.  
  
Sample output:  
```    
(venv) Desktop $ python3 calculate_pat_pool_usage_v16.py  
┌────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐  
│                                                     !!!! DISCLAIMER !!!!!                                                      │  
│ This script will provide accurate data if the 'cluster-member-limit' matches that of the total amount of units in the cluster, │  
│                          or if single unit cluster it will account for half the ports being reserved.                          │  
│                                        If not, then the data output may be unreliable.                                         │  
│                                                                                                                                │  
│                            Note: This script does not support extended, flat, include-reserve, etc.                            │  
└────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘  
Enter the path of the file of 'cluster exec show nat pool': show_nat_pool.txt  
Enter the threshold percentage (70-99): 70  
Do you want to print the output to the screen or write to a file? (print/file): print  
Unit: unit-1-1(LOCAL):******************************************************  
┌────────────────┬─────────────────────┬───────────────────────────────┬─────────────────────┬───────────────────────────────┬─────────────────────┬───────────────────────────────┐  
│ IP Address     │ TCP Allocated ports │ Percentage of TCP allocation  │ UDP Allocated ports │ Percentage of UDP allocation  │ ICMP Allocated ports│ Percentage of ICMP allocation │  
├────────────────┼─────────────────────┼───────────────────────────────┼─────────────────────┼───────────────────────────────┼─────────────────────┼───────────────────────────────┤  
│ 1.2.3.4        │ 1836                │ 8.54                       %  │ 1343                │ 6.25                       %  │ 4                   │ 0.01                       %  │  
│ 1.2.3.5        │ 1170                │ 5.44                       %  │ 1455                │ 6.77                       %  │ 1                   │ 0.00                       %  │  
│ 1.2.3.6        │ 1192                │ 5.54                       %  │ 912                 │ 4.24                       %  │ 0                   │ 0.00                       %  │  
│ 1.2.3.7        │ 524                 │ 2.44                       %  │ 913                 │ 4.25                       %  │ 0                   │ 0.00                       %  │  
│ 1.2.3.8        │ 795                 │ 3.70                       %  │ 613                 │ 2.85                       %  │ 0                   │ 0.00                       %  │  
│ 1.2.3.9        │ 459                 │ 2.13                       %  │ 747                 │ 3.47                       %  │ 1                   │ 0.00                       %  │  
└────────────────┴─────────────────────┴───────────────────────────────┴─────────────────────┴───────────────────────────────┴─────────────────────┴───────────────────────────────┘  
```  
*** Output omitted for brevity. ***  

## AUTHOR  

- Garrett McCollum - Cisco Systems Inc. (2024)  
