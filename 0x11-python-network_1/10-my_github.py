#!/usr/bin/python3
#  Python script that takes in a URL and an email, sends a POST request
# to the passed URL with the email as a parameter, and displays the
# body of the response
import requests
import sys

if __name__ == "__main__":

    url = 'https://api.github.com/user'
    usr = sys.argv[1]
    pwd = sys.argv[2]

    req = requests.get(url, auth=(usr, pwd))
    resp = req.json()
    try:
        print(resp['id'])
    except KeyError:
        print("None")
