import os

# File and Directory Operations
print("Current working directory:", os.getcwd())
print("List of files in current directory:", os.listdir())

# Path Operations
path_to_check = "example_directory"
if not os.path.exists(path_to_check):
    os.mkdir(path_to_check)
    print(f"Created directory: {path_to_check}")
else:
    print(f"Directory '{path_to_check}' already exists.")

# Delete example directory is already exists
if os.path.exists(path_to_check):
    os.rmdir(path_to_check)
    print(f"Deleted directory: {path_to_check}")


print("Print cpu count: ", os.cpu_count())

# Process Management
print("Process ID:", os.getpid())

# Environment Variables
print("Value of HOME environment variable:", os.getenv("HOME"))

# Miscellaneous
print("Name of the user logged in:", os.getlogin())

print("Name of os: ",os.name)


# Theres a reversed function which is mainly an iterator here I'm using join function to join the iterated values thus giving us a reversed string
name = "sandeep"
reversed_name = ''.join(reversed(name))
print(reversed_name)
# Reversed could be used as per use cases example 
# Get a list of filenames in the directory
file_list = os.listdir('.')

# Process filenames in reverse alphabetical order
for filename in reversed(sorted(file_list)):
    # Do something with the filename
    print(filename)




# There are more funtions that are provided by os module just type "os." or visit to https://docs.python.org/3/library/os.html"

