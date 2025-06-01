try:
    with open("/etc/hosts", "r") as file:
        content = file.read()
        print(content)
except Exception as e:
    print(f"Cant access /etc/hosts: {e}")