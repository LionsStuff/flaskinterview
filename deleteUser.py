import requests

res = requests.post("http://127.0.0.1:5000/delete",json={"name":"Leo", "surname":"Guzman", "username":"Usuario", "email":"Email", "password":"3546789"})

print(res.json())