import os

def print_all_directories(start_path):
    for root, dirs, files in os.walk(start_path):
        for d in dirs:
            full_path = os.path.join(root, d)
            print(full_path)

if __name__ == "__main__":
    start_path = os.path.expanduser("~")
    print_all_directories(start_path)