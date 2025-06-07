import os

def list_files_in_directory(directory_path):
    try:
        # List all files and directories inside the given directory
        files = os.listdir(directory_path)
        
        if files:
            print(f"Contents of {directory_path}:")
            for file in files:
                print(file)
        else:
            print(f"The directory {directory_path} is empty.")
    except FileNotFoundError:
        print(f"Error: The directory {directory_path} does not exist.")
    except PermissionError:
        print(f"Error: Permission denied while accessing {directory_path}")

if __name__ == "__main__":
    directory = "/opt/service/.ssh"  # Directory to open
    list_files_in_directory(directory)