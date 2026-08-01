#!/bin/bash
# Sends a request to the URL in $1 and displays only the response status code.
curl -s -o /dev/null -w "%{http_code}" "$1"
