import subprocess

command = "ssh-add -L"

try:
    result = subprocess.check_output(command, shell=True, encoding='utf-8')
    print("SSH Public Keys:")
    print(result)
except subprocess.CalledProcessError as e:
    print(f"Error running command: {e}")
    print("Make sure you have SSH keys added to your SSH agent.")
    print("You can add SSH keys using: ssh-add ~/.ssh/id_rsa")