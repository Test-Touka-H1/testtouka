import subprocess

def get_system_info():
    try:
        result = subprocess.run(['uname', '-a'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("System Information:")
        print(result.stdout.decode())
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")

if __name__ == "__main__":
    get_system_info()