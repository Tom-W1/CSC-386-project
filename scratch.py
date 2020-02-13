import praw
from praw.models import MoreComments
import pandas as pd
import datetime as dt
reddit = praw.Reddit(client_id='h75002hxSddmJA',
                     client_secret='u7ajMK2vTr5lI9UEUu2V87fTaTE',
                     user_agent='Scape_ee',
                     username='Krost303',
                     password='Freedom303!!')


def save_submissions():
    """
    Run through Top submissions of the 'depression' subreddit while collecting
    the title, body, and author of post
    :return: df
    """
    red_all = reddit.subreddit('depression').top(limit=1000)
    depression_dict_all_info = {"title": [],
            "body": [],
            "subreddit": []}

    for submission in red_all:
        depression_dict_all_info["title"].append(submission.title)
        depression_dict_all_info['subreddit'].append(submission.subreddit)
        depression_dict_all_info['body'].append(submission.selftext)

    df = pd.DataFrame(dict)
    df.to_csv('Freedom.csv')
    return df


def process_submissions():
    """
    Looks at the title of the post and checks if it has a '!' in it
    if it has one then it adds to a counter. At the end it prints the number
    of posts with '!' in the title
    :return:
    """
    df = pd.read_csv('Freedom.csv')
    num_subs = len(df["subreddit"])
    diction = {}
    ary = {}
    for i in range(num_subs):
        title = df['title'][i]
        sub = df["subreddit"][i]
        ary[sub] = ary.get(sub, 0)+title.count('!')
        diction[sub] = diction.get(sub, 0)+1
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



