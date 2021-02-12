import praw
from service.service import Service

# reddit credentials
reddit = praw.Reddit(
    client_id='x',
    client_secret='x',
    username='x',
    password='x',
    user_agent='x',
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
def answer_about(ask):
    if ask == 'falcon 1':
        print('Someone asked about Falcon 1! :D')

        mention.reply('Falcon 1 information!')
        mention.mark_read()
        print("Answered it!")

    if ask == 'falcon 9':
        print('Someone asked about Falcon 9! :D')

        if get_rocket('falcon 9').name != '':
            # worked!!!
            mention.reply(
                '>Name: ' + str(get_rocket('falcon 9').name) + '    \n' +
                '    \n' +
                '>Cost per launch: $' + str(get_rocket('falcon 9').cost_per_launch) + '    \n' +
                '    \n' +
                '>Description: ' +
                str(get_rocket('falcon 9').description) + '    \n'
            )
            mention.mark_read()
            print("Answered it!")


post_number = 1
# getting all subreddit posts
for post in hot_posts:
    if not post.stickied:

        print("I'm going try to find someone needing help with the " +
              str(post_number) + "º post(s).")
        # getting all unread mentions
        for mention in reddit.inbox.unread(limit=None):
            user_request = str(mention.body).lower()

            if user_request == asking_about('falcon 1'):
                answer_about('falcon 1')
            if user_request == asking_about('falcon 9'):
                answer_about('falcon 9')
    post_number += 1

print('That is! I am going to turn off... :/')
