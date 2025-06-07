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
    read_etc_shadow()