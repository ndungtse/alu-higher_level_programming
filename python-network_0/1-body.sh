#!/bin/bash
# Sends a GET request to the URL in $1, following redirects to the 200 body.
curl -sL "$1"
