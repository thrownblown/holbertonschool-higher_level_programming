#!/usr/bin/python3
# Python script that takes in a URL, sends a request to the URL and displays
# the value of the X-Request-Id variable found in the header of the response.
import urllib.request as req
from sys import argv


with req.urlopen(argv[1]) as response:
    html = response.getheader('X-Request-Id')
    print(html)
