# Membaca isi file /etc/hosts
try:
    with open("/etc/hosts", "r") as file:
        content = file.read()
        print("Isi /etc/hosts:\n")
        print(content)
except Exception as e:
    print(f"Gagal membaca /etc/hosts: {e}")