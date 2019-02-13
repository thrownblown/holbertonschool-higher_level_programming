#!/usr/bin/python3
# Python script that takes in a URL, sends a request to the URL and displays
# the value of the X-Request-Id variable found in the header of the response.
import requests
import sys

if __name__ == "__main__":
    try:
        resp = requests.get(sys.argv[1])
        resp.raise_for_status()
        print(resp.text)
    except requests.exceptions.HTTPError:
        print("Error code: {}".format(resp.status_code))
