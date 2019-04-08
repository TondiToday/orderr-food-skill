from mycroft import MycroftSkill, intent_file_handler
from adapt.intent import IntentBuilder
import requests

url = 'https://api.yelp.com/v3/businesses/search'
header = {"authorization":"Bearer olKwlvmMEzLVdtZ4gMtTR2n3foi3KPNkwkfPRXMqK1-TyUK6_tiwPRFRKdQJLVPHXyujYSZ7tJxQA4HNehK2JkTtkK8NvdoSifhxiLhGeeXbiX19QdbH8Aucm5GqXHYx"}

def find_restaurants(place):
    params = {"term": "restaurants",
              "location": place,
              "radius": 4280,
              "limit": 10,
              "open_now": "true"}
    resp = requests.get(url=url, headers=header, params=params)
    data = resp.json()
    for key, value in data.items():
        if key == 'error':
            list = ['error']
        else:
            list = []
            for name in data['businesses']:
                list.append(name['name'])
            print(list)
            break
    return list


class FindRestaurant(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    # Find closest restaurants
    @intent_file_handler('food.orderr.intent')
    def finding_restaurant(self, message):
        restaurants = find_restaurants(message.data['place'])
        if restaurants == 'error':
            self.speak_dialog('ThePlaceWasNotFound')
        else:
            self.speak_dialog('place')
            for item in restaurants:
                self.speak(item)

def create_skill():
    return FindRestaurant()

