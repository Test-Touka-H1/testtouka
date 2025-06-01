import os
import platform

# Check if os.uname() is available
if hasattr(os, 'uname'):
    print("os.uname():", os.uname())
else:
    print("os.uname() is not supported on this system.")

print("platform.uname():", platform.uname())