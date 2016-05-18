import requests
import json

url = 'http://172.16.207.20/api/status'
method = 'GET'
response = requests.request(method, url)
payload = json.loads(response.content)
print payload['code']