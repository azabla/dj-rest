import requests


endpoint = "http://localhost:8000/api/"

get_response = requests.post(
    endpoint, params={"abc": 123}, json={"title": "hello world"}
)

print(get_response.json())
