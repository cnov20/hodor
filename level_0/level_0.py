#!/usr/bin/python
import requests

URL = 'http://54.221.6.249/level0.php'
headers = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp'
payload = {'id': '128', 'holdthedoor': 'submit'}

for i in range(1024):
    r = requests.post(URL, data=payload)
