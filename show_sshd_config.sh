#!/bin/bash

CONFIG_FILE="/etc/ssh/sshd_config"

echo "📄 Showing content of $CONFIG_FILE:"
echo "-----------------------------------"

if [ "$(id -u)" -ne 0 ]; then
  sudo cat "$CONFIG_FILE"
else
  cat "$CONFIG_FILE"
fi