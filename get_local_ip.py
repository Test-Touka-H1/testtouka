import socket

def get_local_ip():
    try:
        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)
        print(f"Local IP: {ip}")
        return ip
    except socket.error as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    get_local_ip()