# No need tom understand this but if still want to than it creates a random apache dummy logs  using the sample data
# provided  below  like ips,method,paths,statuses. In this random funnctio is been used to pick up the values randomly.

# When you run thbe script it will create a access.log file in the  current directory where your script resides.


import random
import time
import os

# Sample data for generating dummy Apache log entries
ips = ["192.168.1.1", "10.0.0.1", "172.16.0.1"]
methods = ["GET", "POST", "PUT", "DELETE"]
paths = ["/index.html", "/about", "/contact", "/products"]
statuses = [200, 404, 500, 501, 300]

# Function to generate a random Apache log entry
def generate_log_entry():
    ip = random.choice(ips)
    method = random.choice(methods)
    path = random.choice(paths)
    status = random.choice(statuses)
    timestamp = time.strftime("%d/%b/%Y:%H:%M:%S %z", time.localtime())
    return f"{ip} - - [{timestamp}] \"{method} {path}\" {status}\n"

# Number of log entries to generate
num_entries = 1000

# Generate dummy Apache access log data
log_data = "".join([generate_log_entry() for _ in range(num_entries)])

# Get the current directory path
current_dir = os.path.dirname(os.path.abspath(__file__))

# Save log data to a file in the current directory
log_file_path = os.path.join(current_dir, "access.log")
with open(log_file_path, "w") as file:
    file.write(log_data)


print(f"{num_entries} log entries generated and saved to access.log.")
