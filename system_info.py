import platform

info = platform.uname()
print("System:", info.system)
print("Node Name:", info.node)
print("Release:", info.release)
print("Version:", info.version)
print("Machine:", info.machine)
print("Processor:", info.processor)