import os

info = os.uname()
print("System Name:", info.sysname)
print("Node Name:", info.nodename)
print("Release:", info.release)
print("Version:", info.version)
print("Machine:", info.machine)