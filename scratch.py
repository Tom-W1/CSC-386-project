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
    print(brain)
    return brain


def print_submission_comments():
    auth_com = []
    author = ""
    comment= ""
    for subs in bb_plays:
        comments = subs.comments
        for auth in comments:
            author = auth.author
            comment = auth.body
            auth_com.append(author.__str__()+':' + comment)
    print(auth_com)


def save_submissions():
    red_all = reddit.subreddit('depression').top(limit=1000)
    dict = {"title":[],
            "body":[],
            "subreddit":[]}

    for submission in red_all :
        dict["title"].append(submission.title)
        dict['subreddit'].append(submission.subreddit)
        dict['body'].append(submission.selftext)

    df = pd.DataFrame(dict)
    df.to_csv('Freedom.csv')
    return df


def process_submissions():
    df = pd.read_csv('Freedom.csv')
    num_subs = len(df["subreddit"])
    diction = {}
    ary = {}
    for i in range(num_subs):
        title = df['title'][i]
        sub = df["subreddit"][i]
        ary[sub] = ary.get(sub, 0)+title.count('!')
        diction[sub] = diction.get(sub,0)+1
    subs = list(diction.items())
    subs.sort(key=lambda x: x[1], reverse=True)
    mos_sub = subs[:10]
    print(subs)
    print(mos_sub)
    for (k, v) in mos_sub:
        print(str(ary.get(k)) + ':' + k)


def main():
    save_submissions()
    process_submissions()


if __name__ == '__main__':
    main()



