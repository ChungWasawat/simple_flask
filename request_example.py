import requests

data = {
    "id":"abc", 
    "name": "kongtiao", 
    "price": 27999, 
    "quantity": 2  }

url = 'http://localhost:9696/home'
response = requests.post(url, json=data)
print(response.json())