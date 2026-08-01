#!/bin/bash
# Sends a POST request with the JSON file in $2 as body and displays the response.
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
