## lets get some important information from the logs we need.

# Some critical thing such as 404 :(

#First step is to read the file we can use open() function

import os
# Get the current directory path
current_dir = os.path.dirname(os.path.abspath(__file__))
log_file_path = os.path.join(current_dir, "access.log")

count_404=0
with open(log_file_path,"r") as file:

    for line  in file:
        fields = line.split()
        if len(fields) >= 7:
            ip_address = fields[0]
            request_path = fields[6]


            print("IP Address: ", {ip_address})
            print("Request Path:", request_path)

            
            if "404" in fields:
                count_404+=1 # I'm just counting the number of 404 occurrence we can use it for alerting or any other troubleshooting 



         
                

print(count_404)
            