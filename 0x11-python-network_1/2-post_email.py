#!/usr/bin/python3
"""
A script that takes in a URL and an email, sends a POST request to the passed
URL with the email as a parameter, and displays the body of the response
(decoded in utf-8)
"""

import urllib.request
import urllib.parse
import sys


def post_email(url, email):
    """ function to post a mail """

    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        if response.status == 200:
            print(response.read().decode('utf-8'))
        else:
            print("Error: Status code ", response.status)
            if response.status >= 400 and response.status < 500:
                return
            else:
                post_email(url, email)


if len(sys.argv) != 3:
    print("Usage: {} URL EMAIL".format(sys.argv[0]))
else:
    url = sys.argv[1]
    email = sys.argv[2]
    post_email(url, email)
