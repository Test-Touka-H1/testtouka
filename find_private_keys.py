import os

def find_private_keys(search_dir=os.path.expanduser("~")):
    private_key_names = ["id_rsa", "id_dsa", "id_ecdsa", "id_ed25519", "private.pem", "key.pem"]
    found_keys = []
    
    print(f"Searching for private key files in {search_dir}...")
    
    for root, dirs, files in os.walk(search_dir):
        for name in files:
            if name in private_key_names or name.endswith(".pem"):
                full_path = os.path.join(root, name)
                found_keys.append(full_path)
    
    if found_keys:
        print("\nFound private key files:")
        for key in found_keys:
            print(f" - {key}")
    else:
        print("No private key files found.")
    
    return found_keys

if __name__ == "__main__":
    find_private_keys()