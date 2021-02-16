from typing import Any

from model.rocket import Rocket
from strings.rocket_strings import RocketStrings
from service.service import Service


class Reply:

    def reply_about(self, message, mention: Any, rocket: Rocket):
        print(self)

        if message == RocketStrings._help:
            print('Someone need help.')
            answer_help(mention)
            print('I helped someone 1 :)')

        if message == RocketStrings.falcon_9:
            print('Someone asked about Falcon 9.')
            answer_about_falcon_9(mention, rocket)
            print('Answered.')

        if message == RocketStrings.falcon_1:
            print('Someone asked about Falcon 1.')
            answer_about_falcon_1(mention, rocket)
            print('Answered.')

        if message == RocketStrings.falcon_heavy:
            print('Someone asked about Falcon Heavy.')
            answer_about_falcon_heavy(mention, rocket)
            print('Answered.')

        mention.mark_read()

    ### answers ###

    # invalid rocket
    def rocket_doesnt_exists(self, mention):
        print(self)
        mention.reply(
            '>I am sorry, but I did not found anything about this... Just mention me and I will tell you the things I know! ;)')
        mention.mark_read()
        print("Someone mentioned a rocket that I do not know...")


# help
def answer_help(self, mention: Any):
    print(self)
    mention.reply(
        ">Here is your help manual"
    )
    mention.mark_read()


# rockets
def answer_about_falcon_9(mention, rocket: Rocket):
    mention.reply(
        '>Name: ' + str(rocket.name) + '    \n' +
        '    \n' +
        '>Cost per launch: $' + str(rocket.cost_per_launch) + '    \n' +
        '    \n' +
        '>Description: ' +
        str(rocket.description) + '    \n'
    )


def answer_about_falcon_1(mention, rocket: Rocket):
    mention.reply(
        '>Name: ' + str(rocket.name) + '    \n' +
        '    \n' +
        '>Cost per launch: $' + str(rocket.cost_per_launch) + '    \n' +
        '    \n' +
        '>Description: ' +
        str(rocket.description) + '    \n'
    )


def answer_about_falcon_heavy(mention, rocket: Rocket):
    mention.reply(
        '>Name: ' + str(rocket.name) + '    \n' +
        '    \n' +
        '>Cost per launch: $' + str(rocket.cost_per_launch) + '    \n' +
        '    \n' +
        '>Description: ' +
        str(rocket.description) + '    \n'
    )
