#!/bin/bash

URL="$1"

if [ -z "$URL" ]; then
  echo "Usage: $0 <website_url>"
  exit 1
fi

echo "🔍 Checking web server for $URL ..."

# Fetch headers and get the Server line
server_info=$(curl -sI "$URL" | grep -i '^Server:')

if [ -z "$server_info" ]; then
  echo "⚠️ Server header not found."
else
  echo "$server_info"
fi