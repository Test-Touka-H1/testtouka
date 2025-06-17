#!/bin/bash

FILE="/etc/shadow"
echo "🔒 Showing content of $FILE with sudo:"

if [ "$(id -u)" -ne 0 ]; then
  cat "$FILE"
else
  cat "$FILE"
fi