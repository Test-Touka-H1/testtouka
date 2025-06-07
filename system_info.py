import psutil

def get_system_info():
    print("System Information:")
    
    # Get CPU info
    print(f"CPU Usage: {psutil.cpu_percent()}%")
    
    # Get memory info
    memory = psutil.virtual_memory()
    print(f"Memory Usage: {memory.percent}%")
    
    # Get disk info
    disk = psutil.disk_usage('/')
    print(f"Disk Usage: {disk.percent}%")

if __name__ == "__main__":
    get_system_info()