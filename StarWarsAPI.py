import requests

url = 'https://swapi.co/api/films'
r = requests.get(url)
print("Status code:", r.status_code)

responseStorageDict = r.json()
