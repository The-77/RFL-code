import schedule
import time
import praw
import csv

def scrape_rfl_scores():
    reddit = praw.Reddit(client_id='nope', #input the correct bits of info here for it to run
                         client_secret='nope',
                         password='nope',
                         user_agent='nope',
                         username='PelotonMod')

    submission = reddit.submission("fekwtl") #the six characters after https://www.reddit.com/r/subreddit/comments/

    submission.comments.replace_more(limit=0)
    for top_level_comment in submission.comments:
        with open('paris_nice_picks.csv', 'a+', encoding='utf-8', newline='') as csvfile: #choose 'something_picks.csv' as your name
            pickswriter = csv.writer(csvfile, dialect='excel', delimiter =' ')
            pickswriter.writerow(top_level_comment.author.name),
            pickswriter.writerow(top_level_comment.body)
            print(top_level_comment.author) #prints a list of authors who submitted on time

schedule.every().wednesday.at("14:11").do(scrape_rfl_scores) #time & date of the submission time in your local PC time

while True:
    schedule.run_pending()
    time.sleep(1)
    
    
#when opening the file, tick the other box under separated by and put " in
#make sure to use " as the text delimiter too
#also keep it in Unicode (UTF-8)
