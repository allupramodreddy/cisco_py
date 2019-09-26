#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

from ncclient import manager
import time

"""THIS CODE WILL ACT AS NETCONF CLIENT"""

#using connect function with manager to connect NETCONF enabled device

device = manager.connect(host = '192.168.202.131',username='root',password='cisco',port = '22',allow_agent=False, look_for_keys=False,hostkey_verify=False)
"""print(device)
print('_________________________')
print('_________________________')
time.sleep(3)
print(dir(device))"""
print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
time.sleep(2)
print(device.get_config('running'))