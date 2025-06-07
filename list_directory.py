import os

path = "."  # Current directory
entries = os.listdir(path)

print("All entries:")
for entry in entries:
    print(entry)