import pandas as pd
import re
import os
import shutil
from openpyxl import Workbook
import csv
 

# Lists for WhatsApp data to be stored, date, time, sender, and message
msgDate = []
msgTime = []
msgSender = []
msg = []
 
# Get current working directory
cwd = os.getcwd()

# loop over all files in CWD
for filename in os.listdir(cwd):

    
    # search for all text files that aren't the requirements file
    if filename != ("requirements.txt") and filename.endswith(".txt"):

        # Opens file and loops over each row, looking for dare, time, sender and message
        with open(filename, 'r', encoding='utf-8') as f:
        
            test = f.readlines()
        
            start = 1
            numItems = len(test)
        
            want = range(start, numItems)
        
            for row in want:
        
            # set Date Pattern
                datePattern = '(\d+/\d+/\d+)'
        
                try:
                    date = re.search(datePattern, test[row]).group(0)
                except AttributeError:
                    date = "No Date"
        
                msgDate.append(date)
        
                # Set time pattern
                timePattern = '\d+:\d+'
        
                try:
                    time = re.search(timePattern, test[row]).group(0)
                except AttributeError:
                    time = "No Time"
        
                msgTime.append(time)
        
                # Set person pattern (every value between - and :)
                personPattern = '(?s)(?<=-\s).*?(?=:)'
        
                try:
                    person = re.search(personPattern, test[row]).group(0).replace("- ", "")
                except AttributeError:
                    person = "No Person"
        
                msgSender.append(person)
        
                # set message pattern
                messagePattern = '(:\s).*'    
        
                try:
                    message = re.search(messagePattern, test[row]).group(0).replace(": ", "")
                except AttributeError:
                    message = "No message"
        
                msg.append(message)

                # pandas dataframe created from the lists
        
        df = pd.DataFrame(list(zip(msgDate, msgTime, msgSender, msg)),
                        columns=['Date', 'Time', 'Sender', 'Message'])
       

        # get filename minus extension                
        split_filename = os.path.splitext(filename)[0]  

        # use the split filename with new extensions
        csv_filename = split_filename + '.csv'
        excel_filename = split_filename + '.xlsx'

        # datafram saved to CSV
        df.to_csv(csv_filename, index=False)

        # CSV coverted to Excel format (opens CSV and converst to xlsx format)
        wb = Workbook()
        ws = wb.active
        with open(csv_filename, 'r', encoding='utf-8') as f:
            for row in csv.reader(f):
                ws.append(row)
        wb.save(excel_filename)

        os.makedirs(split_filename)
        shutil.move(filename, split_filename)
        shutil.move(csv_filename, split_filename)
        shutil.move(excel_filename, split_filename)


    else:
        continue

# TODO: create folder for each txt file, with a input/output folders
