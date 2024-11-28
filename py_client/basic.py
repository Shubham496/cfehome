import requests
endpoint = "http://localhost:8000/api/"

get_response = requests.post(endpoint, json={"title": "hello world"})  
print("Status Code:", get_response.status_code)

print("Response json:", get_response.json())
