import requests

API_URL = "http://shibe.online/api/shibes"

params = {"count": 10}

response = requests.get(API_URL, params)

status_code = response.status_code
print(f"Status code: {status_code}")

response_json = response.json()

for url in response_json:
    print(url)
    print()
