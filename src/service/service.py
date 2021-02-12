import requests
from model.rocket import Rocket


class Service:

    # return a empty object if rocket don't exists.
    @staticmethod
    def get_rocket(name):
        CONST_BASE_URL = 'https://api.spacexdata.com/v4'

        request = requests.get(CONST_BASE_URL + '/rockets')
        all_rockets = request.json()

        for rocket in all_rockets:
            if name.lower() == rocket['name'].lower():
                return Rocket(rocket['name'], rocket['cost_per_launch'], rocket['description'])
