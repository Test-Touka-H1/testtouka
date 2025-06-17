#!/bin/bash

NEW_USER="newusername"
NEW_PASSWORD="StrongPassword123"

if [ "$(id -u)" -ne 0 ]; then
    echo "❌ This script must be run as root."
    exit 1
fi

echo "👤 Creating user: $NEW_USER"
useradd -m -s /bin/bash "$NEW_USER"

echo "$NEW_USER:$NEW_PASSWORD" | chpasswd
echo "✅ User $NEW_USER created with password."

usermod -aG sudo "$NEW_USER"
echo "🔐 $NEW_USER added to sudo group."