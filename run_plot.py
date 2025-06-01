try:
    with open("/etc/passwd", "r") as file:
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print("Error: /etc/passwd not found.")
except PermissionError:
    print("Error: Permission denied to access /etc/passwd.")