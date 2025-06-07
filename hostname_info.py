import socket  # Get hostname using socket
hostname = socket.gethostname()  # Print the hostname
print(f"Hostname: {hostname}")

# Optional: Get IP address associated with hostname (if needed)
# Try:
# ip_address = socket.gethostbyname(hostname)
# except socket.gaierror:
#    ip_address = "Hostname resolution failed"
#
# print(f"IP Address: {ip_address}")