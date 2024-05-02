import platform

#for more visit https://docs.python.org/3/library/platform.html

# Cross-Platform Compatibility
if platform.system() == 'Windows':
    print("Running on Windows")
elif platform.system() == 'Linux':
    print("Running on Linux")
else:
    print("Running on an unsupported platform")

# System Information
print("OS Name:", platform.system())
print("OS Version:", platform.version())
print("Python Version:", platform.python_version())
print("Machine Architecture:", platform.machine())

# Conditional Execution
if platform.system() == 'Windows':
    # Execute Windows-specific code
    pass
elif platform.system() == 'Linux':
    # Execute Linux-specific code
    pass
else:
    # Execute code for unsupported platforms
    pass

# Python version
print("Python version:",platform.python_version())
