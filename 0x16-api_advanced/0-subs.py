#!/usr/bin/python3
"""
This module defines a function to get the number of subscribers for a given subreddit
using the Reddit API.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a given subreddit.
    If an invalid subreddit is given, returns 0.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        int: Number of subscribers or 0 if the subreddit is invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'custom-user-agent'}
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data.get('data', {}).get('subscribers', 0)
        else:
            return 0
    except requests.RequestException:
        return 0
    except ValueError:
        return 0
