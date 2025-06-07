import os

def read_etc_shadow():
    try:
        with open("/etc/shadow", "r") as f:
            for line in f:
                print(line.strip())
    except PermissionError:
        print("Permission denied: You need to run this script as root.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if os.geteuid() == 0:
        print("Running as root!")
    else:
        print("Not running as root.")
    read_etc_shadow()