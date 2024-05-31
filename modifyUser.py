import requests

res = requests.post("http://127.0.0.1:5000/modify?email=Email",json={"name":"Gael"})

print(res.json())