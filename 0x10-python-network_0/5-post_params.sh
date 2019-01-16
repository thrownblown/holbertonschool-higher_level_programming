#!/bin/bash
#takes in a URL, sends a request to that URL, and displays the size of the body of the response
curl -s "$1" -X POST -d "subject=I will always be here for PLD&email=hr@holbertonschool.com"
