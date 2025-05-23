import requests

endpoint = "http://localhost:8000/api/"

get_response =  requests.post(endpoint, json={'title': "hello world"}, params={'abc':123}) # API > Application programming interface

# REST APIS - > WEB API
# print(get_response.text) # raw text


print(get_response.text)

print(get_response.status_code)
print(get_response.json())



