import pandas as pd
import re
import sys
import os
import shutil
import csv
import datetime


# Get current working directory
cwd = os.getcwd()
checklist = os.listdir(cwd)

# Checks to see how many text files there are. If there's only one 
# the script is stopped
text_list = []
for filename in checklist:
    if filename.endswith(".txt") == 1:
        text_list.append(filename)
if len(text_list) == 1:
    print('No are no WhatsApp .txt files')
    sys.exit()

# loop over all files in CWD
for filename in checklist:
    
    # search for all text files that aren't the requirements file
    if filename != ("requirements.txt") and filename.endswith(".txt"):

        # open the text file
        with open(filename, "r", encoding='utf-8') as f:   

            # Checks the first line to see if its an old WhatsAPP message or new one.
            first_line = f.readline()

            test = f.readlines()
            start = 1
            num_items = len(test)    
            want = range(start, num_items)
            
            # List where the datetime, sender, message and message number go
            msg_date_time = []
            msg_sender = []
            msg = []
            msg_number_list = []

            # checks first charcater of firstline, if its a opening of square brackets, 
            # it will run new whatsApp loop, otherwise it will run the old one.
            if first_line[0] == '[':
                
                for row in want:
                    try:
                        date = re.search(r'(.\d+/\d+/\d+), (\d+:\d+:\d\d.)', test[row]).group(0)
                        
                        #gets rid of brackets for nicer CSV formatting
                        date = re.sub(r'\[', '', date)
                        date = re.sub(r'\]', '', date)   
                    except AttributeError:
                        new_message = msg[-1] + " " + test[row]
                        del msg[-1]
                        msg.append(new_message)
                        continue     

                    # Looks for message and creates a "No Message" this helps filter out the admin messages, eg. this person changed group icon etc
                    try:
                        message = re.search(r"(:\s).*[\d+/\d+/\d+]*", test[row]).group(0).replace(": ", "")
                    except:
                        message = "No Message"

                    try:
                        # Finds the sender by deleting the message and date/time from the row.
                        row = test[row]
                        sender = re.sub(r"(.\d+/\d+/\d+), (\d+:\d+:\d\d.)", "", row)
                        sender = re.sub(r":.*", "", sender)
                        
                    except:
                        sender = " "


                    msg_date_time.append(str(date))

                    msg_sender.append(sender)

                    msg.append(message)

            else:

                for row in want:

                    # try to find the date, if can't then a message has continued from previous line.
                    # this is then appended to previous message by finding it in the msg list and concantonbating it    
                    try:
                        date = re.search(r'(\d+/\d+/\d+), (\d+:\d+)', test[row]).group(0)
                    except AttributeError:
                        new_message = msg[-1] + " " + test[row]
                        del msg[-1]
                        msg.append(new_message)
                        continue

                    # Tries sender and creates a blank
                    try:
                        sender = re.search(r'(?s)(?<=-\s).*?(?=:)',test[row]).group(0).replace("- ", "")
                    except:
                        sender = " "        

                    # Looks for message and creates a "No Message" this helps filter out the admin messages, eg. this person changed group icon etc
                    try:
                        message = re.search(r"(:\s).*[\d+/\d+/\d+]*", test[row]).group(0).replace(": ", "")
                    except:
                        message = "No Message"

                    msg_date_time.append(date)

                    msg_sender.append(sender)
                    
                    msg.append(message)

        # Creates a pandas dataframe
        df = pd.DataFrame(list(zip(msg_date_time, msg_sender, msg)),
                            columns=['Date Time','Sender', 'Message'])

        # Drops all rows where the message is "No Message"
        df = df[~df.Message.str.contains("No Message")]

        # Create a message number column
        msg_number_list
        loop_num = len(df.index)
        msg_number = 1
        for number in range(loop_num) :
            msg_number_list.append(str(msg_number))
            msg_number += 1

        # Creates new df with message number column
        df = df.assign(message_number = msg_number_list)

        # Reanmes column
        df = df.rename({'message_number': 'Message Number'}, axis=1)

        # Reorders columns
        df = df[['Message Number', 'Date Time', 'Sender', 'Message']]

        # get filename minus extension                
        split_filename = os.path.splitext(filename)[0]  

        # use the split filename with new extensions
        csv_filename = split_filename + '.csv'

        # dataframe saved to CSV
        df.to_csv(csv_filename, index=False)

        # makes a new directory and puts the source and outputs file in it
        os.makedirs(split_filename)
        shutil.move(filename, split_filename)
        shutil.move(csv_filename, split_filename)

