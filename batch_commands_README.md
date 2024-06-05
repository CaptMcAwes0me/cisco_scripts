*** This script allows the usage of pushing commands to a single or multiple Cisco devices. ***

To run:
1.) Create a text file of commands that you want to be pushed to the device(s).  Example:

configure terminal 
interface gigabitethernet0/1
description Python test 
exit 
exit

2.) Run the script (ex. python3 batch_commands.py)
3.) Follow the prompts.

*** Note: Do not mix type(s) of devices and/or version(s) as you may receive unexpected results. ***
