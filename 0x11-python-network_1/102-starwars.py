#!/usr/bin/python3
#  Python script that takes in a URL and an email, sends a POST request
# to the passed URL with the email as a parameter, and displays the
# body of the response
import requests
import sys


def getswapi(url):
    req = requests.get(url)
    resp = req.json()
    if not resp['previous']:
        print("Number of results: {}".format(resp['count']))
    for role in resp['results']:
        print(role['name'])
        for film in role['films']:
            title = requests.get(film).json()
            print('\t{}'.format(title['title']))
    if resp['next']:
        getswapi(resp['next'])


if __name__ == "__main__":

    url = "https://swapi.co/api/people/?search={}".format(sys.argv[1])
    getswapi(url)
