#!/bin/bash
# Sends a request to the URL in $1 and displays the response body size in bytes.
curl -s "$1" | wc -c
