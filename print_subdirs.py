import os

def print_all_subdirectories(base_path=None):
    # Use the home directory if no base path is provided
    if base_path is None:
        base_path = os.path.expanduser("~")
    
    print(f"Searching subdirectories in: {base_path}")
    
    for root, dirs, files in os.walk(base_path):
        # For each directory in the walk, print it
        for dir_name in dirs:
            print(os.path.join(root, dir_name))

if __name__ == "__main__":
    print_all_subdirectories()  # Start the search from the user's home directory