#!/bin/bash
# Send a GET request to a URL passed as an argument and displays the body of the response
curl -s -H "X-School-User-Id: 98" "$1"
