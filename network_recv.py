#! /usr/local/bin/python3

import socket, time

# checking for socket function
"""for i in dir(socket):
    if 'socket' in i:
        print(i)
"""

""" above function can be written as below"""

print[ i for i in dir(socket) if 'socket' in i]

# creating udp socket
# ipv4 socket -- ipv4 + 2 byte port
# ipv6 socket -- ipv6 + 2 byte port

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM) #UDP
#               for IPv4        for UDP socket
#socket.socket(socket.AF_INET,socket.SOCK_STREAM) #TCP
#               for IPv4        for TCP socket

#RECEIVER CODE ONLY
s.bind(("", 8899)) #bind will accept tuple format ip & port
#Basic code
"""while True:
    data = s.recvfrom(1000) #no.of bytes to recv(buffer size)
    print(data)"""

#Send+Receive

while True:
    data = s.recvfrom(1000) #no.of bytes to recv(buffer size)
    print(data[0])
    print('received from: '+data[1])
    msg = imput('enter reply: ')
    newmsg = msg.encode('ascii')
    s.sendto(newmsg,data[1])



"""#SENDER CODE ONLY
msg=input("Enter data to send: ")
#converting data into byte-like format
newmsg = msg.encode('ascii')

#let's send data to target
s.sendto(newmsg,("127.0.0.1",8899))  #sendto will have message and ip & port in tuple format
s.close()"""
