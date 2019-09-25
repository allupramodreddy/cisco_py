#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

import netmiko
# multi vendor library

device1 = {'username':'root','password':'cisco','device_type':'cisco_ios','host':'192.168.202.131'}
device_connect = netmiko.ConnectHandler(**device1)

""" THIS IS TAKING MANUAL INPUT
cmd = ["show run","show ip int br","show ver"]

for i in cmd:
    print('Sending command: ',i)
    print('____________________________')
    output = device_connect.send_command(i)
    print(output)
    
    NOW LET US TRY USING BUILTIN COMMANDS"""

""" MANUALLY TAKING INPUT FROM A LIST
conf = ["hostname pyrouter1","username hello privi 10 password cisco"]
output = device_connect.send_config_set(conf) # this will take care of 'conf t', and 'end'"""

"""NOW LET'S TRY TO TAKE INPUT OF CONFIGS FROM A FILE"""

output = device_connect.send_config_from_file('commandlist_for_netmiko.txt')
# print(output)

output1 = device_connect.send_command("sh ip int br",use_textfsm=True)
print(output1)
