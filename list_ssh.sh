#!/bin/bash

TARGET_DIR="/etc/ssh"
CONFIG_FILE="$TARGET_DIR/sshd_config"

echo "📂 SSH Configuration Management:"
echo "-----------------------------"

# Function to show menu
show_menu() {
    echo -e "\n📋 Available Actions:"
    echo "1) List SSH directory contents"
    echo "2) View sshd_config"
    echo "3) Edit sshd_config"
    echo "q) Quit"
    echo -n "Select an option: "
    read -r choice
}

# List SSH directory contents
list_directory() {
    echo -e "\n📁 Files in $TARGET_DIR:"
    if [ "$(id -u)" -ne 0 ]; then
        sudo ls -l "$TARGET_DIR"
    else
        ls -l "$TARGET_DIR"
    fi
}

# Show sshd_config content
view_config() {
    echo -e "\n🔧 Content of sshd_config:"
    if [ "$(id -u)" -ne 0 ]; then
        sudo cat "$CONFIG_FILE"
    else
        cat "$CONFIG_FILE"
    fi
}

# Edit sshd_config
edit_config() {
    echo -e "\n✏️  Opening sshd_config in nano editor..."
    if [ "$(id -u)" -ne 0 ]; then
        sudo nano "$CONFIG_FILE"
    else
        nano "$CONFIG_FILE"
    fi
}

# Main loop
while true; do
    show_menu
    case $choice in
        1) list_directory ;;
        2) view_config ;;
        3) edit_config ;;
        q|Q) exit 0 ;;
        *) echo -e "\n⚠️  Invalid option. Please try again." ;;
    esac
    echo -e "\nPress Enter to continue..."
    read -r
    clear
done