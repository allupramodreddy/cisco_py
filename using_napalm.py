#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

from napalm import get_network_driver
driver = get_network_driver('ios')

"""connecting to the device"""

device = driver('192.168.202.131','root','cisco')
print([i for i in dir(device) if 'load' in i])
"""output for above command: ['_load_candidate_wrapper', 'load_merge_candidate', 'load_replace_candidate', 'load_template']

Now, open session with device"""
device.open()

# merging configuration
device.load_merge_candidate(filename='/Users/pallu/cisco_py/commandlist_for_napalm.txt')

"""print the compare diff"""

print(device.compare_config())

"""now to commit the applied config"""

try:
    choice = input("\nwould you like to commit changes? [Y/N]: Default N ")
except NameError:
    choice = input("\nwould you like to commit these changes? [Y/N]: Default N ")
if choice == "Y" or choice == "y" or choice == "\n":
    print("committing . . . .")
    device.commit_config()
else:
    print("Discarding . . . .")
    device.discard_config()

"""Close the device connection"""
device.close()