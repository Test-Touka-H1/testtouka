#!/bin/bash

echo "👥 All users on this system:"
echo "----------------------------"

while IFS=: read -r username _ uid _ _ _ _; do
    if [ "$uid" -eq 0 ]; then
        echo "🟥 $username (root user)"
    else
        echo "▫️  $username"
    fi
done < /etc/passwd