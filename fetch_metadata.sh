#!/bin/bash

URL="http://169.254.169.254/latest/meta-data/"

echo "🌐 Fetching content from $URL ..."
curl -s "$URL"