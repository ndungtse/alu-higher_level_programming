#!/usr/bin/python3
"""Lists up to 10 commits of a GitHub repository, newest first."""
import requests
import sys


if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo)
    response = requests.get(url)
    try:
        for commit in response.json()[:10]:
            print("{}: {}".format(
                commit.get("sha"),
                commit.get("commit").get("author").get("name")))
    except (TypeError, KeyError):
        pass
