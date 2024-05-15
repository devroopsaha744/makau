import requests

response=requests.post(
    "http://localhost:8000/blog-gen/invoke",
    json={'input':{'topic':"Dijkstra's Algorithm"}})

print(response.json())

