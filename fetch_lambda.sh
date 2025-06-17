#!/bin/bash

URL="http://localhost:9001/2018-06-01/runtime/invocation/next/"

echo "🌐 Fetching content from $URL ..."
curl -s "$URL"