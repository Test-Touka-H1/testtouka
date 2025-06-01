try:
    with open("/etc/issues", "r") as file:
        content = file.read()
        print(content)
except Exception as e:
    print(f"Cant access /etc/issues: {e}")