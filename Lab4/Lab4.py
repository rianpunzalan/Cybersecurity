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
        logs = file.read()                     
        file.close()
except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
    
log_array= re.findall(r'(.+) - - (\[.+\]) (\".+\") (\d+) (\d+) (\".+\") (\".+\") ',logs)
keywords =["admin","self.logs","bot","honeypot","401","403","404"]
flagged_logs = {"admin":[],"self.logs":[],"bot":[],"honeypot":[],"401":[],"403":[],"404":[]}

line_number=1
for log in log_array:
    flag = False
    ip_address = log[0]
    date_stamp = log[1]
    request_string = log[2]
    response_code = log[3]
    object_size = log[4]
    search_engine=log[5] 
    browser =log[6]
    
    
    for keyword in keywords:
        if keyword.casefold() in request_string or keyword.casefold() in browser or keyword == response_code:
            flagged_logs[keyword].append({"user_agent":browser,"request_string":request_string,"ip_address":ip_address,"date_stamp":date_stamp,"line_number":line_number})
            break
    line_number+=1

print("\nSuspicious Activity Statistics")
print("Choices: ")
count = 1
for flag_type in flagged_logs:
    print(f"{count} - {flag_type}: {len(flagged_logs[flag_type])} hits.")
    count+=1

while True:
    choice = input("input choice to see the access details: ")
    if 1 <= int(choice) <= 7:
        for log in flagged_logs[keywords[int(choice)-1]]:
            print(f"\nUser-agent: {log['user_agent']}")
            print(f"request: {log['request_string']}")
            print(f"IP: {log['ip_address']}")
            print(f"datetime: {log['date_stamp']}")
            print(f"line in log file: {log['line_number']}")
        break
    else:
        print("invalid choice")

    