#!/bin/bash
# Sends a DELETE request to the URL in $1 and displays the response body.
curl -s -X DELETE "$1"
