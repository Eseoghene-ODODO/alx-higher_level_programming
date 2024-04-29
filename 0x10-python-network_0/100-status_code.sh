#!/bin/bash
# Description: Sends a request to a URL and displays only the HTTP status code
curl -so /dev/null -w '%{http_code}' "$1"
