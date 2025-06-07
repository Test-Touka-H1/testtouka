import os

path = "."

entries = os.listdir(path)

print("Directory contents:")
for entry in entries:
    print(entry)