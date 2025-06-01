import os

username = os.popen('whoami').read().strip()
print(username)