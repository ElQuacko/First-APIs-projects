import requests
import pygal

url = 'https://swapi.co/api/films'
r = requests.get(url)
print("Status code:", r.status_code)

responseStorageDict = r.json()

repoDicts = responseStorageDict['results']

title, episode_id, director, release_date = [], [], [], []

for repoDict in repoDicts:
    title.append(repoDict['title'])
    episode_id.append(repoDict['episode_id'])
    release_date.append(repoDict['release_date'])
    director.append(repoDict['director'])

    print('\n\nTitle:', repoDict['title'])
    print('Number of the episode:', repoDict['episode_id'])
    print('Date of premiere:', repoDict['release_date'])
    print('Director:', repoDict['director'])
