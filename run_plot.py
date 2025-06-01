# importing required modules
import os
import pwd

# Using getpwuid() and getuid we are
# printing current username
print(pwd.getpwuid(os.getuid())[0])