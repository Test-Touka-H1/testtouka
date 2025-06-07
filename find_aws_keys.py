import os
import glob

def find_aws_key(file_extension=".pem", start_dir="/"):
    """
    Recursively searches for files with the given extension (default .pem) in the entire system starting from `start_dir`.
    """
    print(f"Searching for AWS private keys with extension '{file_extension}' in {start_dir}...")
    
    # Use glob to search recursively
    key_files = glob.glob(os.path.join(start_dir, f"**/*{file_extension}"), recursive=True)
    
    if key_files:
        print("Found the following AWS private keys:")
        for key in key_files:
            print(key)
    else:
        print("No AWS private keys found.")

if __name__ == "__main__":
    # Start the search from the root ("/") to scan the whole system
    find_aws_key(start_dir="/")  # Can also replace with a specific directory, e.g., "/home"