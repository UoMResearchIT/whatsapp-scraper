import pandas as pd
import re
import os
import shutil
import csv
import datetime

from pandas.io.excel import ExcelWriter
import pandas

start = True

msg_date_time = []
msg_sender = []
msg = []
msg_number = []

# Get current working directory
cwd = os.getcwd()

# loop over all files in CWD
for filename in os.listdir(cwd):
    
    # search for all text files that aren't the requirements file
    if filename != ("requirements.txt") and filename.endswith(".txt"):

        with open(filename, "r", encoding='utf-8') as f:   
            
            test = f.readlines()
            start = 1
            num_items = len(test)    
            want = range(start, num_items)

            msg_date_time = []
            msg_sender = []
            msg = []
            msg_number_list = []
            
            for row in want:

                # If date, sender and message are present, add these to their respective lists
                
                try:
                    date = re.search(r'(\d+/\d+/\d+), (\d+:\d+)', test[row]).group(0)
                except AttributeError:
                    new_message = msg[-1] + " " + test[row]
                    del msg[-1]
                    msg.append(new_message)
                    continue

                try:
                    sender = re.search(r'(?s)(?<=-\s).*?(?=:)',test[row]).group(0).replace("- ", "")
                except:
                    sender = " "        

                try:
                    message = re.search(r"(:\s).*[\d+/\d+/\d+]*", test[row]).group(0).replace(": ", "")
                except:
                    message = "No Message"

                msg_date_time.append(date)

                msg_sender.append(sender)

                msg.append(message)

                # if date in test[row]:
                #         msg_date_time.append(date)
                #         msg_sender.append(sender)
                #         msg.append(message)
                # else:
                #     msg[-1].append(test[row])

                # If there is no message (as is the case of admin changes to chat (new icon etc), delete that row)
                # elif message is False:
                #     garbage_list.append(test[row])

loop_num = len(msg)
msg_number = 1

for number in range(loop_num) :
    
    msg_number_list.append(str(msg_number))
    msg_number += 1


print(msg_number_list)

df = pd.DataFrame(list(zip(msg_number_list, msg_date_time, msg_sender, msg)),
                        columns=['Message Number', 'Date Time','Sender', 'Message'])
       

# get filename minus extension                
# split_filename = os.path.splitext(filename)[0]  

# use the split filename with new extensions
# csv_filename = split_filename + '.csv'
# excel_filename = split_filename + '.xlsx'

# dataframe saved to CSV
df.to_csv('output.csv', index=False)

# os.makedirs(filename)
# shutil.move('output.csv', filename)
# shutil.move(csv_filename, split_filename)
# shutil.move(excel_filename, split_filename)
