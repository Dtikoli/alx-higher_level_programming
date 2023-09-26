#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL and displays the value of
the X-Request-Id variable found in the header of the response
"""
import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    key = "X-Request-Id"
    requrl = urllib.request.Request(url)
    
    with urllib.request.urlopen(requrl) as response:
        print(response.headers[key])
