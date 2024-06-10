
## TITLE  
  
- Presents the route table from an ASA/FTD in a more readable output. 
  
## DESCRIPTION  

- This script takes the output of 'show route all' from an ASA/FTD and provides the output in a more readable output.      

## INSTALL/RUN  
  
- Python3 (tested on Python 3.12.3) on Mac OSX. 
- Download/save "parse_route_table.py" script.  
- To run "python3 parse_route_table.py"

 ## HOW TO USE  
  
- Gather the output of 'show route all' from an ASA/FTD and save to a file.  
- Run the script "python3 parse_route_table.py" and follow the prompts.  

*** Note: The script does not presently support the display of all ECMP routes (e.g. it will only display the first route of all the ECMP routes.)  
  
## AUTHOR  

- Garrett McCollum - Cisco Systems Inc. (2024)  
