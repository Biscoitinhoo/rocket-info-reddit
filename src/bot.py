import praw

from model.rocket import Rocket
from service.service import Service
from strings.rocket_strings import RocketStrings

from controller.controller import Controller
from reply.reply import Reply

# reddit credentials
reddit = praw.Reddit(
    client_id='',
    client_secret='',
    username='',
    password='',
    user_agent='',
)

# initial configs
subreddit = reddit.subreddit('TrainingBots')
hot_posts = subreddit.hot(limit=None)


# http requests


def get_rocket(name):
    return Service.get_rocket(name)


# prefix (already lowercase)
def asking_about(ask):
    return "u/rocketinfo " + ask


# collections of replies
def answer_about(message, mention):

    reply = Reply()
    controller = Controller()

    rocket = get_rocket(message)

    if message == RocketStrings._help:
        reply.reply_about(RocketStrings._help, mention)

    if controller.is_valid_rocket(rocket):
        reply.reply_about(message, mention, rocket)


def main():

    post_number = 1
    # getting all subreddit posts
    for post in hot_posts:
        if not post.stickied:

            print("I'm going try to find someone needing help with the " +
                  str(post_number) + "º post(s).")
            # getting all unread mentions
            for mention in reddit.inbox.unread(limit=None):
                user_request = str(mention.body).lower()

                # help message
                if user_request == asking_about(RocketStrings._help):
                    answer_about(RocketStrings._help, mention)
                    return
                # rocket messages
                if user_request == asking_about(RocketStrings.falcon_1):
                    answer_about(RocketStrings.falcon_1, mention)
                    return
                if user_request == asking_about(RocketStrings.falcon_9):
                    answer_about(RocketStrings.falcon_9, mention)
                    return
                if user_request == asking_about(RocketStrings.falcon_heavy):
                    answer_about(RocketStrings.falcon_heavy, mention)
                    return

                # else...
                reply = Reply()
                reply.rocket_doesnt_exists(mention)

        post_number += 1

    print('That is! I am going to turn off... :/')


if __name__ == "__main__":
    main()
