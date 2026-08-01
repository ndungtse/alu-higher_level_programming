#!/bin/bash
# Sends a GET request with the X-HolbertonSchool-User-Id header and shows the body.
curl -s -H "X-HolbertonSchool-User-Id: 98" "$1"
