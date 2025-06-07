import os

def find_aws_credentials(start_dir=os.path.expanduser("~")):
    target_path = os.path.join(".aws", "credentials")
    
    for root, dirs, files in os.walk(start_dir):
        if "credentials" in files and target_path in os.path.join(root, "credentials"):
            full_path = os.path.join(root, "credentials")
            print(f"Found: {full_path}")
            return full_path
    
    print("AWS credentials file not found.")
    return None

if __name__ == "__main__":
    find_aws_credentials()