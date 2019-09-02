# WhatsApp Scraper

A script that takes WhatsApp messages in .txt format, pareses the DateTime, Sender and Message and outputs them as a CSV file for furtur analysis/visualisation.

> Set-up instructions have been divided into 'New User Set-up', directly below, and 'Experienced User Set-up', furthur down the page.

## New User Set-up

### **1. Downloading the Files**

Head to - https://github.com/UoMResearchIT/whatsapp-scraper

Click 'Clone or Download', select 'Download as .ZIP'

Unzip the file, put the 'whatsapp-scraper-master' into your 'Documents' directory.

### **2. Python Set-up**

Download Anaconda, a Python distribution, here - https://www.anaconda.com/distribution/

Choose your OS, and download the the 'Python 3.7 version'.

Once it has finished downloading, install it, choosing the default options.

### **3. Virtual Environment Set-up**

Open the 'Anaconda Navigator" application.

Click the 'Environments' tab on the left.

Click the 'Import' button at the bottom.

Click the folder button next to "Specification File'. Choose the environment.yml. That's in the whatsapp_scraper_master directory.

Click 'Import'

Once the environment is imported it will appear in the list of environments. It will be called 'whatsapp-conda-env'

### **4. Running the Script.**

Click the play button next to the 'whatsapp-conda-env' environment, and choose 'Open Terminal'.

In the terminal type 

`cd Documents`
`cd whatsapp-scraper-master`
`whatsapp_scraper.py` or `python whatsapp_scraper.py`

The script will run, creating a new directory for each chat txt file, inside it is the original .txt file along with a sorted .csv file.

### **5. Importing into Excel**

To import the data in to Excel -

1. Open Excel,
2. Click the 'Data' panel.
3. Click 'From Text/CSV'
4. Choose the .csv you want to import,
5. Set 'File Origin" to '--None--' (at the top of the list), 'Delimiter' to 'Comma', Data Type Detection to 'Based on entire dataset'
6. Click 'Load'. The data will now be imported to the open worksheet.

### **Re-running the script in the future.**

Open 'Anaconda Navigator'

Click the 'Environments' tab on the left.

Repeat the steps in **4. Running the Script.**

## Experienced User Set-up

### Requirements

#### Windows

    Python 3.7+
    virtualenv
    Git Bash
    Command Line Interface

    NOTE: All commands that use "git" are done in Git Bash. It lets you use MinGW/Linux tools with Git at the command line.

#### Linux/macOS

    Python 3.7+
    virtualenv
    Git
    Command Line Interface

### 1. Set-up

    git clone git@github.com:UoMResearchIT/whatsapp-scraper.git

    cd whatsapp-scraper

#### 2. Virtual Environment

##### Windows

    $ virtualenv <virtualenv_name>

    $ <virtualenv_name>\Scripts\activate

    $ pip install -r requirements.txt

##### Linux

    $ virtualenv <virtualenv_name>

    $ source <virtualenv_name>/bin/activate

    $ pip install -r requirements.txt

### 3. Running Scripts

1. Place the .txt files you want to process into the `whatsapp-scraper` directory.
2. In the command line run `whatsapp_scraper.py` 
3. The scripts will process all the .txt files in `whatsapp-scraper` and create new folders for each file, conataining the original .txt file and the new .csv file.

#### 4. Importing into Excel

To import the data in to Excel -

1. Open Excel,
2. Click the 'Data' panel.
3. Click 'From Text/CSV'
4. Choose the .csv you want to import,
5. Set 'File Origin" to '--None--' (at the top of the list), 'Delimiter' to 'Comma', Data Type Detection to 'Based on entire dataset'
6. Click 'Load'. The data will now be imported to the open worksheet.
