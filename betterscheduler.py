import schedule
import time
import praw
import csv

def scrape_rfl_scores():
    reddit = praw.Reddit(client_id='nope',
                         client_secret='nope',
                         password='nope',
                         user_agent='nope',
                         username='PelotonMod')

    submission = reddit.submission("fekwtl")

    submission.comments.replace_more(limit=0)
    for top_level_comment in submission.comments:
        with open('paris_nice_picks.csv', 'wb+') as csvfile:
            pickswriter = csv.writer(csvfile, delimiter =' ')
            pickswriter.writerows(top_level_comment.author),
            pickswriter.writerows(top_level_comment.body)

schedule.every().wednesday.at("12:59").do(scrape_rfl_scores)

while True:
    schedule.run_pending()
    time.sleep(1)