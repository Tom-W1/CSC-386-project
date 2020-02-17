import praw  # PRAW is the "Python Reddit API Wrapper"
from praw import reddit
from praw.models import MoreComments
import pandas as pd # Pandas Data Frames
from gensim import corpora


reddit_instance = praw.Reddit(user_agent='reddit_386',
                             client_id='Gvg76shTFZumlQ', client_secret="CRv9HJSmJUomaoBR3QXH9MXRudc",
                             username='Newb_Masster_69', password='Berea386!')

def save_submissions():
    my_sub = reddit_instance.subreddit('depression')
    wow = my_sub.hot(limit=10)
    dict = {"author":[],
        "title": [],
            "body":[],
            "commentauth":[],
            "comments":[],
            "subreddit": [],
            }
    for submission in wow:
        rcomments = submission.comments
        rtitle = submission.title
        rsubreddit = submission.subreddit
        rauthor = submission.author
        #rcommentauth = submission.comments.auth
        rbody = submission.selftext
        #print(rsubreddit)
        #print("***NEW POST*** ",submission.author, submission.score, submission.title )
        dict["author"].append(rauthor)
        dict["title"].append(rtitle)
        #dict["body"].append(rbody)
        #dict["commentauth"].append(rcommentauth)
        dict["comments"].append(rcomments)
        #for top_level_comments in rcomments:
            #dict["commentauth"].append(rcommentauth, top_level_comments.body)
            #rauth = top_level_comments.author
            #rcomm = top_level_comments.body
            #print(top_level_comments.author,"'", top_level_comments.score, "'", top_level_comments.body)
            #dict["commentauth"].append(top_level_comments.author)
            #dict["comments"].append(rcomm)
    texts = [[text for text in doc.split()] for doc in dict]

# Create dictionary
    print(dict)
    dictionary = corpora.Dictionary(texts)
    print(dictionary)
    print(dictionary.token2id)


def main():

    save_submissions()
    #process_submission()

if __name__ == '__main__':
    main()