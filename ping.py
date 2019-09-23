#! /usr/local/bin/python3

from subprocess import getoutput
import sys
data = sys.argv[1:]
print(data)

for i in data:
    print("ping request for "+i)
    print(getoutput('ping -c 5 '+i))
    print('_________________')
    print('_________________')