#!/usr/bin/python3
"""top ten function"""
import requests


def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on subreddit"""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "0x16-api_advanced:project:\

    }
    params = {
        "limit": 10
    }
    resp = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if resp.status_code == 404:
        print("None")
        return
    results = resp.json().get("data")
    [print(c.get("data").get("title")) for c in results.get("children")]
