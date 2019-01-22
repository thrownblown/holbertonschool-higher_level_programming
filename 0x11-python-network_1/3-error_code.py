#!/usr/bin/python3
# Python script that takes in a URL, sends a request to the URL and displays
# the value of the X-Request-Id variable found in the header of the response.
import urllib.request
import sys

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            html = response.read()
            print(html)
    except urllib.error.HTTPError as err:
        print("Error code: {}".format(err.code))
