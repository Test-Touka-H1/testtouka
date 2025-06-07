import os

def list_all_home_directories(base_path="/home"):
    try:
        user_dirs = [d for d in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, d))]
        
        if user_dirs:
            print("User home directories:")
            for user_dir in user_dirs:
                print(f"/home/{user_dir}")
        else:
            print("No user directories found.")
    except FileNotFoundError:
        print(f"The directory {base_path} does not exist.")
    except PermissionError:
        print(f"Permission denied while accessing {base_path}")

if __name__ == "__main__":
    list_all_home_directories()