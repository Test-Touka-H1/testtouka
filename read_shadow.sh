#!/bin/bash
echo "Attempting to read /etc/shadow..."
if [ "$(id -u)" -ne 0 ]; then
  echo "You are not root. Trying with sudo..."
  sudo cat /etc/shadow
else
  cat /etc/shadow
fi