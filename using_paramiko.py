#!/usr/local/bin/python3

import paramiko,time

#using as SSH Client

client = paramiko.SSHClient()

# check dir(client) to find available options.
# auto adjust host key verification with yes or no
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# time for connecting to remote Cisco IOS
"""
Manually taking input
addr = input('Provide IP address to connect to: ')
user = input('Username: ')
pwd = getpass.getpass('Password: ')"""

# Taking input from files

f1 = open("devices.txt","r")
f2 = open("commands.txt","r")

for line in f1:

    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    data = line.split(" ")
#    print(data)
    addr = data[0]
    user = data[1]
    pwd = data[2]

    f3 = open(addr+".txt","w+")

# print(addr +" "+ user +" " +pwd)

    client.connect(addr,username=user,password=pwd,allow_agent=False,look_for_keys=False)

# we have to ask for Shell

    device_access = client.invoke_shell()


    for line in f2:
        device_access.send(line)
        time.sleep(1)

    output = device_access.recv(55000).decode('ascii')
    f3.write(output)

"""
THIS CODE IS FOR SINGLE COMMAND, FOR MULTIPLE COMMANDS CODE BELOW

# send command to the device
    device_access.send("ter len 0\nshow run \n")
    time.sleep(2)

# receive output from the device, convert it to byte-like format and print it
print(device_access.recv(550000).decode('ascii'))

# We can print the same to a file too

with open("csr1000v.txt","w") as f:
    f.write(device_access.recv(550000).decode('ascii'))"""