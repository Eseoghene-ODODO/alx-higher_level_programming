#!/usr/bin/python3
"""
Python script that takes 2 arguments in order to solve this challenge.
"""
import requests
import sys


if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo)
    response = requests.get(url)
    data = response.json()
    for commit in data[:10]:
        sha = commit.get("sha")
        name = commit.get("commit").get("author").get("name")
        print("{}: {}".format(sha, name))
