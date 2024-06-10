*** This script allows the usage of pushing commands to a single or multiple Cisco devices. ***

To run:
1.) Create a text file of commands that you want to be pushed to the device(s). Example:

configure terminal
interface gigabitethernet0/1
description Python test
exit
exit

2.) Run the script (ex. python3 batch_commands.py)
3.) Follow the prompts.

*** Note: Do not mix types of devices and/or versions as you may receive unexpected results. Additionally, in the config file make sure you write the exact syntax of the commands you want to push, including 'configure terminal' and 'exit' as many times it takes to bring you back to privileged exec to run the verification 'show' commands. ***
