import requests

def get_public_ip():
    try:
        ip = requests.get('https://api.ipify.org').text
        return ip
    except requests.RequestException:
        return "Unable to get public IP"

print(f"Public IP Address: {get_public_ip()}")