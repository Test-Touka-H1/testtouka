import os

def print_all_directories(start_path):
    for root, dirs, files in os.walk(start_path):
        for d in dirs:
            print(os.path.join(root, d))

if __name__ == "__main__":
    print_all_directories("/")