#!/bin/bash
#takes in a URL, sends a request to that URL, and displays the size of the body of the response
curl -sIX OPTIONS  "$1" | grep "Allow:" | cut -d ' ' -f2- 
