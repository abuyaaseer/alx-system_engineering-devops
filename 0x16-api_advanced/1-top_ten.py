#!/usr/bin/python3
"""Contain top_ten function"""
import requests


def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on a subreddit."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "0x16-api_advanced:project:\
v1.0.0 (by /u/firdaus_cartoon_jr)"
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
