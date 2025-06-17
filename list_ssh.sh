#!/bin/bash

TARGET_DIR="/etc/ssh"
CONFIG_FILE="$TARGET_DIR/sshd_config"

echo "📂 SSH Configuration Status:"
echo "-------------------------"

# List SSH directory contents
echo "📁 Files in $TARGET_DIR:"
if [ "$(id -u)" -ne 0 ]; then
    sudo ls -l "$TARGET_DIR"
else
    ls -l "$TARGET_DIR"
fi

# Show sshd_config content
echo -e "\n🔧 Content of sshd_config:"
if [ "$(id -u)" -ne 0 ]; then
    sudo cat "$CONFIG_FILE"
else
    cat "$CONFIG_FILE"
fi