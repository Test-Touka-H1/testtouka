import os

root_dir = "/"

for dirpath, dirnames, filenames in os.walk(root_dir):
    print(f"Folder: {dirpath}")
    for dirname in dirnames:
        print(f"  Subfolder: {dirname}")
    for filename in filenames:
        print(f"  File: {filename}")