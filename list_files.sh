#!/bin/bash
DIR="/opt/atlassian/pipelines/agent/"
echo "Listing all files under $DIR:"
if [ -d "$DIR" ]; then
  find "$DIR" -type f
else
  echo "Directory $DIR does not exist."
fi