#!/bin/bash
# Sends a POST request to /catch_me so the server replies with its catch message.
curl -sX POST 0.0.0.0:5000/catch_me
