#!/usr/bin/python3
"""A function that queries the Reddit API"""
import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts listed for a given subreddit
    """

    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    headers = {'user-agent': 'API-Client'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        posts = response.json()['data']['children']
        for post in posts:
            title = post['data']['title']
            print(title)
    else:
        print(None)
