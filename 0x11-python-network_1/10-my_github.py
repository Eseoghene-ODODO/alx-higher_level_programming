#!/usr/bin/python3
"""
Write a Python script that takes your GitHub credentials
(username and password)
and uses the GitHub API to display your id
"""
import requests
import sys


if __name__ == "__main__":
    url = 'https://api.github.com/user'
    username = sys.argv[1]
    password = sys.argv[2]
    response = requests.get(url, auth=(username, password))
    if response.status_code == 200:
        print(response.json()["id"])
    else:
        print("None")
