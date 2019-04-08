import requests
from pprint import pprint


url = 'https://api.yelp.com/v3/businesses/search'
header = {"authorization":"Bearer olKwlvmMEzLVdtZ4gMtTR2n3foi3KPNkwkfPRXMqK1-TyUK6_tiwPRFRKdQJLVPHXyujYSZ7tJxQA4HNehK2JkTtkK8NvdoSifhxiLhGeeXbiX19QdbH8Aucm5GqXHYx"}
params = {"term":"restaurants",
 "location":"MO 64111",
 "radius": 4280,
 "limit": 10,
 "open_now":"true"}

resp = requests.get(url=url, headers=header, params=params)
data = resp.json()

for key, value in data.items():
    if key == 'error':
        print('there was an error')
    else:
        list = []
        for name in data['businesses']:
            list.append(name['name'])
        print(list)
        break

