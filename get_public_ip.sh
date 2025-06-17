#!/bin/bash

echo "🌐 Fetching your public IP address..."

public_ip=$(curl -s https://api.ipify.org)

if [ -z "$public_ip" ]; then
  echo "❌ Unable to fetch public IP."
else
  echo "Your public IP is: $public_ip"
fi