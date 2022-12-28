import twint
from datetime import datetime, timedelta


client = twint.Config()


def read_tweets(search, username=None, limit=30, since_mins=30, store=True, output=None, lang=None, geo=None):
    now = datetime.now()
    filename = f"./data/search_{now.strftime('%Y-%m-%d_%H:%M:%S')}.csv"
    client.Search = search
    if username:
        client.Username = username
    client.Limit = limit
    client.Store_csv = store
    # client.Since = (now - timedelta(minutes=since_mins)).strftime('%Y-%m-%d %H:%M:%S')
    client.Verified = True
    client.Popular_tweets = True
    if output:
        client.Output = output
    else:
        client.Output = filename
    if lang:
        client.Lang = lang
    if geo:
        client.Geo = geo

    twint.run.Search(client)


read_tweets(['#ADANI'])
