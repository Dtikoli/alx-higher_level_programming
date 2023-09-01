#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL and displays the
value of the variable X-Request-Id in the response header
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    key = "X-Request-Id"
    response = requests.get(url)

    print(response.headers.get(key))
