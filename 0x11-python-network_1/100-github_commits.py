#!/usr/bin/python3
#  Python script that takes in a URL and an email, sends a POST request
# to the passed URL with the email as a parameter, and displays the
# body of the response
import requests
import sys

if __name__ == "__main__":

    url = "https://api.github.com/repos/{}/{}/commits"
    url = url.format(sys.argv[2], sys.argv[1])

    req = requests.get(url)
    response = req.json()
    for resp in response[:10]:
        print("{}: {}".format(resp['sha'], resp['commit']['author']['name']))
