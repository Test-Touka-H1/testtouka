#!/bin/bash
TARGET_DIR="/opt/atlassian/pipelines/agent/build"
echo "📂 Listing files in: $TARGET_DIR"
echo "--------------------------------"
if [ "$(id -u)" -ne 0 ]; then
    echo "🔐 Not running as root. Using sudo..."
    sudo find "$TARGET_DIR" -type f 2>/dev/null
else
    find "$TARGET_DIR" -type f 2>/dev/null
fi