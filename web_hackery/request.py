import requests

url = 'https://boodelyboo.com'
response = request.get(url) #GET

data = {'user': 'tim', 'passwd':'12345'}

respose = request.post(url, data=data) #POST

print(response.text) #response.text = str
response.content = bytesting

