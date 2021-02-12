from model.rocket import Rocket
from strings.rocket_strings import RocketStrings


class Controller:

    def is_valid_rocket(self, rocket: Rocket):
        print(self)
        # if an invalid rocket was called, then an empty object
        # will be returned. so if some property are empty, the rocket
        # are invalid.
        return rocket.name != None
