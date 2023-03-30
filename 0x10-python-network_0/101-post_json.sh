#!/bin/bash
# Sends a JOSN POST request to a URL passed an argument and displays the body of the response
curl -s -H "Content-Type: application/json" -d "%(cat "$2")" "$1"
