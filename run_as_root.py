import subprocess

def run_as_root(command):
    try:
        # Run the command with sudo (elevated privileges)
        result = subprocess.run(['sudo', 'bash', '-c', command], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        # Print output and error
        print("Output:", result.stdout.decode())
        if result.stderr:
            print("Error:", result.stderr.decode())
        
    except subprocess.CalledProcessError as e:
        print(f"Error running command as root: {e}")

if __name__ == "__main__":
    # Example command (e.g., listing root's home directory)
    run_as_root("ls /root")