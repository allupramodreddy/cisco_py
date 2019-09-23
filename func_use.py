#!/usr/local/bin python3

from time import ctime
# only importing desired functions
from subprocess import getoutput

from os import mkdir

options = '''Press 1 for time
Press 2 for blah
Press 3 for bla bla
'''

print(options)

choose = str(input('Please select an option: '))
#choose = str(choose)
#print(type(choose))
if choose == '1':
    print(ctime())
elif choose == '2':
    d_name = input('please give directory name: ')
    mkdir(d_name)
    print (d_name + " successfully created")
elif choose == '3':
    cmd = input('please give your command: ')
    output = getoutput(cmd)
    print(output)
else:
    print("you have chosen: "+choose)