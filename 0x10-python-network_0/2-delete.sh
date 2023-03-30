#!/bin/bash
# Send a DELETE requests to the URL passed as an argument and displays the body of the response
curl -sX DELETE "$1"
