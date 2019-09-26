#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

import requests
from requests.auth import HTTPBasicAuth
"""THIS IS FOR SUPPLYING HTTP BASIC AUTHENTICATION"""

cred = HTTPBasicAuth('root','cisco')
head = {'Accept':'application/json'}

"""DEFINING DATA FROM THAT API IN JSON FORMAT"""

url = "http://192.168.202.131/level/15/exec/~/sh/ip/int/br"

"""NOW CONNECTION TO RESTCONF --OR-- HTTP PROTOCOL"""

output = requests.get(url,headers=head,auth=cred)
print(output)
"""ONLY GIVES HTTP RESPONSE CODE"""

Print(output.text)

"""GIVES HTTP RESPONSE"""
