#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

import netmiko
# multi vendor library

device1 = {'username':'root','password':'cisco','device_type':'cisco_ios','host':'192.168.202.131'}
# MULTI DEVICES
device2 = {'username':'root','password':'cisco','device_type':'cisco_ios','host':'192.168.54.128'}
device3 = {'username':'root','password':'cisco','device_type':'cisco_ios','host':'192.168.202.131'}

# to connect target device

# by checking couple of things connecthandler will allow you to connect
for i in [device1,device2,device3]:         # Multi Devices
    try:                            # try and except for error messages without stopping the because of an error
        print('connecting with device: ',i['host'])
        print('______________________________')
        device_connect = netmiko.ConnectHandler(**i)
        cmd = ["show run", "show ip int br", "show ver"]
        for k in cmd:                   # Multi Commands
            print('Sending command: ', k)
            print('____________________________')
            output = device_connect.send_command(k)
            print(output)
    except netmiko.ssh_exception.NetMikoTimeoutException:
        print('Device is not reachable, please check IP for: ',i['host'])

"""print the location of device_connect
print(device_connect)"""

"""Print directory of device_connect
print(dir(device_connect))"""

# print all directory messages with 'send' in them

# print([i for i in dir(device_connect) if 'send' in i])

# Output for above command: ['send_command', 'send_command_expect', 'send_command_timing', 'send_config_from_file', 'send_config_set']

# now sending command

""" SINGLE COMMAND
output = device_connect.send_command("show run")
# output = device_connect.read_channel()
print(output)"""

"""MULTIPLE COMMANDS"""

"""cmd = ["show run","show ip int br","show ver"]

for i in cmd:
    print('Sending command: ',i)
    print('____________________________')
    output = device_connect.send_command(i)
    print(output)"""