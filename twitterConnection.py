import requests
import tweepy
import pandas
import json
ApiKey = 'tMyPK26T4fUaBpPqYvvRMLVxR'
ApiSecretKey = 'e7hxgFvgDEw5I9e4bSLsMrE2ilTQ4CN0LwPjAG2YOWMlz2LY3M'
access_token = '879601750830972928-x1sNiUtHCjAamveIhXj0GpG7h9ujV8T'
access_token_secret = '3Wn7SGynXEPNSd4w8xHmrZCehmbRvSQbLXZRxi98imi0K'
BearerToken = 'AAAAAAAAAAAAAAAAAAAAAGiKMwEAAAAAWWaRZI95ykmtiOmnoJDOp5eQLVs%3DUPfxzeXvED2ONvwqP4KB8zOeNvP1qZo6ltUlmx5aIysqFgigi3'


auth = tweepy.OAuthHandler(ApiKey, ApiSecretKey)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# retrieve data from twitter
tweetDictionary = {
    'Date': '',
    'tweetText': '',
}


def twitterSearch(topic, count):
    tweetObject = api.search(topic, lang='en', count=count)
    tweets = tweetObject[0]
    json_str = json.dumps(tweets._json)
    print(tweetDictionary)
    print(json_str)
    for i in tweetObject:
        # print(i.text)
        # print(i.created_at)
        tweetDictionary.update({'Date': i.created_at, 'tweetText': i.text})
    print(tweetDictionary)
    print('the tweet Dictionary Length is: ')
    print(len(tweetDictionary))
