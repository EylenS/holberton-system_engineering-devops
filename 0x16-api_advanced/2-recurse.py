#!/usr/bin/python3
'''A recursive function that queries the Reddit API and
returns a list containing the titles of all hot articles
for a given subreddit.'''
import requests


def recurse(subreddit, hot_list=[], after=None):
    ''''''
    url = 'https://www.reddit.com/r/{}/hot.json?after={}'.format(
        subreddit, after)
    headers = {
        'User-Agent':
        'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:96.0) \
        Gecko/20100101 Firefox/96.0'
    }

    try:
        response = requests.get(url, headers=headers)
        res = response.json()
        path = res['data']['children']
        for idx in range(len(path)):
            hot_list.ppend(path[idx]['data']['title'])
        after = res['data']['after']
        if after is None:
            return hot_list
        return recurse(subreddit, hot_list, after)
    except:
        return None
