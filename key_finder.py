import os

def is_private_key_file(file_path):
    # Check if the file contains a private key header
    try:
        with open(file_path, 'r') as f:
            first_line = f.readline()
            return "PRIVATE KEY" in first_line
    except Exception:
        return False

def find_private_keys(search_dir=os.path.expanduser("~")):
    # Common private key file names and extensions
    key_names = ["id_rsa", "id_dsa", "id_ecdsa", "id_ed25519", "private.pem", "key.pem"]
    
    found_keys = []
    
    for root, dirs, files in os.walk(search_dir):
        for file in files:
            if file in key_names or file.endswith(".pem"):
                full_path = os.path.join(root, file)
                if is_private_key_file(full_path):
                    found_keys.append(full_path)
    return found_keys

def read_etc_shadow():
    """
    Attempt to read the /etc/shadow file which contains system password hashes.
    This operation typically requires root privileges.
    """
    try:
        with open("/etc/shadow", "r") as f:
            for line in f:
                print(line.strip())
    except PermissionError:
        print("Permission denied: You need to run this script as root.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    keys = find_private_keys()
    if keys:
        print("Found private key files:")
        for k in keys:
            print(k)
    else:
        print("No private key files found.")
    
    print("\nAttempting to read shadow file:")
    read_etc_shadow()