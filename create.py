from json import load
from praw import Reddit


def create_client(filename='creds.json'):
    with open(filename, 'r') as file:
        creds = load(file)

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

    return reddit
