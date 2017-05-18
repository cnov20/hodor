#!/usr/bin/python
import requests

URL = 'http://54.221.6.249/level2.php/User-Agent'
payload = {'id': '128', 'holdthedoor': 'Submit', 'key': '0'}

cookies = {'HoldTheDoor': '0'}
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'}
r = requests.get(URL, headers=headers)
jar = requests.cookies.RequestsCookieJar()

r.cookies['HoldTheDoor']


for i in range(2):
    r = requests.post(URL, data=payload, cookies=cookies, headers=headers)
    print (r.content)
