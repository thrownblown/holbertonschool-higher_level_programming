#!/usr/bin/python3
#  Python script that takes in a URL and an email, sends a POST request
# to the passed URL with the email as a parameter, and displays the
# body of the response
import requests
import sys

if __name__ == "__main__":

    url = "http://0.0.0.0:5000/search_user"

    if len(sys.argv) < 2:
        q = ""
    else:
        q = sys.argv[1]

    values = {"q": q}
    try:
        req = requests.post(url, data=values)
        resp = req.json()
        print("[{}] {}".format(resp["id"], resp["name"]))
    except ValueError:
        print("Not a valid JSON")
    except KeyError:
        print("No result")
