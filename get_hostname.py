import os

def get_hostname():
    # Get the hostname of the machine
    hostname = os.uname()[1]
    print(f"Hostname: {hostname}")

if __name__ == "__main__":
    get_hostname()