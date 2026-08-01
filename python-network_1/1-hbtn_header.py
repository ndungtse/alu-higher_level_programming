#!/usr/bin/python3
"""Displays the X-Request-Id response header of a URL using urllib."""
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        print(response.headers.get("X-Request-Id"))
