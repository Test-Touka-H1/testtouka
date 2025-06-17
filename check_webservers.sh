#!/bin/bash

echo "🔍 Checking which web server is running on this Linux machine..."

# Check if Apache is running
if pgrep -x "apache2" >/dev/null 2>&1 || pgrep -x "httpd" >/dev/null 2>&1; then
  echo "✅ Apache web server is running."
fi

# Check if Nginx is running
if pgrep -x "nginx" >/dev/null 2>&1; then
  echo "✅ Nginx web server is running."
fi

# Check if Lighttpd is running
if pgrep -x "lighttpd" >/dev/null 2>&1; then
  echo "✅ Lighttpd web server is running."
fi