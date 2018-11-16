import pandas as pd
import re
from openpyxl import Workbook
import csv
 

# Lists for WhatsApp data to be stored, date, time, sender, and message
msgDate = []
msgTime = []
msgSender = []
msg = []
 
# TODO: make the script open any text file and/or loop over each text fil

# Opens file and loops over each row, looking for dare, time, sender and message
with open('whatsapp_chat.txt', 'r', encoding='utf-8') as f:
 
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
 
# datafram saved to CSV
df.to_csv('whatsapp_chat.csv', index=False)

# CSV coverted to Excel format
wb = Workbook()
ws = wb.active
with open('whatsapp_chat.csv', 'r', encoding='utf-8') as f:
    for row in csv.reader(f):
        ws.append(row)
wb.save('whatsapp_chat.xlsx')

# TODO: create folder for each txt file, with a input/output folders
