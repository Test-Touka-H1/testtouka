#!/bin/bash

echo "👥 Users on this system:"
echo "Username | UID | Home Directory"
echo "------------------------------"

while IFS=: read -r username _ uid _ _ home shell; do
    echo "$username | $uid | $home"
done < /etc/passwd