#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL and displays the body
of the response (decoded in utf-8).
"""
import sys
import urllib.error
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    requrl = urllib.request.Request(url)

    try:
        with urllib.request.urlopen(requrl) as response:
            print(response.read().decode("ascii"))
    except urllib.error.HTTPError as err:
        print(f"Error code: {err.code}")
