import schedule
import time
import praw
import csv

def scrape_rfl_scores():
    reddit = praw.Reddit(client_id='yeah nah',
                         client_secret='nopee',
                         password='defo no',
                         user_agent='nooo',
                         username='PelotonMod')

    submission = reddit.submission("fekwtl")

    submission.comments.replace_more(limit=0)
    for top_level_comment in submission.comments:
        print(top_level_comment.author),
        print(top_level_comment.body)

schedule.every().sunday.at("10:20").do(scrape_rfl_scores)

while True:
    schedule.run_pending()
    time.sleep(1)