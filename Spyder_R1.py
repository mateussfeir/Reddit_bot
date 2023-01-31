# Run using anaconda spyder

import praw
import random
import time

reddit = praw.Reddit(
    # Thats to run the app
    client_id="6A1g1_iNBW41SBm17ZgfmQ",
    client_secret="3_KU7BhrqUrb4u1Igj77-avepnfHkA",
    user_agent="<console:HAPPY:1.0>",
    username="Aggravating_Cycle652",
    password="19942009Dd@",
)

subreddit = reddit.subreddit("Television")


sad_quotes = ['Do not be sad','life is short to be sad','lets be happy again']


for submission in subreddit.hot(limit=10):
    print('-------------Title---------------')
    print(submission.title)
    
    for comment in submission.comments:
        if hasattr(comment,"body"):
            comment.lower = comment.body.lower()
            if " sad " in comment.lower:
                print('------Comment-------')
                print(comment.body)
                random_index = random.randint(0, len(sad_quotes) - 1)
                comment.reply(sad_quotes[random_index])
                time.sleep(5)
