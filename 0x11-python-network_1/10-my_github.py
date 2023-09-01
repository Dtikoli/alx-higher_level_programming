#!/usr/bin/python3
"""
Takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    url = "https://api.github.com/user"
    authen = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    response = requests.get(url, auth=authen)

    print(request.json().get("id"))
