#!/usr/bin/python3
'''queries the Reddit API and returns the number of subscribers
(total subscribers) for a given subreddit.'''
import requests


def number_of_subscribers(subreddit):
    '''Return information about the subreddit.
    Data includes the subscriber count.'''
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {
        'User-Agent':
        'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:96.0) \
        Gecko/20100101 Firefox/96.0'
    }
    response = requests.get(url, headers=headers)

    try:
        res = response.json()
        return res['data']['subscribers']
    except:
        return 0
