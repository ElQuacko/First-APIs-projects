#Project from E. Matthes book "Python Crash Course"

import requests

from operator import itemgetter

#Make an API call and store the reponse
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print("Status code:", r.status_code)

#Process information about each submission and convert response to the list
submission_ids = r.json()
#Set up of empty list to store dictionaries
submission_dicts = []

for submission_id in submission_ids[:30]:
    #Make a separate API call for each submission
    url = ('https://hacker-news.firebaseio.com/v0/item/' + str(submission_id) + '.json')
    submission_r = requests.get(url)
    #Classy, we print status of response
    print(submission_r.status_code)
    response_dict = submission_r.json()

    submission_dict = {
        'title' : response_dict['title'],
        'link' : 'http://news.ycombinator.com/item?id=' + str(submission_id),
        #Comments are stored in the dictionary, dict.get() is super useful, cause if some data does not exist it will print
        #alternative value so in that case it is 0
        'comments' : response_dict.get('descendants', 0)
    }
    submission_dicts.append(submission_dict)

#itemgetter() sorts the list
submission_dicts = sorted(submission_dicts, key = itemgetter('comments'), reverse = True)

for submission_dict in submission_dicts:
    print("\nTitle:", submission_dict['title'])
    print("Discussion link:", submission_dict['link'])
    print("Comments:", submission_dict['comments'])
