#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL
and displays the body of the response.
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    request = requests.get(url)
    if request.status_code >= 400:
        print(f"Error code: {request.status-code}")
    else:
        print(request.text)
