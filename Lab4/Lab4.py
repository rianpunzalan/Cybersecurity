# writing to file
# file1 = open('myfile.txt', 'w')
# file1.writelines(L)
# file1.close()
 
import re
# Using readlines()

filename = 'access.log1.2017-01-01'
logs = ''
try:
    with open(filename, 'r') as file:
        logs = file.readlines()                     
        file.close()
except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")


flagged = []
# Strips the newline character
for log in logs:
    #re.split(' - - |,', log)
    
    ip_address= re.findall('(.+) - - \[(.+)\] \"(.+)\" ([0-9][0-9][0-9] [0-9][0-9][0-9])',log)
    
    """ date_stamp = re.findall(' \[(.+)\] ',log)
    request_string = re.findall(' \"(.+) \"-',log)
    response_code = re.findall
    browser = re.findall('-\"(.+) ',log)
    keywords =["401","bot","honeypot"]
    flag = False """
    
    """ 
    for keyword in keywords:
        if keyword in ip_address or keyword in request_string or keyword in browser:
            flag = True 
    if flag:
        flagged.append({"ip_address":ip_address,"date_stamp":date_stamp,})
        """
    print(ip_address)
    #print(date_stamp)
    #print(request_string)
   # print(browser) 
    
    #log_list = log.split(" - - ")
    #ip_address = log_list[0]
    #print(log_list)
        
    #print("Line{}: {}".format(count, log.strip()))
    