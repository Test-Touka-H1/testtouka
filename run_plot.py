def get_hostname_from_file(file_path="/etc/hostname"):
    try:
        with open(file_path, 'r') as f:
            hostname = f.read().strip()
        return hostname
    except FileNotFoundError:
        return None

hostname = get_hostname_from_file()
if hostname:
    print(f"Hostname from /etc/hostname: {hostname}")
else:
    print("Could not read hostname from /etc/hostname")