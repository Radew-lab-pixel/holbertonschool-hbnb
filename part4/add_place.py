import requests

url = "http://localhost:5001/api/v1/places"
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc0NTczNzI0OSwianRpIjoiMGZhNmVjMzktZTI0ZC00MGFhLThiZjUtYWJhOWI1NGJiNjQ5IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6eyJpZCI6ImExYjJjM2Q0LWU1ZjYtNzg5MC1hYmNkLWVmMTIzNDU2Nzg5MCIsImlzX2FkbWluIjpmYWxzZX0sIm5iZiI6MTc0NTczNzI0OSwiY3NyZiI6ImEzN2NmMWNkLWU2NDEtNDRiMy1iYjgwLTk2ODQ2YzBhMmFiNyIsImV4cCI6MTc0NTczODE0OX0.ZPCdCXpCD9tVlownsn5fW2xIlVt3V53IgWeCs-u_s3I"
}
data = {
    "title": "New Test Place",
    "description": "Another nice place",
    "price": 150.0,
    "latitude": 37.7749,
    "longitude": -122.4194
}

response = requests.post(url, headers=headers, json=data)
print(response.status_code)
print(response.json())