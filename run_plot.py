try:
    with open("/etc/hostname", "r") as file:
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print("Error: /etc/hostname not found.")
except PermissionError:
    print("Error: Permission denied to access /etc/hostname.")