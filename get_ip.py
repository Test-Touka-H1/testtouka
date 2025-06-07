import socket

def get_ip_address():
    # Get the local machine's IP address
    ip_address = socket.gethostbyname(socket.gethostname())
    print(f"Local IP Address: {ip_address}")

if __name__ == "__main__":
    get_ip_address()