#!/bin/bash
#takes in a URL, sends a request to that URL, and displays the size of the body of the response
curl -o /dev/null -sw "%{http_code}" "$1"
