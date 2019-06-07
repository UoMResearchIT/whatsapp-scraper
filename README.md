# WhatsApp Scraper

A script that takes WhatsApp messages in .txt format, pareses the DateTime, Sender and Message and outputs them as a CSV file for furtur analysis/visualisation.

## Requirements

### Windows

    Python 3+
    virtualenv
    Git Bash
    Command Line Interface

    NOTE: All commands that use "git" are done in Git Bash. It lets you use MinGW/Linux tools with Git at the command line.

### Linux/macOS

    Python 3+
    virtualenv
    Git
    Command Line Interface

## Set-up

    git clone git@github.com:UoMResearchIT/whatsapp-scraper.git

    cd whatsapp-scraper

### Virtual Environment

#### Windows

    $ virtualenv <virtualenv_name>

    $ <virtualenv_name>\Scripts\activate

    $ pip install -r requirements.txt

#### Linux

    $ virtualenv <virtualenv_name>

    $ source <virtualenv_name>/bin/activate

    $ pip install -r requirements.txt

## Running Scripts

1. Place the .txt files you want to process into the `whatsapp-scraper` directory.
2. In the command line run `whatsapp_scraper.py` 
3. The scripts will process all the .txt files in `whatsapp-scraper` and create new folders for each file, conataining the original .txt file and the new .csv file.

### Importing into Excel

To import the data in to Excel -

1. Open Excel,
2. Click the 'Data' panel.
3. Click 'From Text/CSV'
4. Choose the .csv you want to import,
5. Set 'File Origin" to '--None--' (at the top of the list), 'Delimiter' to 'Comma', Data Type Detection to 'Based on entire dataset'
6. Click 'Load'. The data will now be imported to the open worksheet.
