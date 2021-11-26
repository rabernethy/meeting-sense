# server_test.py written By Russell Abernethy
# Written for Smart Sensors Class

import requests
from requests.api import head

filename = 'no-thats-not-gonna-do-it.wav'
url = 'http://127.0.0.1:5000/asr'
data = open(filename, 'rb')
file = {'file': data}
headers = {'content-type': 'audio/wav'}

r = requests.post(url, files=file)

print(r)
print(r.text)
