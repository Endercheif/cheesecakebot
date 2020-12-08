import os
from json import loads, load
from praw import Reddit


def create_client(filename='creds.json'):
    error = KeyError('Key REDDIT not found')
    creds = os.environ.get('REDDIT')

    if creds:
        creds = loads(creds)
    else:
        try:
            with open(filename, 'r') as file:
                creds = load(file)
        except FileNotFoundError:
            raise error



    client_id = creds["client_id"]
    client_secret = creds["client_secret"]
    user_agent = creds["user_agent"]
    username = creds["username"]
    password = creds["password"]

    reddit = Reddit(client_id=client_id,
                    client_secret=client_secret,
                    user_agent=user_agent,
                    username=username,
                    password=password)

    return reddit, creds