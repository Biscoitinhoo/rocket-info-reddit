from credentials.api_keys import APIKeys

subreddit = APIKeys.reddit.subreddit('TrainingBots')
hot_posts = subreddit.hot(limit=5)

already_answered = None

for post in hot_posts:
    if not post.stickied:

        # getting all comments
        for comment in post.comments:
            # someone mentioned a rocket!
            if 'falcon 1' in comment.body:
                for reply in comment.replies:
                    if reply.body == 'Falcon 1 informations!':
                        already_answered = True
                    else:
                        already_answered = False
                if not already_answered:
                    comment.reply('Falcon 1 informations!')
                else:
                    print('I already answered about Falcon 1.')

                already_answered = False

print('bot shutdown.')
