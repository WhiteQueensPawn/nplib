"""
telnet 23 \n
dns 53 \n
http 80 \n
ssh 443 \n
"""

import requests

r = requests.get('https://www.google.com')
print r.status_code
