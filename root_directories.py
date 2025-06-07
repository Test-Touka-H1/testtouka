import os

root_path = "/"

dirs = [d for d in os.listdir(root_path) if os.path.isdir(os.path.join(root_path, d))]

print("Top-level directories in /:")
for d in dirs:
    print(d)