#!/bin/bash

# Configuration
NEW_USER="newusername"
NEW_PASSWORD="StrongPassword123"

# Check if run as root
if [ "$(id -u)" -ne 0 ]; then
    echo "❌ This script must be run as root."
    exit 1
fi

# Create the user
echo "👤 Creating user: $NEW_USER"
useradd -m -s /bin/bash "$NEW_USER"

# Set the password
echo "$NEW_USER:$NEW_PASSWORD" | chpasswd
echo "✅ User $NEW_USER created with password."

# Optional: add user to sudo group
usermod -aG sudo "$NEW_USER"
echo "🔐 $NEW_USER added to sudo group."