import os

path = "."  # You can change this to any path

directories = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]

print("Directories:")
for d in directories:
    print(f"  {d}")