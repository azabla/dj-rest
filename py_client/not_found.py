import requests

endpoint = "http://localhost:8000/api/products/1231342314324"

get_response = requests.get(endpoint)
print(get_response.json())
