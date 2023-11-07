#!/usr/bin/python3
"""A recursive function that queries the Reddit API"""
import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """
    Parses the title of all hot articles,
    and prints a sorted count of given keywords
    """
    if counts is None:
        counts = {}

    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=100'

    if after:
        url += f'&after={after}'

    headers = {'User-Agent': 'API-Client'}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        posts = response.json()['data']['children']

        for post in posts:
            title = post['data']['title'].lower()
            for word in word_list:
                word = word.lower()
                if f' {word.lower()} ' in f' {title} ':
                    if word not in counts:
                        counts[word] = 1
                    else:
                        counts[word] += 1

        after = response.json()['data']['after']
        if after:
            return count_words(subreddit, word_list, after, counts)
        else:
            sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_counts:
                print(f'{word}: {count}')
    else:
        return None
