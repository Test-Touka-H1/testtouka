import os

def print_all_directories(start_path="."):
    for root, dirs, files in os.walk(start_path):
        for dir_name in dirs:
            full_path = os.path.join(root, dir_name)
            print(full_path)

if __name__ == "__main__":
    print_all_directories("/")