from math import floor
from datetime import datetime

from create import create_client
reddit = create_client()

dis = 86400 # 60*60*24
ytos = 31536000

submissions = ['k17917']

# for submission in submissions:
    # submission = reddit.submission(submission)
for submission in reddit.subreddit('cakeday').new():
    author = submission.author


    years_f = (submission.created_utc - author.created_utc) / ytos
    years_int = floor(years_f)

    hours = (years_f - years_int) * 365 * 24
    
    
    if 364 >= hours >= (3*24):
        body = (f'u/{author.name} | '
                f'age: {years_int} year(s), {round(hours, 2)} hours / {round(hours/24, 2)} days | '
                f'submission utc: {datetime.utcfromtimestamp(int(submission.created_utc))} | '
                f'author utc: {datetime.utcfromtimestamp(int(author.created_utc))}'
                f'\n https://reddit.com{submission.permalink}')

        reddit.redditor('endercheif').message(subject='cakeday post', message=body)
        print(body)
