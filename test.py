import requests
from requests.api import head

url = 'http://127.0.0.1:5000/asr'
data = open('male.wav', 'rb')
file = {'file': data}
headers = {'content-type': 'audio/wav'}

r = requests.post(url, files=file)

print(r)
print(r.text)
