import praw
from praw.models import MoreComments
import pandas as pd
import datetime as dt
reddit = praw.Reddit(client_id='h75002hxSddmJA',
                     client_secret='u7ajMK2vTr5lI9UEUu2V87fTaTE',
                     user_agent='Scape_ee',
                     username='Krost303',
                     password='Freedom303!!')
big_brain = reddit.subreddit('Futurology')
bb_plays = big_brain.hot(limit=1)



def get_submission():
    brain = []
    for i in bb_plays:
        brain.append(i.title)
    print (brain)


    return brain

def save_submissions():
    red_all = reddit.subreddit('depression').top(limit = 1000)
    dict =        { "title":[],
                    "body":[],
                "subreddit":[]}


    for submission in red_all :
        dict["title"].append(submission.title)
        dict['subreddit'].append(submission.subreddit)
        dict['body'].append(submission.selftext)

    df = pd.DataFrame(dict)
    df.to_csv('Freedom.csv')
    return df


def main():
    save_submissions()
if __name__ == '__main__':
     main()



