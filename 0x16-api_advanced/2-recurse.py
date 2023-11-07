#!/usr/bin/python3
"""A recursive function that queries the Reddit API"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Returns a list containing the titles of all hot articles
    for a given subreddit
    """

    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=100'

    if after:
        url += f'&after={after}'

    headers = {'User-Agent': 'API-Client'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        posts = response.json()['data']['children']

        for post in posts:
            title = post['data']['title']
            hot_list.append(title)

        after = data['data']['after']
        if after:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    else:
        return None
