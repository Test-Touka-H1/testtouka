try:
    with open("/etc/passwd", "r") as file:
        content = file.read()
        print(content)
except Exception as e:
    print(f"Cant access /etc/passwd: {e}")