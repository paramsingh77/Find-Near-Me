import requests

url = 'http://localhost:8080/api/nearby-location/restaraunt'

data = {
    "latitude": 37.7749,
    "longitude": -122.4194,
    "category": "restaraunt",
}

try:
    response = requests.post(url, json=data)
    response.raise_for_status() 
    json_data = response.json()
    print(json_data)
except requests.exceptions.HTTPError as errh:
    print(f"HTTP Error: {errh}")
except requests.exceptions.ConnectionError as errc: