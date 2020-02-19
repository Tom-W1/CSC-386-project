import praw
from praw.models import MoreComments
import pandas as pd
import datetime as dt
reddit = praw.Reddit(client_id='h75002hxSddmJA',
                     client_secret='u7ajMK2vTr5lI9UEUu2V87fTaTE',
                     user_agent='Scape_ee',
                     username='Krost303',
                     password='Freedom303!!')


def save_title_submission():
    """
    saves the title of the first thousand post of the depression reddit sorted by top for manipulation
    : return: df
    """
    red_depress = reddit.subreddit('depression').top(limit=1000)
    depression_dict_title = {"title": []}

    for submission in red_depress:
        depression_dict_title['title'].append(submission.title)

    df = pd.DataFrame(depression_dict_title)
    df.to_csv('post_title_text.csv')
    return df


def save_auth_submission():
    """
    saves the authors of the first thousand post of the depression reddit sorted by top for manipulation
    : return: df
    """
    red_depress = reddit.subreddit('depression').top(limit=1000)
    depression_dict_author = {"author": []}

    for submission in red_depress:
        depression_dict_author['author'].append(submission.author)

    df = pd.DataFrame(depression_dict_author)
    df.to_csv('post_author.csv')
    return df


def save_body_submission():
    """
    saves the body of the first thousand post of the depression reddit sorted by top for manipulation
    : return: df
    """
    red_depress = reddit.subreddit('depression').top(limit=1000)
    depression_dict_body = {"body": []}

    for submission in red_depress:
        depression_dict_body['body'].append(submission.selftext)

    df = pd.DataFrame(depression_dict_body)
    df.to_csv('post_body_text.csv')
    return df


def save_submissions():
    """
    Run through Top submissions of the 'depression' subreddit while collecting
    the title, body, and author of post
    :return: df
    """
    red_all = reddit.subreddit('depression').top(limit=1000)
    depression_dict_all_info = {"title": [],
            "body": [],
            "redditor":[]}

    for submission in red_all:
        depression_dict_all_info["title"].append(submission.title)
        depression_dict_all_info['redditor'].append(submission.author)
        depression_dict_all_info['body'].append(submission.selftext)

    df = pd.DataFrame(depression_dict_all_info)
    df.to_csv('total_submission_info.csv')
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
    save_body_submission()
    save_auth_submission()
    save_title_submission()


if __name__ == '__main__':
     main()



