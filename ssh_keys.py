import subprocess  # Perintah untuk menampilkan kunci publik SSH
command = "ssh-add -L"  # Menggunakan ssh-add dengan opsi -L untuk menampilkan kunci publik

try:
    # Jalankan perintah dan ambil outputnya
    result = subprocess.check_output(command, shell=True, encoding='utf-8')
    
    # Cetak output (kunci publik SSH)
    print("Kunci publik SSH:")
    print(result)
except subprocess.CalledProcessError as e:
    print(f"Error menjalankan perintah: {e}")
    print("Pastikan Anda memiliki kunci SSH yang ditambahkan ke SSH agent.")
    print("Anda dapat menambahkan kunci SSH dengan perintah: `ssh-add ~/.ssh/id_rsa`")