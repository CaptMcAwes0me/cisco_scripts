
## TITLE  
  
- This script allows the usage of pushing commands to a single or multiple Cisco devices. 
  
## DESCRIPTION  

- This script allows the ability to push configuration to one or multiple Cisco devices.  It also prompts the user to provide command(s) to verify if the changes took place.    

## INSTALL/RUN  
  
- Python3 (tested on Python 3.12.3) on Mac OSX. 
- Requires paramiko (pip3 install paramiko). 
- Download/save "batch_commands.py" script.  
- To run "python3 batch_commands.py"

 ## HOW TO USE  
  
- Prepare configuration changes and save to a file.  Example below:  

```
configure terminal
interface Gigabitethernet0/1
description Python test
exit
exit
```

- Run the script "python3 batch_commands.py" and follow the prompts.  

*** Note: Do not mix types of devices and/or versions as you may receive unexpected results. Additionally, in the config file make sure you write the exact syntax of the commands you want to push, including 'configure terminal' and 'exit' as many times it takes to bring you back to privileged exec to run the verification 'show' commands. ***
  
## AUTHOR  

- Garrett McCollum - Cisco Systems Inc. (2024)  
