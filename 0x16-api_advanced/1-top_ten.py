#!/usr/bin/python3
''' queries the Reddit API and prints the titles of the
first 10 hot posts listed for a given subreddit.'''
import requests


def top_ten(subreddit):
    ''''''
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {
        'User-Agent':
        'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:96.0) \
        Gecko/20100101 Firefox/96.0'
    }
    response = requests.get(url, headers=headers)

    try:
        res = response.json()
        path = res['data']['children']
        for idx in range(10):
            print(path[idx]['data']['title'])
    except:
        print("non-existent subreddit")
